import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#練習1
    bg_img2 = pg.transform.flip(bg_img, True, False)
    koukaton_img = pg.image.load("fig/3.png")#練習3
    koukaton_rct = koukaton_img.get_rect()
    koukaton_rct.center = 300, 200
    koukaton_img = pg.transform.flip(koukaton_img, True, False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200 #練習5

        key_lst = pg.key.get_pressed()
        #print(key_lst)#確認用print
        koukaton_rct.move_ip(-1, 0)
        if key_lst[pg.K_UP]:
            koukaton_rct.move_ip(0, -1)
        if key_lst[pg.K_DOWN]:
            koukaton_rct.move_ip(0, +1)
        if key_lst[pg.K_LEFT]:  # 左矢印キーが押されていたら
            koukaton_rct.move_ip(-1, 0)
        if key_lst[pg.K_RIGHT]:  # 右矢印キーが押されていたら
            koukaton_rct.move_ip(+1, 0)
        
        screen.blit(bg_img, [-x, 0])#練習2
        screen.blit(bg_img2, [-x+1600,0])#練習7
        screen.blit(bg_img, [-x+3200, 0])#練習9
        screen.blit(koukaton_img, koukaton_rct)#練習4,練習10
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習6


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()