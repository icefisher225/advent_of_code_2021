import os, sys, time, math

file = "depth_measurements.txt"

def main ():
    depths = list()
    with open(file, "r") as f:
        for line in f:
            try:
                depths.append(int(line.strip()))
            except Exception as e:
                print(line)
                print(e)
                exit()

    avg_depths = list()
    for i in range(2,len(depths)):
        try:
            avg_depths.append(depths[i-2]+depths[i-1]+depths[i])
        except Exception as e:
            print(e)
            exit()


    count = 0
    prev_depth = 999999
    for depth in avg_depths:
        if depth > prev_depth:
            count += 1
        prev_depth = depth

    print(f"number of depths that are greater: {count}")

if __name__ == "__main__":
    main()