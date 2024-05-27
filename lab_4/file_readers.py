import json
import os


def read_settings():
    """This function reads file and returns json.load
    
    Parametres:
        input_file(str): path of the input file"""
    try:
        with open(os.path.join("lab_4", "settings.json"), "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as exc:
        print(f"Failed to read json file: {exc}")