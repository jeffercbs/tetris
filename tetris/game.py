import pygame
import random
import threading


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = 10
        self.y = 10

    def generate_snap(self):
        self.y += 1
        pygame.draw.rect(self.screen, (225, 225, 0), pygame.Rect(self.x, self.y, 20, 20))

    def init(self):
        set_interval(self.generate_snap(), 1000)
