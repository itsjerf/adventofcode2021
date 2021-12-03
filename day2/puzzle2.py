inputfile = "input.txt"
data = []
with open(inputfile, 'r') as f:
    for line in f:
        data.append(line.strip("\n"))

h = 0
v = 0
a = 0
for i in data:
    args = i.split(" ")
    cmd = args[0]
    val = int(args[1])
    if cmd == "forward":
        h += val
        v += a * val
    elif cmd == "down":
        a += val
    elif cmd == "up":
        a -= val
print(f"Horizontal: {h}")
print(f"Vertical: {v}")
print(f"Product: {h * v}")