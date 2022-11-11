import pygame
 
class Ball:
    MAX_VELOC = 6
    COLOR = (255, 255, 255)

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VELOC
        self.y_vel = 0

    def draw_ball(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move_ball(self):
        self.x += self.x_vel
        self.y += self.y_vel

    def reset_ball(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1
