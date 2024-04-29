import math
import json
import os
import mpmath
from typing import List
from scipy.special import gammainc
import file_readers


def frequency_bit_test(sequence: str) -> float:
    """
    """
    N = len(sequence)
    sum_bits = sum(1 if i == '1' else -1 for i in sequence)
    P = sum_bits / math.sqrt(N)
    P = math.erfc(P/math.sqrt(2))
    return P


def identical_bit_test(sequence: str) -> float:
    """
    """
    N = len(sequence)
    sum_bits = sum(int(i) for i in sequence)
    sig = sum_bits/N
    Vn = sum(1 for i in sequence if sequence[i] != sequence[i+1])
    P = math.erfc(abs(Vn-2*N*sig(1-sig))/(2*math.sqrt(2*N)* sig *(1-sig)))
    return P


def longest_subsequence(sequence: str, consts_PI: List[float]) -> float:
    """
    """
    