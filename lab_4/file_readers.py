import json
import os


def read_settings(file_path: str):
    """This function reads file and returns json.load
    
    Parametres:
        input_file(str): path of the input file"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as exc:
        print(f"Failed to read json file: {exc}")
