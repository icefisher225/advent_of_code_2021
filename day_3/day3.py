import os, sys, time, math

def decimalToBinary(n):
    return bin(n).replace("0b","")

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal   

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
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            #print(j)
            if matrix[i][j] == "1":
                out[j] += 1
            else:
                out[j] -= 1
    #print(out)

    for item in out:
        if item > 0:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)

    
    gam_val = ""
    eps_val = ""

    gamma.reverse()
    epsilon.reverse()

    iter = False
    print(f"{gamma}, {epsilon}")

    for item in gamma:
        print(item)
        if item == 0 and iter == False:
            pass
        else:
            iter = True
            gam_val += str(item)
            print(gam_val)
    #print()
    iter = False
    for item in epsilon:
        #print(item)
        if item == 0 and iter == False:
            pass
        else:
            iter = True
            eps_val += str(item)
    
    print(f"{gam_val}, {eps_val}")

    #gam_val = gam_val[::-1]
    #eps_val = eps_val[::-1]

    print(f"{gam_val}, {eps_val}")
    #print(f"{binaryToDecimal(gam_val)}*{binaryToDecimal(eps_val)}")
    #print(binaryToDecimal(gam_val))

if __name__ == "__main__":
    main()