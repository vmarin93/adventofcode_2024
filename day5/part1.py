def main():
    with open("input.txt", 'r') as f:
        data = f.read()

    sum = 0
    rules = []
    for rule in data.strip().split("\n\n")[0].split("\n"):
        a = int(rule.split("|")[0])
        b = int(rule.split("|")[1])
        rules.append((a,b))

    for update_string in data.strip().split("\n\n")[1].split("\n"):
        update = []
        add = True
        for num in update_string.split(","):
            update.append(int(num))
        for a,b in rules:
            if a in update and b in update and update.index(a) > update.index(b):
                add = False
                break
        if add:
            sum += update[len(update) // 2]

    print(sum)


if __name__ == "__main__":
    main()
