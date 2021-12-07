import os, sys, time, math

class position:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
    
    @property
    def change_x_pos(self, amount):
        self.x_pos += amount
        return self.x_pos

    @property
    def change_y_pos(self, amount):
        self.y_pos += amount
        return self.y_pos

    @property
    def get_x(self):
        return self.x_pos

    @property
    def get_y(self):
        return self.y_pos




def main():
    commands = list()
    with open("input.txt", "r") as f:
        for line in f:
            commands.append(line.strip())
    pos = position()
    for command in commands:
        cmd = command.split(" ")
        if cmd[0] == "forward":
            pos.change_x_pos(int(cmd[1]))
        elif cmd[0] == "up":
            pos.change_y_pos(-1*int(cmd[1]))
        elif cmd[0] == "down":
            pos.change_y_pos(int(cmd[1]))

    print(f"{pos.get_x()*pos.get_y()}")


if __name__ == "__main__":
    main()