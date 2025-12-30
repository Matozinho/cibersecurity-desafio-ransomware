import argparse
from cryptoutils import generate_key, process_file

def main():
    parser = argparse.ArgumentParser(description="Educational Encryption Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: gen-key
    key_parser = subparsers.add_parser("gen-key", help="Generate a new secret key")
    key_parser.add_argument("-o", "--out", required=True, help="Path to save the generated key")

    # Command: encrypt
    enc_parser = subparsers.add_parser("encrypt", help="Encrypt a file")
    enc_parser.add_argument("-f", "--file", required=True, help="File to encrypt")
    enc_parser.add_argument("-k", "--key", required=True, help="Path to the secret key")

    # Command: decrypt
    dec_parser = subparsers.add_parser("decrypt", help="Decrypt a file")
    dec_parser.add_argument("-f", "--file", required=True, help="File to decrypt")
    dec_parser.add_argument("-k", "--key", required=True, help="Path to the secret key")

    args = parser.parse_args()

    if args.command == "gen-key":
        generate_key(args.out)
    elif args.command == "encrypt":
        process_file(args.file, args.key, encrypt=True)
    elif args.command == "decrypt":
        process_file(args.file, args.key, encrypt=False)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()