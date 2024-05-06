from pathlib import Path

import pygame


CURRENT_FOLDER = Path(__file__).parent

# print(f'{__file__ = }, {Path().absolute() = }')
# print(f'{Path(__file__).parent = }')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.surface.Surface((30, 30))
        # self.image.fill("red")
        self.image = pygame.image.load(CURRENT_FOLDER / 'logo.png')  # .convert()
        self.rect = self.image.get_rect()
        self.y_speed = 0
        self.x_speed = 0

        self.scene = pygame.display.get_surface().get_rect()
        print(f'area bottom = {self.scene.bottom}')
        self.rect.centerx = self.scene.centerx
        self.rect.y = 100

        self.scene = pygame.display.get_surface().get_rect()
        print(f'area right = {self.scene.right}')
        self.rect.centerx = self.scene.centerx
        self.rect.x = 100

        self.scene = pygame.display.get_surface().get_rect()
        print(f'area left = {self.scene.left}')
        self.rect.centerx = self.scene.centerx


    def update(self):
        self.y_speed += 1
        self.x_speed += 1
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed
        if self.rect.bottom > self.scene.bottom:
            self.y_speed *= -1
            self.rect.y += self.y_speed
        elif self.rect.right > self.scene.right:
            self.x_speed *= -1
            self.rect.x += self.x_speed
        elif self.rect.left < self.scene.left:
            self.x_speed *= 1
            self.rect.x -= self.x_speed
        elif self.y_speed < 0:
            self.y_speed += 0.2
    def boost(self):
        self.y_speed -= 1
        self.x_speed -= 8
