import hashlib
import sys

def test_md5():
    test = "Carl Victor Villaceran"
    md5 = hashlib.md5(test.encode())
    return md5.hexdigest()

    

def test_sha256():
    test = "Carl Victor Villaceran"
    sha256 = hashlib.sha256(test.encode())
    return sha256.hexdigest()

def main():
    print(test_md5())
    print(test_sha256())

if __name__ == "__main__":
    main()