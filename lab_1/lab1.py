import json
import argparse


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
ARR_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-/;<=>?@[\]^_`"


def encryption_decryption_of_text(encryption_key_file, input_file, mode):
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
        print(output)
    except Exception as exc:
        print(f"Error encrypting of decrypting text: {exc}")

encryption_decryption_of_text("C:/Users/ROfl/Desktop/oib-lab1/isb/lab_1/key.json", "C:/Users/ROfl/Desktop/oib-lab1/isb/lab_1/encrypted.txt", 'decryption')