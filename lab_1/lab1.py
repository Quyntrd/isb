import json
import argparse


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
ARR_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-/;<=>?@[\]^_`"


def encryption_decryption_of_text(encryption_key_file, input_file, output_file, mode):
    try:
        with open(encryption_key_file, "r") as f:
            templates = json.load(f)
        step = templates["step"]
        with open(input_file, "r", encoding="utf-8") as file:
            data = file.read().upper()
        output = ""
        for i in data:
            place = ALPHABET.find(i)    
            new_place = 0
            match mode:
                case 'encryption':
                    new_place = place + step
                case 'decryption':
                    new_place = place - step
            if i in ALPHABET:
                output += ALPHABET[new_place]
            else:
                output += i
        with open(output_file, 'x') as out:
            out.write(output)
    except Exception as exc:
        print(f"Error encrypting of decrypting text: {exc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Substitution encryption/decryption")
    parser.add_argument("--kf", default="key.json", help="Path to the encryption key file")
    parser.add_argument("--i", default="text.txt", help="Path to the input file")
    parser.add_argument("--o", default= "encrypted.txt", help="Path to the output file")
    parser.add_argument("--m", default="encryption", choices=['encryption', 'decryption'], help="Mode of operation: encryption or decryption")
    args = parser.parse_args()

    encryption_decryption_of_text(args.kf, args.i, args.o, args.m)
