class Vigenere_modified:
    def __init__(self, key):
        self.string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,:;'\"/\\<>(){}[]-=_+?!@#$%^&*~`"
        self.key = key
        self.key_index = 0

    def set_key(self, key):
        self.key = key

    def encrypt(self, plaintext):
        ciphertext = ""
        for i in range(len(plaintext)):
            char = plaintext[i]
            if char in self.string:
                ciphertext += self.string[(self.string.index(char) + self.string.index(
                    self.key[self.key_index])) % len(self.string)]
                self.key_index = (self.key_index + 1) % len(self.key)
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ""
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            if char in self.string:
                plaintext += self.string[(self.string.index(char) - self.string.index(
                    self.key[self.key_index])) % len(self.string)]
                self.key_index = (self.key_index + 1) % len(self.key)
            else:
                plaintext += char
        return plaintext


def main():
    month = int(input("Enter the month of the year: "))
    vigenere = Vigenere_modified(month)
    print("Public key: ", vigenere.key)
    plaintext = input("Enter the plaintext: ")
    ciphertext = vigenere.encrypt(plaintext)
    print("Ciphertext: ", ciphertext)
    print("Plaintext: ", vigenere.decrypt(ciphertext))


if __name__ == "__main__":
    main()
