import pygame

class Front:
    def __init__(self, root, color):
        self.root = root
        self.color = color
        self.x = 65
        self.y = 65

    def display(self):
        pygame.draw.circle(self.root, self.color, (self.x, self.y), 25)

class Gunner:
    def __init__(self):
        pass

class Cart:
    def __init__(self):
        pass

class Horse:
    def __init__(self):
        pass

class Elephant:
    def __init__(self):
        pass

class Guard:
    def __init__(self):
        pass

class General:
    def __init__(self):
        pass

