inputfile = "input.txt"
data = []
with open(inputfile, 'r') as f:
    for line in f:
        data.append(int(line))

prev_n = 0
p2_count = 0
for i, n in enumerate(data[:-2]):
    n_sum = sum(data[i:i+3])
    if not prev_n:
        prev_n = n_sum
        continue
    p2_count += 1 if n_sum > prev_n else 0
    prev_n = n_sum

print("How many measurements are larger than the previous measurement?")
print(f"-- {p2_count}")