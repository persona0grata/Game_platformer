import pygame as pg 
import os
import csv

from  Sprite import Sprite
from Player import Player

from Platform import Platform


csv_file_path = 'Map.csv'

WIDTH = 1920
HEIGHT = 1080
BACKGROUND = (0, 0, 0)


with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    LEVEL_MAP = []
    for row in csv_reader:
        LEVEL_MAP.append(row[0])
        
# LEVEL_MAP = ["##############################",
#              "|                            |",
#              "|   =                        |",
#              "|                            |",
#              "|                   =        |",
#              "|  _------_                  |",
#              "|                            |",
#              "|                            |",
#              "|        _----_        =     |",
#              "|                            |",
#              "|            |               |",
#              "|                            |",
#              "|                            |",
#              "|  =                         |",
#              "|       _--_                 |",
#              "|                            |",
#              "|                     _--_   |",
#              "|                            |",
#              "##############################"]

def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, "img")
    Player_folder = os.path.join(img_folder, "Player")
    Tiles_folder = os.path.join(img_folder, "Tiles")
    Background_folder = os.path.join(img_folder, "Backgrounds")

    
    player = Player(Player_folder, 100, 950)
    platforms = pg.sprite.Group()
    # for pf in range(0,2000,64):
    #     platforms.add(Platform(Tiles_folder, pf,1000))
    step_h = 32
    step_v = 0
    count = 0
    for vertical in LEVEL_MAP:
        for horizontal in vertical:
            if (horizontal == "-"): 
                platforms.add(Platform(Tiles_folder, "tileGreen_27.png", step_h, step_v))
            if (horizontal == "#"): 
                platforms.add(Platform(Tiles_folder, "tileGreen_05.png", step_h, step_v))
            
            if (horizontal == "|"): 
                platforms.add(Platform(Tiles_folder, "tileGreen_17.png", step_h, step_v))
            if (horizontal == "_"):
                if (count != 1):
                    platforms.add(Platform(Tiles_folder, "tileGreen_26.png", step_h, step_v))
                    count += 1
                else: 
                    platforms.add(Platform(Tiles_folder, "tileGreen_01.png", step_h, step_v))
                    count = 0
            if (horizontal == "="): 
                platforms.add(Platform(Tiles_folder, "tileGreen_02.png", step_h, step_v))
            
            step_h += 64
        step_h = 32
        step_v += 60


    Running = True
    while Running:
        pg.event.pump()
        player.update(platforms)
        
        for event in pg.event.get():
        #Event for closing window
            if event.type == pg.QUIT:
                Running = False
            
            
        # Draw loop
        screen.blit(pg.transform.scale(pg.image.load(os.path.join(Background_folder, "Forest.png")).convert(), (1920, 1080)), (0, 0))
        player.draw(screen)
        platforms.draw(screen)
        pg.display.flip()

        clock.tick(30)

if __name__ == "__main__":
    main()