import pygame

class Paddle:
    COLOR = (255, 255, 255)
    VEL = 6

    def __init__(self, x, y, width, height):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw_paddle(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move_paddle(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL
