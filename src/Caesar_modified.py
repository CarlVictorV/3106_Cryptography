class Caesar:
    def __init__(self, day):
        self.key = self.create_key(day)
        self.characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def create_key(self, days):
        if days == 9:
            return 41
        elif days == 18:
            return 42
        elif days == 27:
            return 43
        else:
            return days

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
    ciphertext = "47B384A8-5B7B96AC-BA4786B4-BBBB6693-46656A67-B4C7BBBA-89C834BA-43346C68-98C87448-AAB8C6BC-BA4786B4-46656A67-B4C7BBBA-89C834BA-BBBB6693-BBBB6693-5B7B96AC-43346C68-A37B8557-BA4786B4-5B7B96AC-AC8A7654"
    print("Ciphertext:", ciphertext)
    decrypted_plaintext = caesar.decrypt(ciphertext)
    print("Decrypted plaintext:", decrypted_plaintext)


if __name__ == "__main__":
    main()
