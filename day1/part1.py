with open("input.txt") as f:
    lines = f.readlines()
list_a = []
list_b = []
total_distance = 0

for line in lines:
    list_a.append(int(line.split("   ")[0]))
    list_b.append(int(line.split("   ")[1].strip('\n')))

list_a.sort()
list_b.sort()

print(list_a)
print(list_b)

for id_a, id_b in zip(list_a, list_b):
    total_distance += (abs(id_a - id_b))

print(total_distance)
