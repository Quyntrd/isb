import json
import argparse

from enum import Enum


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-/;<=>?@[\]^_`"


class Mode(Enum):
    ENCRYPTION = 'encryption'
    DECRYPTION = 'decryption'


def read_json_file(input_file: str):
    """This function reads file and returns json.load
    
    Parametres:
        input_file(str): path of the input file"""
    with open(input_file, "r", encoding="utf-8") as f:
        return json.load(f)


def read_and_up_file(input_file: str) -> str:
    """This function reads and uppers characters in text
    
    Paramentres:
        input_file(str): path of the input file"""
    with open(input_file, "r", encoding="utf-8") as f:
        return f.read().upper()


def create_and_write_file(output_file: str, output: str) -> None:
    """This function creates new file and writes data into it
    
    Parametres:
        output_file(str): path and name of the output file
        
        output(str): text that needed to be written"""
    with open(output_file, "x", encoding="utf-8") as o:
        o.write(output)


def encryption_decryption_of_text(encryption_key_file: str, input_file: str, output_file: str, mode: str) -> None:
    """This function encrypts or decrypts text from input file into output file
                
    Parametres:
        encryption_key_file(str): path for json file with step in it

        input_file(str): path of the txt input file with text

        output_file(str): name of the txt output file for encrypted or decrypted text

        mode(str): mode for encrypting/decrypting"""
    try:
        templates = read_json_file(encryption_key_file)
        step = templates["step"]
        data = read_and_up_file(input_file)
        output = ""
        m = Mode.ENCRYPTION if mode == 'encryption' else Mode.DECRYPTION
        for i in data:
            place = ALPHABET.find(i)    
            new_place = 0
            if m == Mode.ENCRYPTION:
                new_place = place + step
            elif m == Mode.DECRYPTION:
                new_place = place - step
            if i in ALPHABET:
                output += ALPHABET[new_place]
            else:
                output += i
        create_and_write_file(output_file, output)
    except Exception as exc:
        print(f"Error encrypting of decrypting text: {exc}")


def char_frequency(input_file: str) -> None:
    """This function checks the frequency of the characters in the text
                
    Parametres:
        input_file(str): path of the input file with text"""
    try:
        text = read_and_up_file(input_file)
        count = len(text)
        for char in LETTERS:
            if char in text:
                count_symbol = text.count(char)
                print(f"{char}({count_symbol}) : {count_symbol / count}")
    except Exception as exc:
        print(f"Error checking letter frequency in text: {exc}")


def frequency_decryption(input_file: str, replacements: str, output_file: str):
    """This function decrypts text with found keys and writes the result into output file
                
    Parametres:
        input_file(str): path of the input file with text
        
        replacements(str): path of the json file with keys
        
        output_file(str): name of the txt output file for encrypted or decrypted text"""
    try:
        replacement = read_json_file(replacements)
        encoded_text = read_and_up_file(input_file)
        output = ""
        for char in encoded_text:
            decoded_char = replacement.get(char, char)
            output += decoded_char
        create_and_write_file(output_file, output)
    except Exception as exc:
        print(f"Error in decrypting text using frequency analysis method: {exc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Substitution encryption/decryption")
    parser.add_argument("--kf", default="key.json", help="Path to the encryption key file")
    parser.add_argument("--i", default="text.txt", help="Path to the input file")
    parser.add_argument("--out", default= "encrypted.txt", help="Path to the output file")
    parser.add_argument("--out1", default= "decrypted-cod9.txt", help="Path to the output file")
    parser.add_argument("--c9", default="cod9.txt", help = "Path to the cod(var).txt file")
    parser.add_argument("--r", default="replacements.json", help="Path to the replacements file")
    parser.add_argument("--m", default="encryption", choices=['encryption', 'decryption'], help="Mode of operation: encryption or decryption")
    args = parser.parse_args()

    encryption_decryption_of_text(args.kf, args.i, args.out, args.m)
    char_frequency(args.c9)
    frequency_decryption(args.c9, args.r, args.out1)