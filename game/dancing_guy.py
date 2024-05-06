from pathlib import Path

import pygame

CURRENT_FOLDER = Path(__file__).parent


class Dancer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(CURRENT_FOLDER / 'dancing_guy.png').convert_alpha()
        self.stop_image = pygame.image.load(CURRENT_FOLDER / 'where_is_music.png')
        self.rect = self.image.get_rect()
        self.x_speed = 7

        self.scene = pygame.display.get_surface().get_rect()
        self.rect.centerx = self.scene.centerx
        self.rect.y = 100

        self.scene = pygame.display.get_surface().get_rect()
        self.rect.centerx = self.scene.centerx
        self.rect.x = 100

        self.scene = pygame.display.get_surface().get_rect()
        self.rect.centerx = self.scene.centerx

    def update(self):
        if pygame.mixer.music.get_busy():
            self.rect.x += self.x_speed
            if self.rect.right > self.scene.right or self.rect.left < self.scene.left:
                self.image = pygame.transform.flip(self.image, True, False)
                self.x_speed *= -1







