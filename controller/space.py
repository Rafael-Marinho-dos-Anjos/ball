""" Space controller
"""

from model.dot import Dot


class Space():
    def __init__(self, width: int, height: int, dot_size: int, timestamp: float) -> None:
        self.width = width
        self.height = height
        self.dot = Dot(width//2, height//2, dot_size)
        self.timestamp = timestamp

    def actualizate(self):
        self.dot.actualizate(self.timestamp)
        if self.dot.x <= self.dot.size:
            self.dot.mirror_x()
        elif self.dot.x >= self.width - self.dot.size:
            self.dot.mirror_x()

        if self.dot.y <= self.dot.size:
            self.dot.mirror_y()
        elif self.dot.y >= self.height - self.dot.size:
            self.dot.mirror_y()
