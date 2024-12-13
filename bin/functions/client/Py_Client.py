import selectors
import socket
import time
import pickle
import traceback

from PySide6.QtCore import QObject, Signal, Slot

# debugging exceptions: [Class](function)->errorMessage
class Client:
    def __init__(self):
        self.clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # IPV4|TCP
        self.SERVER_ADDRESS = ('', 9999)
        self.sel = selectors.DefaultSelector()  # handles multiple connections with .select()
        self.alive = False
        # maximum size of bytes that can be received per call
        self.BUFFER_SIZE = 4096
        # main data access points
        self.sendBuffer = bytearray()
        self.recvBuffer = bytearray()
        # the first bytes we read are the querySize they help us know the query limits bcz we are reading from a stream of bytes -> QueryQueryQuery...
        self.querySize = None
        # we will use this to send a signal when we recv query from server
        self.signals = ClientSignals()

    @Slot(dict)
    def getQuery(self):
        self.recvBuffer = self.recvBuffer[:self.querySize]
        query = pickle.loads(self.recvBuffer)  # bytes to -> python obj (dict)
        self.signals.query.emit(query)  # send signal to Functions class with the query
        # buffer drained (readyUp for new query)
        self.recvBuffer = self.recvBuffer[self.querySize:]
        self.querySize = None

    def getQuerySize(self):
        querySizeBytes = self.recvBuffer.split(b'.', 1)[0]+b'.'
        self.recvBuffer = self.recvBuffer[len(querySizeBytes):]
        self.querySize = pickle.loads(querySizeBytes)

    def recvIt(self):
        try:  # receive and fragment all chunks
            chunk = self.clientSocket.recv(self.BUFFER_SIZE)
            if chunk:
                self.recvBuffer.extend(chunk)  # append to recvBufferByteArray
        except BlockingIOError:
            pass  # Resource temporarily unavailable (errno EWOULDBLOCK)
        except OSError:  # expecting [WinError 10054] (server down)
            raise OSError(f"[Client](recvIt)->Connection was forcibly closed by the remote host")  # the event loop will close connection

    def readQuery(self):
        self.recvIt()
        if self.recvBuffer:
            if self.querySize is None:
                self.getQuerySize()
            if self.querySize is not None:  # don't put "else" here
                if len(self.recvBuffer) >= self.querySize:
                    self.getQuery()

    def createQuery(self, isCmd: bool = False, isCmdResult: bool = False, **kwargs):
        kwargs['isCmd'] = isCmd
        kwargs['isCmdResult'] = isCmdResult
        queryBytes = pickle.dumps(kwargs)
        querySizeBytes = pickle.dumps(len(queryBytes))
        self.sendBuffer = querySizeBytes + queryBytes
        # Set selector to listen for read events, we're done writing.
        self.sel.modify(self.clientSocket, selectors.EVENT_WRITE)

    def writeQuery(self):
        if self.sendBuffer:
            try:  # send until the buffer is drained
                bytesSent = self.clientSocket.send(self.sendBuffer)
                self.sendBuffer = self.sendBuffer[bytesSent:]
            except OSError:  # expecting [WinError 10054] (server is down)
                raise OSError(f"[Client](write)->Connection was forcibly closed by the remote host")
        if not self.sendBuffer:
            self.sel.modify(self.clientSocket, selectors.EVENT_READ)

    def disconnect(self):
        if self.alive:
            # close connection with server
            self.alive = False
            self.sel.unregister(self.clientSocket)
            self.clientSocket.close()
            self.sel.close()

    def startEventLoop(self):
        while self.alive:
            events = self.sel.select(timeout=0.2)  # we must put a timeOut here bcz we are modifying the socket selectors events while iterating to save some cpu cycles
            for key, mask in events:
                try:
                    if mask & selectors.EVENT_READ:  # If socket is ready for reading, then mask and selectors.EVENT_READ is True (bitwise)
                        self.readQuery()
                    if mask & selectors.EVENT_WRITE:  # If socket is ready for writing, then mask and selectors.EVENT_WRITE is True (bitwise)
                        self.writeQuery()
                except Exception as err:
                    # print(traceback.format_exc())
                    print(err)
                    self.disconnect()
                    self.signals.hostLeft.emit()  # hostLeft or you got kicked

    def connect(self, serverAddress: tuple):
        # reset
        self.sendBuffer = bytearray()
        self.recvBuffer = bytearray()
        self.SERVER_ADDRESS = serverAddress
        try:
            self.clientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)  # IPV4|TCP
            self.clientSocket.connect(self.SERVER_ADDRESS)
            self.clientSocket.setblocking(False)
            self.sel.register(fileobj=self.clientSocket, events=selectors.EVENT_READ | selectors.EVENT_WRITE, data=None)
            self.alive = True
        except Exception as err:  # expecting [WinError 10061] can't connect to server
            print("[Client](connect)->", err)
            self.alive = False




class ClientSignals(QObject):
    query = Signal(dict)
    hostLeft = Signal()