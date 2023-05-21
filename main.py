from typing import List


def split_numbers(numbers) -> List[str]:
    delimiter = ','
    if numbers.startswith('//['):
        delimiter, numbers = numbers.split('\n', 1)
        delimiter = delimiter[3:-1]
    elif numbers.startswith('//'):
        delimiter, numbers = numbers.split('\n', 1)
        delimiter = delimiter[2:]
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
    check_negative_numbers(numbers_list)
    numbers_list = check_bigger_numbers(numbers_list)
    print(sum(map(int, numbers_list)))
    return sum(map(int, numbers_list))


if __name__ == '__main__':
    add('//[***]\n1***1001***3')
