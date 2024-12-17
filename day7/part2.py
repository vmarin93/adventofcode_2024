from typing import Tuple
from collections import deque


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    sum = 0
    for line in data:
        test_value = int(line.strip().split(":")[0])
        numbers = [int(number) for number in line.split(":")[1].split()]
        if are_numbers_good(test_value, numbers):
            sum += test_value
    print(sum)


def are_numbers_good(test_value, numbers):
    totals: deque[Tuple[int, int]] = deque([(numbers[0], 1)])
    while totals:
        current_total, index = totals.popleft()
        if index == len(numbers):
            if current_total == test_value:
                return True
            continue
        next_number = numbers[index]
        totals.append((current_total + next_number, index + 1))
        totals.append((concatenate(current_total, next_number), index + 1))
        totals.append((current_total * next_number, index + 1))
    return False


def concatenate(x, y):
    z_string = str(x) + str(y)
    z = int(z_string)
    return z


if __name__ == "__main__":
    main()
