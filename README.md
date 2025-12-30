# Educational Ransomware Simulator (CLI)

This is a proof-of-concept (PoC) tool developed for educational purposes in the context of Information Security. It demonstrates how modern ransomware uses symmetric encryption to lock files and the importance of key management.

> **⚠️ WARNING:** This project is for educational purposes only. Never use this tool on files you do not have a backup of or on systems you do not own.

---

## 🛠 Features

* **AES-128 (CTR Mode):** Uses robust symmetric encryption.
* **CLI Interface:** Easy to use via command line arguments.
* **Key Management:** Separate module to generate and save unique 16-byte secret keys.
* **Universal:** Works with any file type (Images, PDFs, Text, Executables, etc.).

<img width="800" height="418" alt="image" src="https://github.com/user-attachments/assets/c97bdcd6-3757-41f7-a380-c0fc8b19ee89" />


## 🚀 Getting Started

### Prerequisites

You will need Python 3.x and the `pyaes` library. You can install the dependency via pip:

```bash
pip install pyaes
```

## Instalation

```bash
git clone https://github.com/Matozinho/cibersecurity-desafio-ransomware.git
cd cibersecurity-desafio-ransomware
```

## 💻 Usage
The tool is divided into three main commands: gen-key, encrypt, and decrypt.

### 1. Generate a Secret Key
First, you need to create a key file. This key is required for both encryption and decryption.

```bash
python main.py gen-key -o mykey.bin
```

### 2. Encrypt a File
To encrypt a file (e.g., document.pdf), run:

```bash
python main.py encrypt -f document.pdf -k mykey.bin
```
- Result: The original file is deleted, and a new file named document.pdf.ransomwaretroll is created.

### 3. Decrypt a File
To restore your file to its original state:

```bash
python main.py decrypt -f document.pdf.ransomwaretroll -k mykey.bin
```
- Result: The encrypted file is removed, and the original document.pdf is restored.

## 🧪 Educational Context
This project demonstrates the CTR (Counter Mode) of the AES algorithm. In this mode:

- A 16-byte key is used.
- The encryption process turns the plaintext into ciphertext that is indistinguishable from random noise.
- Without the .bin key file, recovering the original data is computationally unfeasible.

## Project Structure
- main.py: Entry point handling the CLI arguments.
- cryptoutils.py: Logic for AES encryption/decryption and key generation.
