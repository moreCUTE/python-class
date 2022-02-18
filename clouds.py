#pygame is a bunch of pre-written python code that makes coding games easier
import pygame #handles graphics, sound, game timings, keyboard input, etc
pygame.init()

#creates game screen and caption
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Silly Shapes")

class cloud:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen, (255,255,255), (self.xpos, self.ypos), 65)
        pygame.draw.circle(screen, (255,255,255), (self.xpos-45, self.ypos+30), 50)
        pygame.draw.circle(screen, (255,255,255), (self.xpos+45, self.ypos+30), 50)
        pygame.draw.arc(screen,(255,0,0), (self.xpos-75, self.ypos-180, 160, 190), 7*3.14/4, 5*3.14/4, 7)
        pygame.draw.arc(screen,(255,255,0), (self.xpos-65, self.ypos-160, 140, 150), 7*3.14/4, 5*3.14/4, 7)
        pygame.draw.arc(screen,(0,255,0), (self.xpos-55, self.ypos-140, 120, 130), 7*3.14/4, 5*3.14/4, 7)
        pygame.draw.arc(screen,(0,0,255), (self.xpos-45, self.ypos-120, 100, 110), 7*3.14/4, 5*3.14/4, 7)

cloud1 = cloud(500,500)
cloud1.draw()
pygame.display.flip() #update 
