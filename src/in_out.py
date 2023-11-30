import binascii
import os
import hashlib

if os.name == "nt":
    append = "\\"
else:
    append = "/"


class in_out_plain():
    def __init__(self, file_name, month, day, year):
        self.file_name = file_name
        self.month = month
        self.day = day
        self.year = year
        self.file_data = self.read_file()
        self.md5 = self.create_md5()
        self.sha256 = self.create_sha256()

    def check_file_exists(self):
        if self.file_name == None:
            return False

        if not self.file_name.endswith(".txt"):
            self.file_name += ".txt"

        self.file_name = f"input{append}" + self.file_name

        return os.path.exists(self.file_name) and os.path.isfile(self.file_name)

    def read_file(self):
        if self.check_file_exists():
            with open(self.file_name, "r") as file:
                return file.read()
        return None

    def output(self, private_key, modulus, file_data):
        Date = f"Date: {self.month}/{self.day}/{self.year}\n"
        MD5 = f"MD5: {self.md5}\n"
        SHA256 = f"SHA256: {self.sha256}\n"
        private_key = f"Private Key: {private_key}\n"
        modulus = f"Modulus: {modulus}\n\n"
        self.file_name = self.file_name.split(append)[-1]
        self.file_name = self.file_name.split(".")[0]
        self.file_name += "_cipher.txt"
        with open(f"output{append}{self.file_name}", "w") as file:
            file.write(Date)
            file.write(MD5)
            file.write(SHA256)
            file.write(private_key)
            file.write(modulus)
            file.write(file_data)

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
            print("File does not exist")

    def check_file_exists(self):
        if self.file_name is None:
            return False

        if not self.file_name.endswith(".txt"):
            self.file_name += ".txt"

        self.file_name = f"input{append}" + self.file_name

        return os.path.isfile(self.file_name)

    def read_file(self):
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()

                metadata = {}
                encrypted_data = []

                for line in lines:
                    parts = line.strip().split(': ')
                    if len(parts) == 2:
                        key, value = parts
                        if key == 'Date':
                            # Extract date components
                            self.month, self.day, self.year = map(
                                int, value.split('/'))
                        else:
                            metadata[key] = value
                    else:
                        # Assuming everything after the last structured entry is encrypted data
                        encrypted_data.append(line.strip())

                # Store metadata and encrypted data
                self.md5 = metadata.get('MD5')
                self.sha256 = metadata.get('SHA256')
                self.private_key = int(metadata.get(
                    'Private Key')) if 'Private Key' in metadata else None
                self.modulus = int(metadata.get('Modulus')
                                   ) if 'Modulus' in metadata else None
                self.encrypted_data = ''.join(encrypted_data)

        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"File '{self.file_name}' not found or unable to read.") from e

    def calculate_hashes(self):
        if self.file_data:
            temp_md5 = hashlib.md5(self.file_data.encode())
            temp_sha256 = hashlib.sha256(self.file_data.encode())
            return temp_md5.hexdigest(), temp_sha256.hexdigest()
        return None, None

    def output(self):
        temp_md5, temp_sha256 = self.calculate_hashes()
        self.file_name = self.file_name.split(append)[-1]
        self.file_name = self.file_name.split(".")[0]
        self.file_name += "_plain.txt"
        with open(f"output{append}{self.file_name}", "w") as file:
            file.write(f"Previous MD5: {self.md5}\n")
            file.write(f"Previous SHA256: {self.sha256}\n")
            if temp_md5 and temp_sha256:
                file.write(f"Current MD5: {temp_md5}\n")
                file.write(f"Current SHA256: {temp_sha256}\n\n")
            file.write(self.file_data)

    def print_metadata(self):
        if self.md5 is None or self.sha256 is None or self.private_key is None or self.modulus is None:
            return False

        print("Date:", f"{self.month}/{self.day}/{self.year}")
        print("MD5:", self.md5)
        print("SHA256:", self.sha256)
        print("Private Key:", self.private_key)
        print("Modulus:", self.modulus)
        print("Encrypted Data:", self.encrypted_data)

        return True


class in_file():
    def __init__(self, file_name, month, day, year, file_type):
        self.file_name = file_name
        self.month = month
        self.day = day
        self.year = year
        self.file_type = file_type
        self.file_data = self.read_file()
        # Turn self.file_data into Hex
        self.md5 = self.create_md5()
        self.sha256 = self.create_sha256()

    def check_file_exists(self):
        if self.file_name is None:
            return False

        if not self.file_name.endswith(".{}".format(self.file_type)):
            self.file_name += ".{}".format(self.file_type)

        self.file_name = f"input{append}" + self.file_name

        return os.path.exists(self.file_name) and os.path.isfile(self.file_name)

    def read_file(self):
        if self.check_file_exists():
            with open(self.file_name, "rb") as file:
                file_contents = file.read()
                file_contents = binascii.hexlify(file_contents)
                return file_contents
        return None

    def output(self, private_key, modulus, file_data):
        Date = f"Date: {self.month}/{self.day}/{self.year}\n"
        MD5 = f"MD5: {self.md5}\n"
        SHA256 = f"SHA256: {self.sha256}\n"
        file_type = f"File Type: {self.file_type}\n"
        private_key = f"Private Key: {private_key}\n"
        modulus = f"Modulus: {modulus}\n\n"
        self.file_name = self.file_name.split(append)[-1]
        self.file_name = self.file_name.split(".")[0]
        self.file_name += "_cipher.txt"
        with open(f"output{append}{self.file_name}", "w") as file:
            file.write(Date)
            file.write(MD5)
            file.write(SHA256)
            file.write(file_type)
            file.write(private_key)
            file.write(modulus)
            file.write(file_data)

    def create_md5(self):
        md5 = hashlib.md5(self.file_data)
        return md5.hexdigest()

    def create_sha256(self):
        sha256 = hashlib.sha256(self.file_data)
        return sha256.hexdigest()


class out_file():
    def __init__(self, file_name):
        self.file_name = file_name
        self.month = None
        self.day = None
        self.year = None
        self.private_key = None
        self.modulus = None
        self.md5 = None
        self.sha256 = None
        self.file_type = None
        self.file_data = None
        self.encrypted_data = None
        if self.check_file_exists():
            self.read_file()
        else:
            self.file_data = None
            print("File does not exist")

    def check_file_exists(self):
        if self.file_name is None:
            return False

        if not self.file_name.endswith(".txt"):
            self.file_name += ".txt"

        self.file_name = f"input{append}" + self.file_name

        return os.path.isfile(self.file_name)

    def read_file(self):
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()

                metadata = {}
                encrypted_data = []

                for line in lines:
                    parts = line.strip().split(': ')
                    if len(parts) == 2:
                        key, value = parts
                        if key == 'Date':
                            # Extract date components
                            self.month, self.day, self.year = map(
                                int, value.split('/'))
                        else:
                            metadata[key] = value
                    else:
                        # Assuming everything after the last structured entry is encrypted data
                        encrypted_data.append(line.strip())

                # Store metadata and encrypted data
                self.md5 = metadata.get('MD5')
                self.sha256 = metadata.get('SHA256')
                self.private_key = int(metadata.get(
                    'Private Key')) if 'Private Key' in metadata else None
                self.modulus = int(metadata.get('Modulus')
                                   ) if 'Modulus' in metadata else None
                self.file_type = metadata.get('File Type')
                self.encrypted_data = ''.join(encrypted_data)

        except FileNotFoundError as e:
            raise FileNotFoundError(
                f"File '{self.file_name}' not found or unable to read.") from e

    def calculate_hashes(self):
        if self.file_data:
            temp_md5 = hashlib.md5(self.file_data.encode())
            temp_sha256 = hashlib.sha256(self.file_data.encode())
            return temp_md5.hexdigest(), temp_sha256.hexdigest()
        return None, None

    def output(self):
        print(self.calculate_hashes())
        self.file_name = self.file_name.split(append)[-1]
        self.file_name = self.file_name.split(".")[0]
        self.file_name += ".{}".format(self.file_type)
        # Convert to bytes
        self.hex_to_bytes()
        with open(f"output{append}{self.file_name}", "wb") as file:
            file.write(self.file_data)

    def print_metadata(self):
        if self.md5 is None or self.sha256 is None or self.private_key is None or self.modulus is None:
            return False

        print("Date:", f"{self.month}/{self.day}/{self.year}")
        print("MD5:", self.md5)
        print("SHA256:", self.sha256)
        print("Private Key:", self.private_key)
        print("Modulus:", self.modulus)
        print("Encrypted Data:", self.encrypted_data)

        return True

    def hex_to_bytes(self):
        # Check if file is odd length

        self.file_data = binascii.unhexlify(self.file_data)

def test():
    # Test in_file and out_file
    inn = in_file("Capture", 1, 1, 2020, "png")
    inn.check_file_exists()
    print(inn.file_data)
    # out = out_file("test")


if __name__ == "__main__":
    test()
