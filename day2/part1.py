def main():
    with open("input.txt") as f:
        lines = f.readlines()
    
    reports = []
    
    for line in lines:
        report = [int(num) for num in (line.strip('\n').split(" "))]
        if increasing(report) or decreasing(report):
            reports.append(report)
    print(len(reports))


def above_limits(x, y):
    if abs(x - y) < 1 or abs(x - y) > 3:
        return True
    return False


def increasing(list):
    for i in range(len(list) - 1):
        if not list[i] < list[i + 1] or above_limits(list[i], list[i + 1]):
            return False
    return True


def decreasing(list):
    for i in range(len(list) - 1):
        if not list[i] > list[i + 1] or above_limits(list[i], list[i + 1]):
            return False
    return True


if __name__ == "__main__":
    main()
