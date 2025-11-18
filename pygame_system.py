import os
import sys
import pygame as pg
from pygame.locals import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はじめてのPygame")

    w, h = 800, 600
    screen = pg.display.set_mode((w, h))
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)

    enn = pg.Surface((20, 20))
    r = 10
    pg.draw.circle(enn, (255, 0, 0), (10, 10), r)
    
    enn.set_colorkey((0, 0, 0))

    tmr = 0
    x = 10
    y = 10

    while True:
        pressed_key = pg.key.get_pressed()
        if pressed_key[K_ESCAPE]: pg.quit()
        if pressed_key[K_RIGHT]: x += 5
        if pressed_key[K_LEFT]: x -= 5
        if pressed_key[K_UP]: y -= 5
        if pressed_key[K_DOWN]: y += 5
        
        if y > h + r:
            y = 0
        elif y < 0 - r:
            y = h + r
        
        if x > w + r:
            x = 0
        elif x < 0 - r:
            x = w + r

        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [300, 200])
        screen.blit(enn, [x, y])
        pg.display.update()
        tmr += 1        
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()