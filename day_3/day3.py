import os, sys, time, math, copy

dpr = True

def dprint(arg):
    global dpr
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
    global dpr
    matrix, gamma, epsilon, o2, co2 = list(), list(), list(), list(), list()
    with open("input.txt", "r") as f:
        for line in f:
            matrix.append([char for char in line.strip()])

    for i in range(len(matrix[0])):
        ones, zeros = 0, 0
        for j in range(len(matrix)):
            if str(matrix[j][i]) == "0":
                zeros += 1
            else:
                ones += 1
        dprint(f"{ones}, {zeros}")
        if ones > zeros:
            gamma.append(1)
            epsilon.append(0)
        elif ones == zeros:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    
    print(f"\ngamma = {gamma}, epsilon = {epsilon}")
    print(f"dec(gamma) = {binaryToDecimal(gamma)}, dec(epsilon) = {binaryToDecimal(epsilon)}")
    print(f"part1 answer={binaryToDecimal(gamma)*binaryToDecimal(epsilon)}\n")

    orig = copy.deepcopy(matrix)

    o2_filter, co2_filter = list(), list()
    co2_flag, o2_flag = False, False
    for i in range(len(matrix[0])):
        val = 0
        if len(matrix) == 1:
            o2_filter = matrix[0]
            o2_flag = True
        if len(matrix) == 1:
            o2 = matrix[0]
            break
        
        dpr = False
        for j in range(len(matrix)):
            val += int(matrix[j][i])
        if 2*val > len(matrix):
            o2_filter.append(1)
            dprint("Case 1")
        elif 2*val == len(matrix):
            o2_filter.append(1)
            dprint("Case 2")
        else: #val < 500
            dprint("Case 3")
            o2_filter.append(0)
        dpr = True
        dprint(f"val={val}")
        matrix = filter_matrix(o2_filter, matrix, i)
        

    for i in range(len(orig[0])):
        val = 0
        if len(orig) == 1:
            co2 = orig[0]
            break

        dpr = False
        for item in orig:
            val += int(item[i])
        if 2*val > len(orig):
            co2_filter.append(0)
            dprint("Case 1")
        elif 2*val == len(orig):
            co2_filter.append(0)
            dprint("Case 2")
        else: #val < 500
            co2_filter.append(1)
            dprint("Case 3")
        dpr = True
        dprint(f"val={val}")
        orig = filter_matrix(co2_filter, orig, i)


    o2 = matrix[0]
    co2 = orig[0]

    for i in range(len(o2)):
        o2[i] = int(o2[i])
        co2[i] = int(co2[i])

    print(f"\no2_filter = {o2_filter}, co2_filter = {co2_filter}")
    print(f"o2 =        {o2}, co2 =        {co2}")
    print(f"dec(o2) = {binaryToDecimal(o2)}, dec(co2) = {binaryToDecimal(co2)}")
    print(f"part2 answer = {binaryToDecimal(o2)*binaryToDecimal(co2)}\n")


def filter_matrix(target, matrix, i):
    try:
        #dprint(len(matrix))
        if len(matrix) == 1:
            #dprint("\n")
            return matrix[0]
        value = target[i]
        removed = 0
        for j in range(len(matrix)):
            if str(value) == str(matrix[j-removed][i]):
                pass
            else:
                matrix.remove(matrix[j-removed])
                removed += 1
        return matrix
    except Exception as e:
        print(f"target={target}, matrix, i={i}")
        raise(e)
    #raise ValueError("There is an error in your code")
    
            

if __name__ == "__main__":
    main()