import math

class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        ciphertext = [''] * self.key
        for col in range(self.key):
            pointer = col
            while pointer < len(plaintext):
                ciphertext[col] += plaintext[pointer]
                pointer += self.key
        return ''.join(ciphertext)

    def decrypt(self, ciphertext):
        numOfColumns = math.ceil(len(ciphertext) / self.key)
        numOfRows = self.key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(ciphertext)
        plaintext = [''] * numOfColumns
        col = 0
        row = 0
        for symbol in ciphertext:
            plaintext[col] += symbol
            col += 1
            if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1
        return ''.join(plaintext)

    def getKey(self):
        return self.key


def main():
    myMessage = "y#qtv⌂r{pr~y)⌂y30cbfgooil9X[♣♀♀^^]  ^BBK▬▬MG¶↓JB     ♦SV☺W☺_↨▼→              ▼§Mj☼☼IJ▼MioH♣k↔YCq→@►j▲L↑Q"
    myKey = 1+1
    print('Message: %s' % (myMessage))

    myCipher = TranspositionCipher(myKey)
    ciphertext = myCipher.encrypt(myMessage)
    print('Encrypted: %s' % (ciphertext))
    plaintext = myCipher.decrypt(ciphertext)
    print('Decrypted: %s' % (plaintext))


if __name__ == '__main__':
    main()
