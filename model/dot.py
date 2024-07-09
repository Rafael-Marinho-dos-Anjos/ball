""" Dot module
"""

from math import sqrt


class Dot():
    def __init__(self, x, y, size) -> None:
        self.x = x
        self.y = y
        self.x_acc = 0
        self.x_vel = 0
        self.y_acc = 0
        self.y_vel = 0
        self.brk = 1
        self.acc = 5
        self.max_vel = 50
        self.size = size

    def actualizate(self, timestamp: float) -> None:
        if self.x_acc == 0:
            self.x_vel += timestamp * (-1) * self.brk if self.x_vel > 0 else timestamp * self.brk
            if timestamp * self.brk >= abs(self.x_vel):
                self.x_vel = 0
        elif self.x_vel**2 + self.y_vel**2 < self.max_vel**2 or \
            self.x_vel == 0 or \
            self.x_vel / abs(self.x_vel) != self.x_acc / abs(self.x_acc):
            self.x_vel += timestamp * self.x_acc
        
        if self.y_acc == 0:
            self.y_vel += timestamp * (-1) * self.brk if self.y_vel > 0 else timestamp * self.brk
            if timestamp * self.brk >= abs(self.y_vel):
                self.y_vel = 0
        elif self.x_vel**2 + self.y_vel**2 < self.max_vel**2 or \
            self.y_vel == 0 or \
            self.y_vel / abs(self.y_vel) != self.y_acc / abs(self.y_acc):
            self.y_vel += timestamp * self.y_acc

        self.x += timestamp * self.x_vel
        self.y += timestamp * self.y_vel

    def accelerate(self, axis: str, reverse: bool = False, stop: bool = False) -> None:
        if axis == "x":
            self.x_acc = self.acc
            if reverse:
                self.x_acc = self.acc * (-1)
            if stop:
                self.x_acc = 0

        elif axis == "y":
            self.y_acc = self.acc
            if reverse:
                self.y_acc = self.acc * (-1)
            if stop:
                self.y_acc = 0

        elif axis is None:
            self.x_acc = 0
            self.y_acc = 0

    def mirror_x(self) -> None:
        self.x_vel *= -1
        self.x_acc = 0

    def mirror_y(self) -> None:
        self.y_vel *= -1
        self.y_acc = 0
    
    def points(self) -> list:
        pnts = []
        for i in range(self.size):
            for j in range(self.size):
                if i ** 2 + j ** 2 > self.size ** 2:
                    continue
                pnts.append((int(self.x + i), int(self.y + j)))
                if i != 0:
                    pnts.append((int(self.x - i), int(self.y + j)))
                if j != 0:
                    pnts.append((int(self.x + i), int(self.y - j)))
                if i != 0 and j != 0:
                    pnts.append((int(self.x - i), int(self.y - j)))
        
        return pnts
