class Caesar:
    def __init__(self, day: int):
        self.key = day

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