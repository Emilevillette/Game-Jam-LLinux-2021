import pygame as pg
from settings import *
import sys

vec = pg.math.Vector2  # usefull for lots of thing


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.is_animating = False
        self.sprites = []
        self.sprites.append(pg.image.load("Sprite-00021.png"))
        self.sprites.append(pg.image.load("Sprite-00022.png"))
        self.sprites.append(pg.image.load("Sprite-00023.png"))
        self.sprites.append(pg.image.load("Sprite-00024.png"))
        self.sprites.append(pg.image.load("Sprite-00025.png"))
        self.sprites.append(pg.image.load("Sprite-00026.png"))
        self.sprites.append(pg.image.load("Sprite-00027.png"))
        self.sprites.append(pg.image.load("Sprite-00028.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()

    def animate(self):
        self.is_animating = True

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_q]:
            self.vel.x = - PLAYER_SPEED
            self.animate()
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
            self.animate()
        if keys[pg.K_UP] or keys[pg.K_z]:
            self.vel.y = - PLAYER_SPEED
            self.animate()
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
            self.animate()
        if self.vel.x != 0 and self.vel.y != 0:
            self.vel *= 0.7071  # si diag : divisé par sqrt(2) pour ne pas DRIFTEEEEEER (trop vite quoi)

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:  # collision par la droite
                    self.pos.x = hits[0].rect.left - self.rect.width  # place contre le mur
                if self.vel.x < 0:  # collision par la gauche
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:  # collision par la droite
                    self.pos.y = hits[0].rect.top - self.rect.height  # place contre le mur
                if self.vel.y < 0:  # collision par la gauche
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y

    def update(self):
        self.get_keys()
        self.pos += self.vel * self.game.dt  # dt : frame d'avant, dans "run"
        self.rect.x = self.pos.x
        self.collide_with_walls('x')
        self.rect.y = self.pos.y
        self.collide_with_walls('y')
        if self.is_animating == True:
            self.current_sprite += 1

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[self.current_sprite]


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.x = x
        self.y = y

        self.rect.x = x
        self.rect.y = y

# class Wall(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites, game.walls
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image.fill(GREEN)
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE
