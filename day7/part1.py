from typing import List, Tuple


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
    totals: List[Tuple[int, int]] = [(numbers[0], 1)]
    while totals:
        current_total, index = totals.pop(0)
        if index == len(numbers):
            if current_total == test_value:
                return True
            continue
        next_number = numbers[index]
        totals.append((current_total + next_number, index + 1))
        totals.append((current_total * next_number, index + 1))
    return False

if __name__ == "__main__":
    main()
