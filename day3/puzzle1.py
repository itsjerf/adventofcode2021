inputfile = "input.txt"
data = []
with open(inputfile, 'r') as f:
    for line in f:
        data.append(line.strip("\n"))


zeroes = [0] * len(data[0])
ones = [0] * len(data[0])
for bstr in data:
    for i, bit in enumerate(bstr):
        if bit == "0":
            zeroes[i] += 1
        if bit == "1":
            ones[i] += 1

gamma = ""
epsilon = ""
for i in range(len(data[0])):
    if zeroes[i] > ones[i]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)
print(f"gamma: {gamma}")
print(f"epsilon: {epsilon}")

print(f"gamma_dec: {gamma_dec}")
print(f"epsilon_dec: {epsilon_dec}")

print(f"gamma * epsilon = {gamma_dec * epsilon_dec}")