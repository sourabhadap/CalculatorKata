import re
from typing import List


def check_multiple_delimiters(delimiter: str):
    delimiter = delimiter.replace('[', '').replace(']', ',')
    delimiter = delimiter.split(',')
    return delimiter


def check_numbers_value(value: str) -> bool:
    pattern = r'^-?\d+(\.\d+)?$'  # Regex pattern to match a negative or positive number
    result = bool(re.match(pattern, value))
    return result


def validate_and_update_multiple_delimiters(delimiters: List[str], numbers: str):
    for i in delimiters:
        if i in numbers:
            numbers = numbers.replace(i, ',')
        else:
            raise Exception(f'Invalid delimiter: {i}')
    numbers_list = numbers.split(',')
    return numbers_list


def validate_numbers(numbers: List[str]):
    for n in numbers:
        if check_numbers_value(n) is False:
            raise Exception(f'Invalid number: {n}')


def split_numbers(numbers) -> List[str]:
    delimiter = ','
    if numbers.startswith('//['):
        delimiter, numbers = numbers.split('\n', 1)
        delimiter = delimiter[3:-1]
        delimiters = check_multiple_delimiters(delimiter)
        numbers_list = validate_and_update_multiple_delimiters(delimiters, numbers)
        print(numbers_list)
    elif numbers.startswith('//'):
        delimiter, numbers = numbers.split('\n', 1)
        delimiter = delimiter[2:]
        numbers = numbers.replace('\n', delimiter)
        numbers_list = numbers.split(delimiter)
    else:
        numbers = numbers.replace('\n', delimiter)
        numbers_list = numbers.split(delimiter)
    return numbers_list


def check_negative_numbers(numbers: List[str]):
    negative_numbers = [int(n) for n in numbers if int(n) < 0]
    if negative_numbers:
        raise Exception(f'Negatives not allowed: {negative_numbers}')


def check_bigger_numbers(numbers: List[str]):
    numbers = [0 if int(n) > 1000 else int(n) for n in numbers]
    return numbers


def add(numbers: str) -> int:
    if numbers == '':
        return 0
    numbers_list = split_numbers(numbers)
    validate_numbers(numbers_list)
    check_negative_numbers(numbers_list)
    numbers_list = check_bigger_numbers(numbers_list)
    print(sum(map(int, numbers_list)))
    return sum(map(int, numbers_list))


if __name__ == '__main__':
    add('//[**][%%]\n1**2%%3')
