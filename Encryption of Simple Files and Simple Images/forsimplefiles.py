from cryptography.fernet import Fernet
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
def decrypt (filename,key):
    f = Fernet(key)
    with open(filename,"rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename,"wb") as file:
        file.write(decrypted_data)
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="I am still bored to death and I am still encrypting random things.")
    parser.add_argument("file",help="File to encryt/decrypt")
    parser.add_argument("-g", "--generate-key", dest="generate_key", action="store_true",
                        help="Whether to generate a new key or use existing")
    parser.add_argument("-e", "--encrypt", action="store_true",help="Whether to encrypt the file, only -e or -d can be specified.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Whether to decrypt the file, only -e or -d can be specified.")
    args = parser.parse_args()
    file = args.file
    generate_key = args.generate_key
    if generate_key:
        write_key()
    key = load_key()


    encrypt_ = args.encrypt
    decrypt_ = args.decrypt

    if encrypt_ and decrypt_:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it")
    elif encrypt_:
        encrypt(file,key)
    elif decrypt_:
        key = load_key()
        decrypt(file,key)
    else:
        raise TypeError("Please specify whether you want to encrypt the file or decrypt it.")