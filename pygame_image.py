import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img = pg.transform.scale(bg_img, (1600, 900))

    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img = pg.transform.scale(bg_img2, (1600, 900))
    
    bird_img = pg.image.load("fig/3.png")
    bird_img = pg.transform.flip(bird_img, True, False)
    
    tmr = 0
    x, y = 0, 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        screen.blit(bg_img, [-x, y])
        screen.blit(bird_img, [300, 200])

        pg.display.update()
        tmr += 1        
        clock.tick(200)
        clock.tick(600)
        
        x = tmr
        # screen.blit(bg_img2, [800 - x, 0])

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()