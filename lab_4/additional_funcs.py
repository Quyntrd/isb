import hashlib
import logging
import json
import time
import multiprocessing as mp
import matplotlib.pyplot as plt

from tqdm import tqdm

from file_readers import read_settings


def check_hash(x:int, bins: tuple, hash: str, last_numbers: str) -> tuple:
    """This function verificates hash"""
    x = str(x).zfill(6)
    for bin in bins:
        if hashlib.sha3_256(f"{bin}{x}{last_numbers}".encode()).hexdigest() == hash:
            return (bin, x, last_numbers)
    return None


def find_card_data(bins:tuple, hash: str, last_numbers: str, data_path: str) -> str:
    """This function searchs bank data"""
    try:
        args = []
        for i in range(0, 1000000):
            args.append((i, bins, hash, last_numbers))
        with mp.Pool(processes=mp.cpu_count()) as p:
            for result in p.starmap(check_hash, args):
                if result:
                    logging.info(f"Number of card: {result[0]}{result[1]}{result[2]}")
                    p.terminate()
                    try:
                        with open(data_path, "w") as file:
                            json.dump({"card_number": str(f"{result[0]}{result[1]}{result[2]}")}, file)
                            return str(f"{result[0]}{result[1]}{result[2]}")
                    except Exception as exc:
                        logging.error(f"Failed to save data: {exc}")
    except Exception as exc:
        logging.error(f"Failed to find the card data: {exc}")


def luhn_algorithm(card_numbers: str) -> bool:
    """This function checks the card number with Luhn algorithm"""
    try:
        result = int(card_numbers[-1])
        list_numbers = [int(i) for i in (card_numbers[::-1])]
        for i, num in enumerate(list_numbers):
            if i%2 == 0:
                mul = num*2
                if mul > 9:
                    mul -= 9
                list_numbers[i] = mul
        total_sum = sum(list_numbers)
        rem = total_sum % 10
        check_sum = 10 - rem if rem != 0 else 0
        if check_sum == result:
            logging.info("Card data successfully completed the Luhn algorithm")
            return True
        else:
            logging.info("Card data unsuccessfully completed the Luhn algorithm")
            return False
    except Exception as exc:
        logging.error(f"Failed to execute the luhn algorithm: {exc}")


def time_measurement(bins: tuple, hash: str, last_numbers: str) -> None:
    """This function measures time and draws the graph of time and processes"""
    try:
        args = []
        for i in range(0, 1000000):
            args.append((i, bins, hash, last_numbers))
        times_list = []
        for i in tqdm(range(1, int(mp.cpu_count()* 1.5)), desc ="Processes"):
            start = time.time()
            with mp.Pool(processes=i) as p:
                for result in p.starmap(check_hash, args):
                    if result:
                        end = time.time() - start
                        times_list.append(end)
                        p.terminate()
                        break
        fig=plt.figure(figsize=(15, 5))
        plt.plot(range(len(times_list)), times_list, linestyle = ":", color= "green", marker="x", markersize = 10)
        plt.bar(range(len(times_list)), times_list)
        plt.xlabel("Processes")
        plt.ylabel("Time, sec")
        plt.title("График зависимости времени выполнения программы от числа процессов")
        plt.show()
    except Exception as exc:
        logging.error(f"Failed measuring time: {exc}")


if __name__ == "__main__":
    settings = read_settings()

    result = find_card_data(settings["bins"], settings["hash"], settings["last_numbers"], settings["data_path"])
    luhn_algorithm(result)
    time_measurement(settings["bins"], settings["hash"], settings["last_numbers"])
        