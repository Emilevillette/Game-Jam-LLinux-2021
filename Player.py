import pygame
import random
import math

class Player:

    def __init__(self,img, x, y, speed, size=64):
        self.img = img
        self.X = x
        self.Y = y
        self.speed = speed
        self.moveX = 0
        self.moveY = 0
        self.size = size

    def move(self,x,y):
        self.moveX += x*self.speed
        self.moveY += y*self.speed

    def stop(self):
        self.moveX = 0
        self.moveY = 0

    def update(self):
        self.X += self.moveX
        self.Y += self.moveY

    def cancel(self):
        self.X -= self.moveX
        self.Y -= self.moveY

    def isCollision(self,x,y):
        distance = math.sqrt(math.pow(self.X-x,2) + math.pow(self.Y-y,2))
        if (distance < self.size):
            self.cancel()