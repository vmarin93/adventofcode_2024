with open("input.txt") as f:
    lines = f.readlines()
list_a = []
list_b = []
similarity_score = 0

for line in lines:
    list_a.append(int(line.split("   ")[0]))
    list_b.append(int(line.split("   ")[1].strip('\n')))

for id_a in list_a:
    count = 0
    for id_b in list_b:
        if id_a == id_b:
            count += 1
    similarity_score += (id_a * count)

print(similarity_score)
