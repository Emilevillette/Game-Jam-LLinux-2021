import pygame as pg
from settings import *
from os import path
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
        game_folder = path.dirname(__file__)
        sprites_folder = path.join(game_folder, 'ressources/images')
        self.spritesl = []
        self.spritesl.append(pg.image.load(path.join(sprites_folder, "Spritegauche/Sprite-0002gauche1.png")))
        self.spritesl.append(pg.image.load(path.join(sprites_folder, "Spritegauche/Sprite-0002gauche2.png")))
        self.spritesl.append(pg.image.load(path.join(sprites_folder, "Spritegauche/Sprite-0002gauche3.png")))
        self.spritesl.append(pg.image.load(path.join(sprites_folder, "Spritegauche/Sprite-0002gauche4.png")))
        self.spritesl.append(pg.image.load(path.join(sprites_folder, "Spritegauche/Sprite-0002gauche5.png")))
        self.spritesl.append(pg.image.load(path.join(sprites_folder, "Spritegauche/Sprite-0002gauche6.png")))
        self.spritesl.append(pg.image.load(path.join(sprites_folder, "Spritegauche/Sprite-0002gauche7.png")))
        self.spritesl.append(pg.image.load(path.join(sprites_folder, "Spritegauche/Sprite-0002gauche8.png")))
        self.spritesr = []
        self.spritesr.append(pg.image.load(path.join(sprites_folder, "SpriteDroite/Sprite-00021.png")))
        self.spritesr.append(pg.image.load(path.join(sprites_folder, "SpriteDroite/Sprite-00022.png")))
        self.spritesr.append(pg.image.load(path.join(sprites_folder, "SpriteDroite/Sprite-00023.png")))
        self.spritesr.append(pg.image.load(path.join(sprites_folder, "SpriteDroite/Sprite-00024.png")))
        self.spritesr.append(pg.image.load(path.join(sprites_folder, "SpriteDroite/Sprite-00025.png")))
        self.spritesr.append(pg.image.load(path.join(sprites_folder, "SpriteDroite/Sprite-00026.png")))
        self.spritesr.append(pg.image.load(path.join(sprites_folder, "SpriteDroite/Sprite-00027.png")))
        self.spritesr.append(pg.image.load(path.join(sprites_folder, "SpriteDroite/Sprite-00028.png")))
        self.spritesu = []
        self.spritesu.append(pg.image.load(path.join(sprites_folder, "SpriteHaut/Sprite-0002haut1.png")))
        self.spritesu.append(pg.image.load(path.join(sprites_folder, "SpriteHaut/Sprite-0002haut2.png")))
        self.spritesu.append(pg.image.load(path.join(sprites_folder, "SpriteHaut/Sprite-0002haut3.png")))
        self.spritesu.append(pg.image.load(path.join(sprites_folder, "SpriteHaut/Sprite-0002haut4.png")))
        self.spritesu.append(pg.image.load(path.join(sprites_folder, "SpriteHaut/Sprite-0002haut5.png")))
        self.spritesu.append(pg.image.load(path.join(sprites_folder, "SpriteHaut/Sprite-0002haut6.png")))
        self.spritesu.append(pg.image.load(path.join(sprites_folder, "SpriteHaut/Sprite-0002haut7.png")))
        self.spritesu.append(pg.image.load(path.join(sprites_folder, "SpriteHaut/Sprite-0002haut8.png")))
        self.spritesd = []
        self.spritesd.append(pg.image.load(path.join(sprites_folder, "Spritebas/Sprite-0002bas1.png")))
        self.spritesd.append(pg.image.load(path.join(sprites_folder, "Spritebas/Sprite-0002bas2.png")))
        self.spritesd.append(pg.image.load(path.join(sprites_folder, "Spritebas/Sprite-0002bas3.png")))
        self.spritesd.append(pg.image.load(path.join(sprites_folder, "Spritebas/Sprite-0002bas4.png")))
        self.spritesd.append(pg.image.load(path.join(sprites_folder, "Spritebas/Sprite-0002bas5.png")))
        self.spritesd.append(pg.image.load(path.join(sprites_folder, "Spritebas/Sprite-0002bas6.png")))
        self.spritesd.append(pg.image.load(path.join(sprites_folder, "Spritebas/Sprite-0002bas7.png")))
        self.spritesd.append(pg.image.load(path.join(sprites_folder, "Spritebas/Sprite-0002bas8.png")))
        self.current_sprite = 0
        self.direction = 'right'
        self.image = self.spritesl[self.current_sprite]
        self.rect = self.image.get_rect()

    def animate(self):
        self.is_animating = True

    def get_keys(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_q]:
            self.vel.x = - PLAYER_SPEED
            self.animate()
            self.direction = 'left'
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vel.x = PLAYER_SPEED
            self.animate()
            self.direction = 'right'
        if keys[pg.K_UP] or keys[pg.K_z]:
            self.vel.y = - PLAYER_SPEED
            self.animate()
            self.direction = 'up'
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vel.y = PLAYER_SPEED
            self.animate()
            self.direction = 'down'
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

            if self.current_sprite >= len(self.spritesd):
                self.current_sprite = 0
                self.is_animating = False

            if self.direction == 'left':
                self.image = self.spritesl[self.current_sprite]
            elif self.direction == 'down':
                self.image = self.spritesd[self.current_sprite]
            elif self.direction == 'up':
                self.image = self.spritesu[self.current_sprite]
            else:
                self.image = self.spritesr[self.current_sprite]
            # self.image = pg.transform.scale(self.image, PLAYER_RADIUS)


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