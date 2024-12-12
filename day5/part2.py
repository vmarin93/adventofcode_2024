def main():
    with open("input.txt", 'r') as f:
        data = f.read()

    answer = 0
    rules = []
    for rule in data.strip().split("\n\n")[0].split("\n"):
        a = int(rule.split("|")[0])
        b = int(rule.split("|")[1])
        rules.append((a,b))

    for update_string in data.strip().split("\n\n")[1].split("\n"):
        update = []
        is_sorted = True
        for num in update_string.split(","):
            update.append(int(num))
        for a,b in rules:
            if a in update and b in update and update.index(a) > update.index(b):
                is_sorted = False
                break
        if not is_sorted:
            sort_update(update, rules)
            answer += update[len(update) // 2]

    print(answer)


def sort_update(update, rules):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for a,b in rules:
            if a in update and b in update and update.index(a) > update.index(b):
                x, y = update.index(a), update.index(b)
                update[x], update[y] = update[y], update[x]
                is_sorted = False
    return update


if __name__ == "__main__":
    main()
