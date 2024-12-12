import re


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()

    result = 0
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    rows = len(data)
    cols = len(data[0])
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                word = ""
                cx, cy = i, j
                for _ in range(4):
                    if cx not in range(rows) or cy not in range(cols):
                        break
                    word += data[cx][cy]
                    cx += dx
                    cy += dy
                if word == "XMAS":
                    result += 1

    print(result)

    

if __name__ == "__main__":
    main()
