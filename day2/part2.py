def main():
    with open("input.txt") as f:
        lines = f.readlines()
    
    #unsafe = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
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


#def remove_level(report):
#    for i in range(len(report) - 1):
#        if above_limits(report[i], report[i + 1]):
#            if should_pop(report, i):
#                report.pop(i)
#                return
#            if should_pop(report, i + 1):
#                report.pop(i + 1)
#                return
#
#    for i in range(len(report) - 2):
#        if report[i] < report[i + 1] and report[i + 1] > report[i + 2]:
#            if should_pop(report, i + 2):
#                report.pop(i + 2)
#                return
#            if should_pop(report, i):
#                report.pop(i)
#                return
#            if should_pop(report, i + 1):
#                report.pop(i + 1)
#                return
#        if report[i] > report[i + 1] and report[i + 1] < report[i + 2]:
#            if should_pop(report, i + 2):
#                report.pop(1 + 2)
#                return
#            if should_pop(report, i):
#                report.pop(i)
#                return
#            if should_pop(report, i + 1):
#                report.pop(i + 1)
#                return
#    return

def should_pop(report, i):
    temp = report.copy()
    temp.pop(i)
    if is_safe(temp):
        return True
    return False


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
