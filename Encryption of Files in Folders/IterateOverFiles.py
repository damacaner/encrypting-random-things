from cryptography.fernet import Fernet
from argparse import ArgumentTypeError as err
import os
from pathlib import Path
def write_key():
    #Generate a key and store it
    key = Fernet.generate_key()
    with open("encryptionkey.txt","wb") as file:
        file.write(key)
def load_key():
    return open("encryptionkey.txt","rb").read()
def encrypt (filename,key):
    f = Fernet(key)
    with open(filename,"rb") as file:
        file_data = file.read()
    encrypteddata = f.encrypt(file_data)
    with open(filename,"wb") as datafilew:
        datafilew.write(encrypteddata)
    #Too lazy to write decryption function, run encryption function one more time and it will decrypt itself.
def encryptfolder (foldername,key):
    files = Path(foldername).glob("*")
    for file in files:
        f = Fernet(key)
        with open(file, "rb") as filer:
            file_data = filer.read()
        encrypteddata = f.encrypt(file_data)
        with open(file, "wb") as filew:
            filew.write(encrypteddata)
def decryptfolder (foldername,key):
    files = Path(foldername).glob("*")
    for file in files:
            f = Fernet(key)
            with open(file, "rb") as filer:
                encrypted_data = filer.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(file, "wb") as filew:
                filew.write(decrypted_data)
def decrypt (filename,key):
    f = Fernet(key)
    with open(filename,"rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename,"wb") as file:
        file.write(decrypted_data)
class FileOfType:
    def __init__(self, type):
        self.type = type
        assert type in ['dir', 'file']
    def __call__(self, path):
        if self.type == 'dir':
            if not os.path.isdir(path):
                raise argparse.ArgumentTypeError(f"{path} is not a directory")
        elif self.type == 'file':
            if not os.path.isfile(path):
                raise argparse.ArgumentTypeError(f"{path} is not a regular file")
            elif os.path.islink(path):
                raise argparse.ArgumentTypeError(f"{path} is a symbolic link")
        return path
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="I am still bored to death and I am still encrypting random things.")
    # parser.add_argument("file",help="File to encryt/decrypt")
    parser.add_argument("-g", "--generate-key", dest="generate_key", action="store_true",
                        help="Whether to generate a new key or use existing")
    parser.add_argument("-e", "--encrypt", action="store_true",help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Whether to decrypt the file, only -e or -d can be specified.")
    parser.add_argument("-dir", "--directory", type=FileOfType('dir'))
    parser.add_argument("-f", "--file", type=FileOfType('file'))
    parser.add_argument("-ef","--encrypt_folder", action="store_true",help="Encrypt entire folder")
    parser.add_argument("-df", "--decrypt_folder", action="store_true", help="Decrypt entire folder")
    args = parser.parse_args()
    print(parser.parse_args())
    generate_key = args.generate_key
    if generate_key:
        write_key()
    key = load_key()

    encrypt_ = args.encrypt
    decrypt_ = args.decrypt
    encryptf = args.encrypt_folder
    decryptf = args.decrypt_folder
    if encrypt_ and decrypt_:
       raise TypeError("Please specify whether you want to encrypt the file or decrypt it")
    elif encrypt_:
       file = args.file
       key = load_key()
       encrypt(file,key)
    elif decrypt_:
       file = args.file
       key = load_key()
       decrypt(file,key)
    else:
       pass

    if encryptf and decryptf:
       raise TypeError("Please specify whether you want to encrypt the files or decrypt them")
    elif encryptf:
        directory = args.directory
        key = load_key()
        encryptfolder(directory,key)
    elif decryptf:
        directory = args.directory
        key = load_key()
        decryptfolder(directory,key)



