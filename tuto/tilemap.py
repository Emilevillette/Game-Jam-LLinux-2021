import pygame as pg
from settings import *
class Map:
    def __init__(self, filename):
        self.data =[]
        with open(filename, 'rt') as f: #rt : read
            for line in f:
                self.data.append(line.strip())
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height) # calcul du shift de tt les éléments
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2) # déplacement dans le sens inverse du joueur et il reste au centre
        y = -target.rect.y + int(HEIGHT / 2)

        
        # limite scrolling to map size
        x = min(0, x) # left 
        y = min(0, y) # top
        x = max(-(self.width - WIDTH), x) # right
        y = max(-(self.height - HEIGHT), y) # bottom
        self.camera = pg.Rect(x, y, self.width, self.height)