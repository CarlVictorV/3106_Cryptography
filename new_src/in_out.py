import datetime
import os

if os.name == "nt":
    append = "\\"
else:
    append = "/"


class in_out_plain():
    def __init__(self, file_name, month, day, year):
        self.file_name = file_name
        if self.check_file_exists():
            self.file_data = self.read_file()
        else:
            self.file_data = None
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
    
    def output(self, data):
        with open(self.file_name, "w") as file:
            file.write(data)

    def set_file_name(self, file_name):
        self.file_name = file_name
    
    #todo: create md5


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
