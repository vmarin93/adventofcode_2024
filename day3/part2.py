import re


def main():
    with open("input.txt", "r") as f:
        data = f.read().strip()

    result = 0
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    matches = re.finditer(pattern, data)
    flag = True
    for match in matches:
        if match.group(0) == "do()":
            flag = True
        elif match.group(0) == "don't()":
            flag = False
        else:
            if flag:
                result += int(match.group(1)) * int(match.group(2))
    print(result)


if __name__ == "__main__":
    main()
