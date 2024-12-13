import subprocess

psCmd = r"get.ps1"
result = subprocess.run(["powershell", psCmd], 
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                stdin=subprocess.PIPE, 
                                text=True)

print(result.stdout)
print(result.stderr)
