
#Rectangles using OOP concept
#import and initialize pygame 
import pygame
pygame.init()

#set dimensions of the screen
screen=pygame.display.set_mode((1200,800))


#Colors
#screen fil
running=True
#creating a Rectangle class
class drawrec():
    #initializd/constucter
    def __init__(self,dimensens,colour):
        print("nathan")
        self.rec_surface=screen
        self.rec_colour=colour
        self.rec_dimen=dimensens
        #function to draw rectagal
    def rec(self):
        self.nathan=pygame.draw.rect(self.rec_surface,self.rec_colour,self.rec_dimen)
#creating Instances 
''' 
redrec=drawrec("red",(100,100,100,75)) 
redrec.rec()

yellowrec=drawrec("yellow",(200,200,150,100))
yellowrec.rec()

bluerec=drawrec("blue",(600,600,100,75)) 
bluerec.rec()

pinkrec=drawrec("pink",(500,300,125,100))
pinkrec.rec()
'''
grayrec=drawrec((700,400,100,100),"gray")
grayrec.rec()
#accessing methods 
#Display update to reflect the things on screeen

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False