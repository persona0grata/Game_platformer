import pygame as pg 
import numpy as np
import os

from  Sprite import Sprite


class Player(Sprite):
    
    def __init__(self, image_path, startx, starty):
        super().__init__(os.path.join(image_path, 'playerGrey_stand.png'), startx, starty)
        self.stand_image = self.image
        self.jump_image = pg.image.load(os.path.join(image_path, 'playerGrey_up3.png'))
        self.fall_image = pg.image.load(os.path.join(image_path, 'playerGrey_fall.png'))
        
        self.walk_cycle = [pg.image.load(os.path.join(image_path, f"playerGrey_walk{i}.png")) for i in range(1,6)]
        self.animation_index = 0
        self.facing_left = False
        
        self.speed = 10
        self.jumpspeed = 40
        self.vertical_speed = 3
        self.gravity = 1
        
        
        
    def walk_animation(self):
        self.image = self.walk_cycle[self.animation_index]
        if self.facing_left:
            self.image = pg.transform.flip(self.image, True, False)

        if self.animation_index < len(self.walk_cycle)-1:
            self.animation_index += 1
        else:
            self.animation_index = 0
            
            
            
    def jump_animation(self):
        self.image = self.jump_image
        if self.facing_left:
            self.image = pg.transform.flip(self.image, True, False)
    def fall_animation(self):
        self.image = self.fall_image
        if self.facing_left:
            self.image = pg.transform.flip(self.image, True, False)
    
    
    
    def update(self, entities):
        
        horizontal_speed = 0
        onground = self.check_collision(1, 0, entities)
        
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.facing_left = True
            self.walk_animation()
            horizontal_speed = -self.speed
        elif key[pg.K_RIGHT]:
            self.facing_left = False
            self.walk_animation()
            horizontal_speed = self.speed
        else:
            self.image = self.stand_image
            
        if key[pg.K_UP] and onground:
           self.vertical_speed = -self.jumpspeed
           
        if self.vertical_speed < 10 and not onground: # 9.8 rounded up
            self.jump_animation()
            self.vertical_speed += self.gravity
            
        if self.vertical_speed > 0 and onground:
            self.vertical_speed = 0
           
        self.move(horizontal_speed, self.vertical_speed, entities)
            
            
            
    def move(self, x, y, entities):
        dx = x
        dy = y
        
        
        while self.check_collision(0, dy, entities):
            dy -= np.sign(dy)
            
        while self.check_collision(dx, dy, entities):
            dx -= np.sign(dx)
            
        
        
        self.rect.move_ip([dx, dy])
        
        
        
    def check_collision(self, x, y, entities):
        self.rect.move_ip([x,y])
        collide = pg.sprite.spritecollideany(self, entities)
        self.rect.move_ip([-x,-y])
        return collide
         