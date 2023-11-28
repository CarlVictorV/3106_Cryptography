class Caesar:
    def __init__(self, day: int):
        self.key = self.create_key(day)

    def create_key(self, days: int) -> int:
        if days in [9, 18, 27]:
            return days + 40
        else:
            return days

    def encrypt(self, plaintext: str) -> str:
        ciphertext = ""
        for char in plaintext:
            if char == "-":
                ciphertext += "-"
            else:
                ciphertext += self.encrypt_char(char)
        return ciphertext

    def encrypt_char(self, char: str) -> str:
        num = int(char)
        hold = num + self.key
        return CHARACTERS[hold % len(CHARACTERS)]

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ""
        for char in ciphertext:
            if char == "-":
                plaintext += "-"
            else:
                plaintext += self.decrypt_char(char)
        return plaintext

    def decrypt_char(self, char: str) -> str:
        num = CHARACTERS.index(char)
        hold = num - self.key
        return CHARACTERS[hold % len(CHARACTERS)]

    def get_public_key(self) -> int:
        return self.key


CHARACTERS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


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
