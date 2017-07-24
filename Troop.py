import pygame

pygame.init()
pygame.font.init()

class Font:
    def add_text(root, size, text, color, posx, posy):
        myfont = pygame.font.SysFont('SimHei', size)
        surf = myfont.render(text, False, color)
        root.blit(surf, (posx,posy))

class Front(Font):
    def __init__(self, root, color, txt_color):
        self.root = root
        self.color = color
        self.txt_color = txt_color
        self.x = 65
        self.y = 65

    def display(self):
        pygame.draw.circle(self.root, self.color, (self.x, self.y), 25)
        self.add_text(self.root, 10, '卒', self.txt_color, self.x, self.y)
        

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

