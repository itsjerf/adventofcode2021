inputfile = "input.txt"
data = []
with open(inputfile, 'r') as f:
    for line in f:
        data.append(int(line))

prev_n = 0
p1_count = 0
for i, n in enumerate(data):
    if i == 0:
        prev_n = n
        continue
    p1_count += 1 if n > prev_n else 0
    prev_n = n

print("How many measurements are larger than the previous measurement?")
print(f"-- {p1_count}")