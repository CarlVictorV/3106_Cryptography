class Caesar:
    def __init__(self, key):
        self.key = key
        self.characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def encrypt(self, plaintext):
        ciphertext = ""
        for char in plaintext:
            if char == "-":
                ciphertext += "-"
            else:
                ciphertext += self.adder(char)
        return ciphertext

    def adder(self, char):
        num = int(char)
        hold = num + self.key
        return self.characters[hold]

    def subtractor(self, char):
        num = self.characters.index(char)
        hold = num - self.key
        return self.characters[hold]

    def decrypt(self, ciphertext):
        plaintext = ""
        for char in ciphertext:
            if char == "-":
                plaintext += "-"
            else:
                plaintext += self.subtractor(char)
        return plaintext

    def get_public_key(self):
        return self.key


def main():
    day = int(input("Enter the day of the month: "))
    caesar = Caesar(day)
    print("Public key:", caesar.get_public_key())
    plaintext = "13-24-355-43-52"
    print("Plaintext:", plaintext)
    ciphertext = caesar.encrypt(plaintext)
    print("Ciphertext:", ciphertext)
    decrypted_plaintext = caesar.decrypt(ciphertext)
    print("Decrypted plaintext:", decrypted_plaintext)


if __name__ == "__main__":
    main()
