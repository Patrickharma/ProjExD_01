import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bird_img = pg.image.load("fig/3.png")
    bird_rct = bird_img.get_rect()
    bird_rct.center = 300, 200
    bird_img = pg.transform.flip(bird_img, True, False)
    bird_imgs = [bird_img, pg.transform.rotozoom(bird_img, 10, 1.0)]
    pg.transform.rotozoom(bird_img, 1, 1.0),pg.transform.rotozoom(bird_img, 2, 1.0),pg.transform.rotozoom(bird_img, 3, 1.0),pg.transform.rotozoom(bird_img, 4, 1.0),pg.transform.rotozoom(bird_img, 5, 1.0),pg.transform.rotozoom(bird_img, 6, 1.0),pg.transform.rotozoom(bird_img, 7, 1.0),pg.transform.rotozoom(bird_img, 8, 1.0),pg.transform.rotozoom(bird_img, 9, 1.0)


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img, True, False), [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(bird_imgs[tmr%100//50], bird_rct)
        
        pg.display.update()
        tmr += 1        
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()