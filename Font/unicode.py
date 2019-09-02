# -*- coding: utf-8 -*-
from pygame import *
init()
one_moment = "等一下"

screen = display.set_mode((0,0))
fnt = font.Font("cyberbit.ttf",60)
ding = font.Font("harry_potter_dingbat.ttf",80)
txtPic = fnt.render(one_moment,True,(255,255,255))
screen.blit(txtPic,(100,100))
picNum=64
running = True
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            picNum += 1
            txtPic = ding.render(chr(picNum),True,(255,255,255))
            screen.blit(txtPic,evnt.pos)

    display.flip()

quit()
