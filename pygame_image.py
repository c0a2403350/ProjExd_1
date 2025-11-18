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
    bg_img2 = pg.transform.scale(bg_img2, (1600, 900))    
    bg_img2 = pg.transform.flip(bg_img2, True, False)

    
    bird_img = pg.image.load("fig/3.png")
    bird_img = pg.transform.flip(bird_img, True, False)
    bird_img_rec = bird_img.get_rect()
    bird_img_rec.center = 300, 200
    
    tmr = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            
        # key_lst = pg.key.get_pressed()
        # if key_lst[]
        # bird_img_rec.move_ip
        
        screen.blit(bg_img, [-x, 0])
        screen.blit(bird_img, bird_img_rec)

        pg.display.update()
        tmr += 1
        x = tmr
        
        clock.tick(200)
        
        screen.blit(bg_img2, [1600 - x, 0])
        screen.blit(bg_img, [3200 - x, 0])
        
        if x > 3200:
            tmr = 0

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()