class Vigenere_modified:
    def __init__(self, key):
        self.string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,:;'\"/\\<>(){}[]-=_+?!@#$%^&*~`"
        self.key = self.set_key(key)
        self.key_index = 0

    def set_key(self, key):
        # Switch case for months
        switcher = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December"
        }
        return switcher.get(key, "Invalid month")

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
    month = input("Enter the month of the year: ")
    vigenere = Vigenere_modified(month)
    print("Public key: ", vigenere.key)
    plaintext = 'Fucker'
    ciphertext = vigenere.encrypt(plaintext)
    print("Ciphertext: ", ciphertext)
    print("Plaintext: ", vigenere.decrypt(ciphertext))


if __name__ == "__main__":
    main()
