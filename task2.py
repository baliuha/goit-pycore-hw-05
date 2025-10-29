import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator:
    """
    Finds all numerical values in the given text and yields them one by one
    """
    number_pattern = r"\s+[-+]?\d+(\.\d+)?\s+"
    matches = re.finditer(number_pattern, text)
    for match in matches:
        yield match.group().strip()


def sum_profit(text: str, func: Callable) -> float:
    """
    Calculates the total sum of all numbers found in the text using a generator
    """
    total = 0.0
    for number in func(text):
        total += float(number)

    return total


text = "The employee’s total income consists of several components:  " \
    "1000.01 dollars as the base salary, supplemented by additional " \
    "earnings of 27.45 and 324.00 dollars."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income}")
