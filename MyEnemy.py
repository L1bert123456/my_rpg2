import pygame
#import time
from constants import *
import Projective
from pygame.sprite import Sprite, collide_rect


class Mob(pygame.sprite.Sprite):
    def __init__(self, START_Y, START_X, dir):
        super().__init__()
        self.image = pygame.image.load('data/hpframe.png').convert_alpha()
        self.rect = self.image.get_rect(center=(START_X, START_Y))
        self.rect = self.image.get_rect()
        self.state = ALIVE
        self.x = START_X
        self.y = START_Y
        self.rect.x = self.x
        self.rect.y = self.y
        self.dir = dir
        self.hp = orge_HP
        self.mp = orge_MP
        self.spell_casted = 0
        self.mooving = [0, 0, 0, 0]

    def render(self, screen):
        # screen.blit(self.images[self.direction][self.state], (self.x, self.y))
        screen.blit(self.images[self.dir][0], (self.x, self.y))

class Orge(Mob):
    def __init__(self,  START_X, START_Y, dir):
        self.image_pack = ['data/orge_left.png', 'data/orge_down.png', 'data/orge_right.png', 'data/orge_up.png']
        self.speed = 5
        self.images = []
        Mob.__init__(self, START_X, START_Y, dir)
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            temp.set_colorkey((255, 255, 255))
            i=[]
            i.append(temp.subsurface(0,0,90,90))
            i.append(temp.subsurface(90,0,90,90))
            i.append(temp.subsurface(180,0,90,90))
            self.images.append(i)

    def moove(self):
        if self.mooving[RIGHT] == 1:
            self.x += self.speed
            self.direction = RIGHT
        if self.mooving[DOWN]:
            self.y += self.speed
            self.direction = DOWN
        if self.mooving[LEFT]:
            self.x -= self.speed
            self.direction = LEFT
        if self.mooving[UP]:
            self.y -= self.speed
            self.direction = UP

        if self.x <= 0: self.x = 0
        if self.y <= 0: self.y = 0
        if self.x >= SCREEN_WIDTH-35: self.x = SCREEN_WIDTH-35
        if self.y >= SCREEN_HEIGHT-75: self.y = SCREEN_HEIGHT-75

    def __str__(self):
        Mob.__str__(self)

    def tick(self):
        if self.mp <= orge_MP: self.mp += mp_reg_ogr
        if self.hp <= orge_HP: self.hp += HP_REG
        if pygame.time.get_ticks() > self.spell_casted + TIME2SHOT:
            self.state = ALIVE

