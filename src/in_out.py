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
        else:
            self.file_data = None
        self.month = month
        self.day = day
        self.year = year

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

    def output(self, private_key, modulus):
        Date = ("Date: " + str(self.month) + "/" +
                str(self.day) + "/" + str(self.year) + "\n")
        temp = self.file_data
        self.read_file()
        MD5 = ("MD5: " + str(self.create_md5()) + "\n")
        SHA256 = ("SHA256: " + str(self.create_sha256()) + "\n")
        private_key = ("Private Key: " + str(private_key) + "\n")
        modulus = ("Modulus: " + str(modulus) + "\n\n")
        with open(f"output{append}ciphertext.txt", "w") as file:
            file.write(Date)
            file.write(MD5)
            file.write(SHA256)
            file.write(private_key)
            file.write(modulus)
            file.write(temp)

    def create_md5(self):
        md5 = hashlib.md5(self.file_data.encode())
        return md5.hexdigest()

    def create_sha256(self):
        sha256 = hashlib.sha256(self.file_data.encode())
        return sha256.hexdigest()


class in_out_cipher():
    def __init__(self, file_name):
        self.file_name = file_name
        self.month = None
        self.day = None
        self.year = None
        self.private_key = None
        self.modulus = None
        self.md5 = None
        self.sha256 = None
        self.file_data = None
        self.encrypted_data = None
        if self.check_file_exists():
            self.read_file()
        else:
            self.file_data = None

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
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()
                # Initialize a variable to store encrypted data
                encrypted_data = []

                for line in lines:
                    parts = line.strip().split(': ')
                    if len(parts) == 2:
                        key, value = parts
                        if key == 'Date':
                            # Extract date components
                            self.month, self.day, self.year = map(
                                int, value.split('/'))
                        elif key == 'MD5':
                            self.md5 = value
                        elif key == 'SHA256':
                            self.sha256 = value
                        elif key == 'Private Key':
                            self.private_key = int(value)
                        elif key == 'Modulus':
                            self.modulus = int(value)
                    else:
                        # Assuming everything after the last structured entry is encrypted data
                        encrypted_data.append(line.strip())

                # Join the encrypted data into a single string
                self.encrypted_data = ''.join(encrypted_data)
        except FileNotFoundError:
            print("File not found or unable to read.")

    def checker(self):
        if self.md5 == None or self.sha256 == None or self.private_key == None or self.modulus == None:
            return False

        # Print the output
        print("Date: " + str(self.month) + "/" +
              str(self.day) + "/" + str(self.year))
        print("MD5: " + str(self.md5))
        print("SHA256: " + str(self.sha256))
        print("Private Key: " + str(self.private_key))
        print("Modulus: " + str(self.modulus))
        print("Encrypted Data: " + str(self.encrypted_data))

        return True

    def output(self):
        # Input the data or the plain text
        with open(f"output{append}plaintext.txt", "w") as file:
            file.write(self.file_data)

        # Then open the file and save the data to self.file_data
        with open(f"output{append}plaintext.txt", "r") as file:
            self.file_data = file.read()

        # Then calculate the MD5 and SHA256
        temp_md5 = hashlib.md5(self.file_data.encode())
        temp_sha256 = hashlib.sha256(self.file_data.encode())

        # Then open the file write the previous MD5 & SHA256 to the file
        # Then also write the new MD5 & SHA256 to the file
        # Then input the plain text to the file
        with open(f"output{append}plaintext.txt", "w") as file:
            file.write("Prev MD5: " + str(self.md5) + "\n")
            file.write("Prev SHA256: " + str(self.sha256) + "\n")
            file.write("MD5: " + str(temp_md5.hexdigest()) + "\n")
            file.write("SHA256: " + str(temp_sha256.hexdigest()) + "\n")
            file.write(self.file_data)


if __name__ == "__main__":
    # Get the current date
    testcipher = in_out_cipher("ciphertext.txt")
    testcipher.checker()
