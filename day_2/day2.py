import os, sys, time, math

class position:
    def __init__(self, x_pos=0, y_pos=0, aim=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.aim = aim
    
    def change_aim(self, amount):
        self.x_pos += amount
        self.y_pos += self.aim*amount

    def change_y_pos(self, amount):
        self.aim += amount

    def get_x(self):
        return self.x_pos

    def get_y(self):
        return self.y_pos

    def get_aim(self):
        return self.aim




def main():
    commands = list()
    with open("input.txt", "r") as f:
        for line in f:
            commands.append(line.strip())
    #print(commands[0])
    posit = position()
    print(f"{posit.get_x()}, {posit.get_y()}, {posit.get_aim()}")
    time.sleep(5)
    for command in commands:
        cmd = command.split(" ")
        #print(f"{int(cmd[1])}")
        if cmd[0] == "forward":
            posit.change_aim(int(cmd[1]))
        elif cmd[0] == "up":
            posit.change_y_pos(-1*int(cmd[1]))
        elif cmd[0] == "down":
            posit.change_y_pos(int(cmd[1]))
        print(f"{posit.get_x()}, {posit.get_y()}, {posit.get_aim()}")

    print(f"{posit.get_x()*posit.get_y()}")


if __name__ == "__main__":
    main()