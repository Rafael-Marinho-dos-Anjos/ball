""" Play control
"""

from controller.space import Space
from keyboard import is_pressed
import cv2
import numpy as np


class Game():
    def __init__(self,
                 width: int,
                 height: int,
                 dot_size: int,
                 timestamp: float = 0.1) -> None:
        self.space = Space(width, height, dot_size, timestamp)
        self.end = False
        self.timestamp = timestamp
        cv2.namedWindow('Dot floating', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Dot floating', width, height)

    def control(self):
        if is_pressed("up"):
            self.space.dot.accelerate("y", True)
        elif is_pressed("down"):
            self.space.dot.accelerate("y", False)
        else:
            self.space.dot.accelerate("y", stop=True)

        if is_pressed("right"):
            self.space.dot.accelerate("x", False)
        elif is_pressed("left"):
            self.space.dot.accelerate("x", True)
        else:
            self.space.dot.accelerate("x", stop=True)
        self.space.actualizate()
        cv2.imshow('Dot floating', self.draw_window())
        cv2.waitKey(1)

    def draw_window(self):
        img = np.ones((self.space.height, self.space.width, 3), dtype=np.uint8) * 255
        for point in self.space.dot.points():
            try:
                img[point[1], point[0], 0] = 0
                img[point[1], point[0], 1] = 0
                img[point[1], point[0], 2] = 255
            except:
                pass
        
        return img
