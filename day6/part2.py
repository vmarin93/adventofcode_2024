def main():
    with open("input.txt", "r") as f:
        data = f.readlines()
    
    data = [list(line.strip()) for line in data]
    start = get_start(data)
    directions = [
        (-1, 0), #up
        (0, 1), #right
        (1, 0), #down
        (0, -1), #left
    ]
    answer = 0
    for cx in range(len(data)):
        for cy in range(len(data[0])):
            if data[cx][cy] == "#" or data[cx][cy] == "^":
                continue
            data[cx][cy] = "#"
            if travel(start, data, directions):
                answer += 1
            data[cx][cy] = "."
    print(answer)


def travel(start, data, directions):
    x, y = start
    current_dir = 0
    visited = set()

    while True:
        if (x,y,current_dir) in visited:
            return True
        visited.add((x,y,current_dir))
        dx, dy = directions[current_dir]
        new_x, new_y = x + dx, y + dy

        if not is_on_map(new_x, new_y, data):
            return False

        if data[new_x][new_y] == "#":
            current_dir = (current_dir + 1) % len(directions)
            continue
        x, y = new_x, new_y



def is_on_map(cx, cy, data):
    if 0 <= cx < len(data) and 0 <= cy < len(data[0]):
        return True
    return False


def get_start(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "^":
                return (i, j)


if __name__ == "__main__":
    main()
