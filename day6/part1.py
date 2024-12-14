def main():
    with open("input.txt", "r") as f:
        data = f.readlines()
    
    start = get_start(data)
    visited = set()
    directions = [
        (-1, 0), #up
        (0, 1), #right
        (1, 0), #down
        (0, -1), #left
    ]
    travel(start, data, visited, directions)
    print(len(visited))


def travel(start, data, visited, directions):
    x, y = start
    current_dir = 0

    while True:
        visited.add((x, y))

        dx, dy = directions[current_dir]
        new_x, new_y = x + dx, y + dy

        if not is_on_map(new_x, new_y, data):
            break

        if data[new_x][new_y] == "#":
            current_dir = (current_dir + 1) % len(directions)
            dx, dy = directions[current_dir]
            new_x, new_y = x + dx, y + dy
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
