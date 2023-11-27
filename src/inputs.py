import datetime
import os

if os.name == "nt":
    append = "\\"
else:
    append = "/"


class Input():
    def __init__(self, file_name, month, day, year, type):
        self.file_name = file_name
        if self.check_file_exists():
            self.file_data = self.read_file()
        else:
            self.file_data = None
        self.month = month
        self.day = day
        self.year = year
        self.date = datetime.datetime(self.year, self.month, self.day)
        self.today = datetime.datetime.today()
        self.type = type

    def check_file_exists(self):
        if self.file_name == None:
            return False

        if not self.file_name.endswith(".txt"):
            self.file_name += ".txt"

        self.file_name = f"input{append}" + self.file_name

        try:
            with open(self.file_name, "r") as file:
                pass
        except FileNotFoundError:
            return False
        return True

    def read_file(self):
        self.file_data = None
        with open(self.file_name, "r") as file:
            self.file_data = file.read()
        return self.file_data

    def set_file_name(self, file_name):
        self.file_name = file_name


class Output():
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def store(self, data):
        if self.type == "plaintext":
            self.type_encrypt(data)
        elif self.type == "ciphertext":
            self.type_decrypt(data)
        else:
            print("Error: Invalid output type.")

    def type_decrypt(self, data):
        with open(f"output{append}plaintext.txt", "w") as file:
            file.write(data)
        print(f"Decrypted text stored in output{append}plaintext.txt")

    def type_encrypt(self, data):
        with open(f"output{append}ciphertext.txt", "w") as file:
            file.write(data)
        print(f"Encrypted text stored in output{append}ciphertext.txt")


def test():
    input = Input("input_cipher.txt", 1, 1, 2020, "ciphertext")
    print(input.file_data)
    


if __name__ == "__main__":
    test()
