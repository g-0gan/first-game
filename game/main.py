import asyncio
import sys
from pathlib import Path

import pygame

from music import MusicPlayer
from dancing_guy import Dancer

CURRENT_FOLDER = Path(__file__).parent

SONGS = ['song_for_game#1.mp3', 'song_for_game#2.mp3', 'song_for_game#3.mp3']
FPS = 45
SCREEN_SIZE = (1280, 720)

music_player = MusicPlayer(SONGS)


async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()

    background = pygame.image.load(CURRENT_FOLDER / 'background.jpg')
    screen.blit(background, (0, 0))
    pygame.display.update()

    dancer = Dancer()  # Sprite: Surface, Rectangle
    all_sprites = pygame.sprite.RenderPlain(dancer)

    if pygame.font:
        font = pygame.font.Font(None, 32)
        text = font.render("Warning! This guy likes to dance, dont turn the music off!"
                           " To change music use A(<) and D(>), advice: DONT USE SPACE!", True, (220, 235, 232))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    pygame.mixer.init()
    music_player.play_music()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    music_player.previous_song()
                if event.key == pygame.K_d:
                    music_player.next_song()
                if event.key == pygame.K_SPACE:
                    if pygame.mixer.music.get_busy():
                        music_player.stop_music()
                    else:
                        music_player.play_music()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        all_sprites.update()

        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)
        await asyncio.sleep(0)

if __name__ == '__main__':
    asyncio.run(main())
