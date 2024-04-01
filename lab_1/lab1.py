import json
import argparse


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-/;<=>?@[\]^_`"


def encryption_decryption_of_text(encryption_key_file: str, input_file: str, output_file: str, mode: str) -> None:
    """This function encrypting or decryptin text from input file into output file
                
    Parametres:
        encryption_key_file(str): path for json file with step in it

        input_file(str): path of the input file with text

        output_file(str): name of the output file for encrypted or decrypted text

        mode(str): mode for encrypting/decrypting"""
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


def char_frequency(input_file: str) -> None:
    """This function checks the frequency of the characters in the text
                
    Parametres:
        input_file(str): path of the input file with text"""
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            original = file.read().upper()
        count = len(original)
        for char in LETTERS:
            if char in original:
                count_symbol = original.count(char)
                print(f"{char}({count_symbol}) : {count_symbol / count}")
    except Exception as exc:
        print(f"Error checking letter frequency in text: {exc}")






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Substitution encryption/decryption")
    parser.add_argument("--kf", default="key.json", help="Path to the encryption key file")
    parser.add_argument("--i", default="text.txt", help="Path to the input file")
    parser.add_argument("--o", default= "encrypted.txt", help="Path to the output file")
    parser.add_argument("--cod9", default="cod9.txt", help = "Path to the cod(var).txt file")
    parser.add_argument("--r", default="replacements.json", help="Path to the replacements file")
    parser.add_argument("--m", default="encryption", choices=['encryption', 'decryption'], help="Mode of operation: encryption or decryption")
    args = parser.parse_args()

    encryption_decryption_of_text(args.kf, args.i, args.o, args.m)
    char_frequency(args.cod9)

