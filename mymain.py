import pygame
import time
import random as rnd
from pygame.locals import *
from constants import *
from MyPlayer import Player
from Projective import *
from MyEnemy import *
class Main():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player('Grut')
        self.projective = []
        self.background = pygame.image.load('data/background.jpg')
        self.temp = pygame.image.load('data/ogre.png')
        self.otg = self.temp.subsurface(0, 0, 71,71)
        self.running = True
        self.count = 0
        self.mobs = []


        self.ogre_group = pygame.sprite.Group()
        ogre1 = Orge(100, 100, LEFT)
        self.ogre_group.add(ogre1)

        self.main_loop()
    def add_orge(self, x, y):
        ogre1 = Orge(x, y, LEFT)
        self.mobs.append(ogre1)
        self.ogre_group.add(ogre1)

    def hits(self):
        hits = pygame.sprite.spritecollide(self.player, self.ogre_group, False)
        for i in hits:
            self.player.hp -= 40
            i.kill()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == USEREVENT+1:
                self.player.tick()
            elif event.type == USEREVENT+3:
                for i in self.mobs:
                    i.tick()
                    i.moove()
            elif event.type == USEREVENT+4:
                self.add_orge(rnd.randint(0,500), rnd.randint(0,500))
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    self.player.mooving = [1,0,0,0]
                if event.key == K_DOWN or event.key == K_s:
                     self.player.mooving = [0,1,0,0]
                if event.key == K_LEFT or event.key == K_a:
                       self.player.mooving = [0,0,1,0]
                if event.key == K_UP or event.key == K_w:
                    self.player.mooving = [0,0,0,1]

                if event.key == K_SPACE:
                    self.player.hp-=5
                    if self.player.state != DEAD:
                        self.player.state = DEAD
                        self.player.direction = DIE
                    else:
                        self.player.state = ALIVE
                        self.player.direction = UP

                if event.key == K_z:
                    if self.player.mp >= SKILL1_COST and self.player.state != SHOOT and self.player.state != DEAD:
                        self.player.mp -= SKILL1_COST
                        self.player.state = SHOOT
                        self.player.spell_casted = pygame.time.get_ticks()


                        if self.player.direction == RIGHT:
                            self.projective.append(Arrow(self.player.x+12, self.player.y, self.player.direction))
                        elif self.player.direction == DOWN:
                            self.projective.append(Arrow(self.player.x, self.player.y+12, self.player.direction))
                        elif self.player.direction == LEFT:
                            self.projective.append(Arrow(self.player.x-12, self.player.y, self.player.direction))
                        else:
                            self.projective.append(Arrow(self.player.x, self.player.y-12, self.player.direction))

                if event.key == K_x:
                    if self.player.mp >= SKILL2_COST and self.player.state != SHOOT and self.player.state != DEAD:
                        self.player.mp -= SKILL2_COST
                        self.player.state = SHOOT
                        self.player.spell_casted = pygame.time.get_ticks()

                        self.projective.append(Firearrow(self.player.x , self.player.y, self.player.direction))
                      #  if self.player.direction == RIGHT:
                     #       self.projective.append(Firearrow(self.player.x+12, self.player.y, self.player.direction))
                      #  elif self.player.direction == DOWN:
                      #      self.projective.append(Firearrow(self.player.x, self.player.y+12, self.player.direction))
                      #  elif self.player.direction == LEFT:
                      #      self.projective.append(Firearrow(self.player.x-12, self.player.y, self.player.direction))
                      #  else:
                      #      self.projective.append(Firearrow(self.player.x, self.player.y-12, self.player.direction))
                if event.key == K_c:
                    if self.player.mp >= SKILL3_COST and self.player.state != SHOOT and self.player.state != DEAD:
                        self.player.mp -= SKILL3_COST
                        self.player.state = SHOOT
                        self.player.spell_casted = pygame.time.get_ticks()

                        self.projective.append(Fireball(self.player.x, self.player.y, self.player.direction))




            elif event.type == KEYUP:
                if event.key == K_RIGHT  or event.key == K_d:
                    self.player.mooving[RIGHT] = 0
                if event.key == K_DOWN or event.key == K_s:
                    self.player.mooving[DOWN] = 0
                if event.key == K_LEFT or event.key == K_a:
                    self.player.mooving[LEFT] = 0
                if event.key == K_UP or event.key == K_w:
                    self.player.mooving[UP] = 0


    def render(self):

        self.screen.blit(self.background,(0,0))
        self.player.render(screen)
        self.player.render_ui(screen)
        for i in self.mobs:
            i.render(screen)
        for i in self.projective:
            i.render(screen)
        self.ogre_group.draw(screen)
        pygame.display.flip()

   # def clear_garbage(self):
   #     for i in self.projective:
    #        if i.x > SCREEN_WIDTH or i.x < -32 or

    def main_loop(self):
        while self.running == True:
            if self.player.state != DEAD:
                self.player.moove()
            for i in self.projective:
                i.moove()
            self.render()
            self.hits()
            self.handle_events()
            #self.pygame.time.Clock.tick(33)
            clock.tick(50)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.time.set_timer(USEREVENT+1, 100)
pygame.time.set_timer(USEREVENT+2, 1000)
pygame.time.set_timer(USEREVENT+3, 100) # передвижение Огров
pygame.time.set_timer(USEREVENT+4, 300) # появление Огров
game = Main(screen)