import pygame 
pygame.init()#initialize

#title
pygame.display.set_caption('Events in pygame')

#width & height 
screen=pygame.display.set_mode((600,600))

screen.fill((255,255,255))
blue=(0,0,255)
pygame.display.update()

class Circle ():
    def __init__(self,color,pos,raduis,width):
        self.surface=screen
        self.circle_color=color
        self.circle_raduis=raduis
        self.circle_width=width
        self.circle_pos=pos

    def draw(self):
        self.draw_circle=pygame.draw.circle(self.surface,self.circle_color,self.circle_pos,self.circle_raduis,self.circle_width)

    def grow (self,r):
      self.raduis=self.raduis+r
      self.draw_circle=pygame.draw.circle(self.surface,self.circle_color,self.circle_pos,self.circle_raduis,self.circle_width)

    #object creation
cir= Circle(blue,(300,300),25,0)

while 1:                              

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          screen.fill((255,255,255))
          cir.draw()
          pygame.display.update()

      elif event.type== pygame.MOUSEBUTTONUP:
        screen.fill((255,255,255))
        cir.grow(20)
        pygame.display.update()