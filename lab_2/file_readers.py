import json


def read_json_file(input_file: str):
    """This function reads file and returns json.load
    
    Parametres:
        input_file(str): path of the input file"""
    with open(input_file, "r", encoding="utf-8") as f:
        return json.load(f)
    

def write_file(output_file: str, output: str) -> None:
    """This function writes data into text file
    
    Parametres:
        output_file(str): path and name of the output file
        
        output(str): text that needed to be written"""
    with open(output_file, "w", encoding="utf-8") as o:
        o.write(output)