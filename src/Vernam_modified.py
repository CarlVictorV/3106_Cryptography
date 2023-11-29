import hashlib


class Vernam_modified:
    def __init__(self, key):
        self.key = key
        self.key_length = len(key)
        self.substitute_char = '\x01'  # Substitute character for removal

    def encrypt(self, message):
        encrypted_message = ""
        for i in range(len(message)):
            encrypted_char = chr(ord(message[i]) ^ ord(
                self.key[i % self.key_length]))
            if encrypted_char in self.get_problematic_chars():
                encrypted_char = self.substitute_char
            encrypted_message += encrypted_char
        return encrypted_message

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        for i in range(len(encrypted_message)):
            decrypted_char = chr(ord(encrypted_message[i]) ^ ord(
                self.key[i % self.key_length]))
            if decrypted_char in self.get_problematic_chars():
                decrypted_char = self.substitute_char
            decrypted_message += decrypted_char
        return decrypted_message

    def getKey(self):
        return self.key

    def get_problematic_chars(self):
        # Define your problematic characters here
        problematic_chars = ['\x00', '\x1a', '\x1c', '\x1d', '\x1e', '\x1f', '\x7f', '\x80', '\x81', '\x82', '\x83', '\x84',
                             '\x85', '\x86', '\x87', '\x88', '\x89', '\x8a', '\x8b', '\x8c', '\x8d', '\x8e', '\x8f',
                             '\x90', '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', '\x97', '\x98', '\x99', '\x9a',
                             '\x9b', '\x9c', '\x9d', '\x9e', '\x9f', '\xa0', '\xa1', '\xa2', '\xa3', '\xa4', '\xa5',
                             '\xa6', '\xa7', '\xa8', '\xa9', '\xaa', '\xab', '\xac', '\xad', '\xae', '\xaf', '\xb0',
                             '\xb1', '\xb2', '\xb3', '\xb4', '\xb5', '\xb6', '\xb7', '\xb8', '\xb9', '\xba', '\xbb',
                             '\xbc', '\xbd', '\xbe', '\xbf', '\xc0', '\xc1', '\xc2', '\xc3', '\xc4', '\xc5', '\xc6',
                             '\xc7', '\xc8', '\xc9', '\xca', '\xcb', '\xcc', '\xcd', '\xce', '\xcf', '\xd0', '\xd1',
                             '\xd2', '\xd3', '\xd4', '\xd5', '\xd6', '\xd7', '\xd8', '\xd9', '\xda', '\xdb', '\xdc',
                             '\xdd', '\xde', '\xdf', '\xe0', '\xe1', '\xe2', '\xe3', '\xe4', '\xe5', '\xe6', '\xe7',
                             '\xe8', '\xe9', '\xea', '\xeb', '\xec', '\xed', '\xee', '\xef', '\xf0', '\xf1', '\xf2',
                             '\xf3', '\xf4', '\xf5', '\xf6', '\xf7', '\xf8', '\xf9', '\xfa', '\xfb', '\xfc', '\xfd',
                             '\xfe', '\xff']
        return problematic_chars


def main():
    myMessage = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,:;'\"/\\<>(){}[]-=_+?!@#$%^&*~`"
    md5 = hashlib.md5(myMessage.encode()).hexdigest()
    sha256 = hashlib.sha256(myMessage.encode()).hexdigest()
    myKey = md5 + sha256
    print('Message  : %s' % (myMessage))

    myCipher = Vernam_modified(myKey)
    ciphertext = myCipher.encrypt(myMessage)
    print('Encrypted: ' + ciphertext)
    plaintext = myCipher.decrypt(ciphertext)
    print('Decrypted: %s' % (plaintext))


if __name__ == '__main__':
    main()
