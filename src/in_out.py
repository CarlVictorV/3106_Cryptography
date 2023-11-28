import datetime
import os
import hashlib

if os.name == "nt":
    append = "\\"
else:
    append = "/"


class in_out_plain():
    def __init__(self, file_name, month, day, year):
        self.file_name = file_name
        if self.check_file_exists():
            self.file_data = self.read_file()
            self.md5 = self.create_MD5()
        else:
            self.file_data = None
            self.md5 = None
        self.month = month
        self.day = day
        self.year = year
        self.date = datetime.datetime(self.year, self.month, self.day)

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

    def output(self):
        with open(f"output{append}ciphertext.txt", "w") as file:
            file.write(self.file_data)

    def set_file_name(self, file_name):
        self.file_name = file_name

    # TODO - ADD Hashing Algorithms MD5, SHA256
    #      - ADD Checksum
    

    def create_MD5(self):
        return hashlib.md5(self.file_data.encode()).hexdigest()
    
    def check_MD5(self, md5):
        if self.md5 == md5:
            return True
        return False
    
    def create_SHA256(self):
        return hashlib.sha256(self.file_data.encode()).hexdigest()


class in_out_cipher(in_out_plain):
    def __init__(self, file_name, month, day, year, private_key, modulus):
        super().__init__(file_name, month, day, year)
        self.private_key = private_key
        self.modulus = modulus

    def get_private_key(self):
        return self.private_key

    def set_private_key(self, private_key):
        self.private_key = private_key

    def get_modulus(self):
        return self.modulus

    def set_modulus(self, modulus):
        self.modulus = modulus
