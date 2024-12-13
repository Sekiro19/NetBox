import configparser
import hashlib
import urllib.parse
import random
import pyimgur

########################
config = configparser.ConfigParser()
config.read(r'imgur.ini')

class ImgurService:
    def __init__(self):
        self.client = pyimgur.Imgur(client_id=config.get('ImgurInfo', 'client_id'),
                                    client_secret=config.get('ImgurInfo', 'client_secret'))

    def upload_img(self, img_path: str) -> str:
        img = self.client.upload_image(path=img_path)
        return img.link


class ImgService:
    @staticmethod
    def generate_img(value: any = random.random(), theme: str = 'random', size: int = 40) -> str:
        """
        :param value: generate image from value (if left empty it will generate image from a random number)
        :param theme: ('404', 'mp', 'identicon', 'monsterid', 'wavatar', 'retro', 'robohash', 'blank')
        :param size: default is (40X40)
        :return: Gravatar url
        """
        if theme == 'random':
            theme = random.choice(('identicon', 'monsterid', 'wavatar', 'retro', 'robohash'))
        default = "https://www.gravatar.com/avatar/"
        url = default + hashlib.md5(str(value).encode('utf-8')).hexdigest() + "?"
        url += urllib.parse.urlencode({'d': theme, 's': str(size)})
        return url



