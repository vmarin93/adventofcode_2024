def main():
    with open("input.txt") as f:
        lines = f.readlines()
    
    safe = []
    
    for line in lines:
        report = [int(num) for num in (line.strip('\n').split(" "))]
        if is_safe(report):
            safe.append(report)
            continue
        for i in range(len(report)):
            temp = report.copy()
            temp.pop(i)
            if is_safe(temp):
                safe.append(temp)
                break

    print(len(safe))


def is_safe(report):
    if increasing(report) or decreasing(report):
        return True
    return False


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
