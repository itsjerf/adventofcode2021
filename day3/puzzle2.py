def count_bits(bit_strs: list, index):
    ones = 0
    zeros = 0
    for bs in bit_strs:
        if bs[index] == "0":
            zeros += 1
        else:
            ones += 1
    return zeros, ones

def check_init_criteria(data, index, zeros, ones):
    carbon = []
    oxygen = []
    zeros, ones = count_bits(data, index)
    for d in data:
        if zeros == ones:
            if d[index] == "0":
                carbon.append(d)
            else:
                oxygen.append(d)
        elif zeros > ones:
            if d[index] == "0":
                oxygen.append(d)
            else:
                carbon.append(d)
        elif ones > zeros:
            if d[index] == "0":
                carbon.append(d)
            else:
                oxygen.append(d)
    return carbon, oxygen

def filter_by_criteria(oxygen, carbon, index):
    oxygen_i_to_remove = []
    carbon_i_to_remove = []
    for i, d in enumerate(oxygen):
        z, o = count_bits(oxygen, index)
        if z == o:
            if d[index] == "0":
                oxygen_i_to_remove.append(i)
        if z > o:
            if d[index] == "1":
                oxygen_i_to_remove.append(i)
        if o > z:
            if d[index] == "0":
                oxygen_i_to_remove.append(i)
    
    for i, d in enumerate(carbon):
        z, o = count_bits(carbon, index)
        if z == o:
            if d[index] == "1":
                carbon_i_to_remove.append(i)
        if z > o:
            if d[index] == "0":
                carbon_i_to_remove.append(i)
        if o > z:
            if d[index] == "1":
                carbon_i_to_remove.append(i)

    oxygen_i_to_remove.reverse()
    carbon_i_to_remove.reverse()
    for idx in oxygen_i_to_remove:
        if len(oxygen) == 1:
            break
        oxygen.pop(idx)
    for idx in carbon_i_to_remove:
        if len(carbon) == 1:
            break
        carbon.pop(idx)

def main():
    inputfile = "input.txt"
    data = []
    with open(inputfile, 'r') as f:
        for line in f:
            data.append(line.strip("\n"))

    carbon = []
    oxygen  = []
    for i in range(len(data[0])):
        if i == 0:
            z, o = count_bits(data, i)
            clist, olist = check_init_criteria(data, i, z, o)
            carbon.extend(clist)
            oxygen.extend(olist)
        else:
            filter_by_criteria(oxygen, carbon, i)

    print(f"carbon: {carbon}")
    print(f"oxygen: {oxygen}")
    print(f"product: {int(oxygen[0], 2) * int(carbon[0], 2)}")


if __name__ == '__main__':
    main()