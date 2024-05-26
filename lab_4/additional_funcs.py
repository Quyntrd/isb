import hashlib
import logging
import json
import os
import time
import multiprocessing as mp
import matplotlib.pyplot as plt

import tqdm


def check_hash(x:int, bins: tuple, hash: str, last_numbers: str) -> tuple:
    x = str(x).zfill(6)
    for bin in bins:
        if hashlib.blake2b(f"{bin}{x}{last_numbers}".encode()).hexdigest() == hash:
            return (bin, x, last_numbers)
    return None



def find_card_data(bins:tuple, hash: str, last_numbers: str, data_path: str) -> str:
    try:
        args = []
        for i in range(0, 1000000):
            args.append((i, bins, hash, last_numbers))
        with mp.Pool(processes=mp.cpu_count()) as p:
            for result in p.starmap(check_hash, args):
                if result:
                    logging.info(f"Number of card: {result[0]}-{result[1]}-{result[2]}")
                    p.terminate()
                    try:
                        with open(data_path, "w") as file:
                            json.dump({"card_number": str(f"{result[0]}-{result[1]}-{result[2]}")}, file)
                            return str(f"{result[0]}-{result[1]}-{result[2]}")
                    except Exception as exc:
                        logging.error(f"Failed to save data: {exc}")
    except Exception as exc:
        logging.error(f"Failed to find the card data: {exc}")



def luhn_algorithm(card_numbers: str) -> bool:
    



def time_measurement(bins: tuple, hash: str, last_numbers: str) -> None:




if __name__ == "__main__":
    