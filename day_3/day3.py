import os, sys, time, math, copy

def dprint(arg):
    dpr = False
    if dpr == True:
        print(arg)

def binaryToDecimal(binary):
    bin=list()
    if type(binary) == str:
        bin.append(int(char) for char in binary)
    elif type(binary) == list:
        bin = copy.deepcopy(binary)
        for i in range(len(bin)):
            bin[i] = int(bin[i])
    bin.reverse()
    iter = 1
    dec = 0
    for num in bin:
        if num == 1:
            dec += iter
        iter *= 2
    return dec


def main():
    matrix = list()
    with open("input.txt", "r") as f:
        for line in f:
            matrix.append([char for char in line.strip()])

    out = []
    gamma = []
    epsilon = []

    for i in range(len(matrix[0])):
        out.append(0)


    for i in range(len(matrix[0])):
        ones = 0
        zeros = 0
        for j in range(len(matrix)):
            if matrix[j][i] == "0":
                zeros += 1
            else:
                ones += 1
        dprint(f"{ones}, {zeros}")
        if ones > zeros:
            out[i] = 1
        else:
            out[i] = 0
            

    for item in out:
        if item == 0:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)
    
    print(f"\ngamma = {gamma}, epsilon = {epsilon}")
    print(f"dec(gamma) = {binaryToDecimal(gamma)}, dec(epsilon) = {binaryToDecimal(epsilon)}")
    print(f"part1 answer={binaryToDecimal(gamma)*binaryToDecimal(epsilon)}\n")

    o2 = list()
    co2 = list()

    orig = copy.deepcopy(matrix)

    dprint(f"filtering matrix by gamma:   {gamma}")
    o2 = filter_matrix(gamma, matrix)
    dprint(matrix)
    dprint(f"filtering matrix by epsilon: {epsilon}")
    co2 = filter_matrix(epsilon, orig)
    dprint(orig)

    for i in range(len(o2)):
        o2[i] = int(o2[i])
        co2[i] = int(co2[i])

    print(f"\ngamma = {gamma}, epsilon = {epsilon}")
    print(f"o2 =    {o2}, co2 =     {co2}")
    print(f"dec(o2) = {binaryToDecimal(o2)}, dec(co2) = {binaryToDecimal(co2)}")
    print(f"part2 answer = {binaryToDecimal(o2)*binaryToDecimal(co2)}\n")


def filter_matrix(target, matrix):
    for i in range(len(matrix[0])):
        dprint(len(matrix))
        if len(matrix) == 1:
            dprint("\n")
            return matrix[0]
        value = target[i]
        removed = 0
        for j in range(len(matrix)):
            if str(value) == str(matrix[j-removed][i]):
                pass
            else:
                matrix.remove(matrix[j-removed])
                removed += 1
    raise ValueError("There is an error in your code")
    
            

if __name__ == "__main__":
    main()