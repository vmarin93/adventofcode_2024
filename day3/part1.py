import re


def main():
    with open("input.txt", "r") as f:
        data = f.read()

    result = 0
    pattern = r"mul\((\d+),(\d+)\)"
    muls = re.findall(pattern, data)
    for mul in muls:
        result += int(mul[0]) * int(mul[1])
    print(result)


if __name__ == "__main__":
    main()
