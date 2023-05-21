def add(numbers: str) -> int:
    if numbers == '':
        return 0
    delimiter = ','
    if numbers.startswith('//'):
        pass
    numbers = numbers.replace('\n', delimiter)
    numbers_list = numbers.split(delimiter)
    negative_numbers = [int(n) for n in numbers_list if int(n) < 0]
    if negative_numbers:
        raise Exception(f'Negatives not allowed: {negative_numbers}')
    return sum(map(int, numbers_list))


if __name__ == '__main__':
    add('1\n2,3')
