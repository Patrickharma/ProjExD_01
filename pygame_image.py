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
    bird_img = pg.transform.rotozoom(bird_img, 10, 1.0)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
        screen.blit(bird_img, bird_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()