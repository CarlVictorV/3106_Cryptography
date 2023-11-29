import base64
import hashlib
from random import Random


class AES:
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]
    
    def getKey(self):
        return self.key
    
def main():
    myMessage = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,:;'\"/\\<>(){}[]-=_+?!@#$%^&*~`"
    md5 = hashlib.md5(myMessage.encode()).hexdigest()
    sha256 = hashlib.sha256(myMessage.encode()).hexdigest()
    myKey = md5 + sha256
    print('Message  : %s' % (myMessage))

    myCipher = AES(myKey)
    ciphertext = myCipher.encrypt(myMessage)
    print('Encrypted: ' + ciphertext)

if __name__ == '__main__':
    main()