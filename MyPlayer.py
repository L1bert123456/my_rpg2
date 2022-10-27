import pygame
#import time
from constants import *
import Projective
from pygame.sprite import Sprite, collide_rect

class Player(Sprite):
    def __init__(self, name: str):
        self.image = pygame.image.load('data/hpframe.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.state = ALIVE
        self.x = START_X
        self.y = START_Y
        self.direction = RIGHT
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.spell_casted = 0
        self.mooving = [0, 0, 0, 0]
        #self.image_pack = ['data/archerr.png','data/archerd.png'        , 'data/archerl.png', 'data/archeru.png']
        # self.images = []
        # for image in self.image_pack:
        #     temp = pygame.image.load(image).convert_alpha()
        #     i=[]
        #     i.append(temp.subsurface(0,0,64,64))
        #     i.append(temp.subsurface(64, 0, 64, 64))
        #     i.append(temp.subsurface(128, 0, 64, 64))
        #     self.images.append(i)

        self.hpframe = pygame.image.load('data/hpframe.png').convert_alpha()
        self.hpframe5 = pygame.image.load('data/hpframe5.png').convert_alpha()
        self.mpframe = pygame.image.load('data/mpframe.png').convert_alpha()
        self.mpframe5 = pygame.image.load('data/mpframe5.png').convert_alpha()

        temp = pygame.image.load('data/wizard.png').convert_alpha()
        i = []
        i.append(temp.subsurface(240, 186, 60, 88)) # право
        i.append(temp.subsurface(0, 0, 60, 88))  # низ
        i.append(temp.subsurface(0, 363, 59, 87))  # лево
        i.append(temp.subsurface(300, 0, 60, 88))  # верх
        i.append(temp.subsurface(60, 0, 60, 88))  # умер
        self.image = i





    def moove(self):
        if self.mooving[RIGHT] == 1:
            self.x+=PLAYER_SPEED
            self.direction = RIGHT
        if self.mooving[DOWN]:
            self.y+=PLAYER_SPEED
            self.direction = DOWN
        if self.mooving[LEFT]:
            self.x-=PLAYER_SPEED
            self.direction = LEFT
        if self.mooving[UP]:
            self.y-=PLAYER_SPEED
            self.direction = UP

        if self.x <= 0: self.x = 0
        if self.y <= 0: self.y = 0
        if self.x >= SCREEN_WIDTH-35: self.x = SCREEN_WIDTH-35
        if self.y >= SCREEN_HEIGHT-75: self.y = SCREEN_HEIGHT-75


    def render(self, screen):
       # screen.blit(self.images[self.direction][self.state], (self.x, self.y))
       screen.blit(self.image[self.direction], (self.x, self.y))
    def render_ui(self, screen):
        screen.blit(self.hpframe, (self.x-4, self.y-5))
        m = 1
        z = self.hp // 5
        while m<= z:
            screen.blit(self.hpframe5, (self.x-3+m*3, self.y-4))
            m+=1

        screen.blit(self.mpframe, (self.x - 4, self.y - 1))
        m = 1
        z = self.mp // 5
        while m <= z:
            screen.blit(self.mpframe5, (self.x - 3 + m * 3, self.y) )
            m += 1

    def tick(self):
        if self.mp <= MAX_MP: self.mp+=MP_REG
        if self.hp <= MAX_HP: self.hp+=HP_REG
        if pygame.time.get_ticks() > self.spell_casted +TIME2SHOT:
            self.state = ALIVE





