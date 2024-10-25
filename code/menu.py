import pygame
import sys
from settings import *
from sprites import *
from groups import *

class Menu:
    def __init__(self, main):
        pygame.init()
        self.clock=pygame.time.Clock()  #fps

        # self.mouse = pygame.image.load('D:\\Gameproject\\images\\menu\\mouse1.png')
        self.gamev1 = pygame.image.load('D:\\Gameproject\\images\\menu\\v1.png')
        self.x_title, self.y_title = self.gamev1.get_size()
        self.gamev1.set_colorkey((255, 255, 255))
        self.pos_xt = WINDOW_WIDTH // 2 - self.x_title // 2

        self.start = pygame.image.load('D:\\Gameproject\\images\\menu\\start.png')
        self.x_start, self.y_start = self.start.get_size()
        self.start = pygame.transform.scale(self.start, (self.x_start/1.2,self.y_start/1.2))
        self.start.set_colorkey((255, 255, 255))
        self.pos_xs = WINDOW_WIDTH // 2 - self.x_start // 2
        self.start_rect = pygame.Rect(self.pos_xs,WINDOW_HEIGHT//2 - 50, self.start.get_width(), self.start.get_height())


        self.quit = pygame.image.load('D:\\Gameproject\\images\\menu\\quit.png')
        self.x_quit, self.y_quit = self.quit.get_size()
        self.quit = pygame.transform.scale(self.quit, (self.x_quit/1.2,self.y_quit/1.2))
        self.quit.set_colorkey((255, 255, 255))
        self.pos_xq = WINDOW_WIDTH // 2 - self.x_quit // 2
        self.quit_rect = pygame.Rect(self.pos_xq,WINDOW_HEIGHT//2 +50, self.quit.get_width(), self.quit.get_height())

        self.map1 = pygame.image.load('D:\\Gameproject\\images\\menu\\map1.png')
        self.x_map1, self.y_map1 = self.map1.get_size()
        self.map1 = pygame.transform.scale(self.map1, (self.x_map1/1,self.y_map1/1))
        self.map1.set_colorkey((255, 255, 255))
        self.pos_xm1 = WINDOW_WIDTH // 2 - self.x_map1 // 2
        self.map1_rect = pygame.Rect(self.pos_xm1,WINDOW_HEIGHT//2 -150, self.map1.get_width(), self.map1.get_height())

        self.map2 = pygame.image.load('D:\\Gameproject\\images\\menu\\map2.png')
        self.x_map2, self.y_map2 = self.map2.get_size()
        self.map2 = pygame.transform.scale(self.map2, (self.x_map2/1,self.y_map2/1))
        self.map2.set_colorkey((255, 255, 255))
        self.pos_xm2 = WINDOW_WIDTH // 2 - self.x_map2 // 2
        self.map2_rect = pygame.Rect(self.pos_xm2,WINDOW_HEIGHT//2 -50, self.map2.get_width(), self.map2.get_height())

        self.back = pygame.image.load('D:\\Gameproject\\images\\menu\\back.png')
        self.x_back, self.y_back = self.back.get_size()
        self.back = pygame.transform.scale(self.back, (self.x_back/1,self.y_back/1))
        self.back.set_colorkey((255, 255, 255))
        self.pos_xback = WINDOW_WIDTH // 2 - self.x_back // 2
        self.back_rect = pygame.Rect(30,30, self.back.get_width(), self.back.get_height())

        self.map3 = pygame.image.load('D:\\Gameproject\\images\\menu\\map3.png')
        self.x_map3, self.y_map3 = self.map3.get_size()
        self.map3 = pygame.transform.scale(self.map3, (self.x_map3/1,self.y_map3/1))
        self.map3.set_colorkey((255, 255, 255))
        self.pos_xm3 = WINDOW_WIDTH // 2 - self.x_map3 // 2
        self.map3_rect = pygame.Rect(self.pos_xm3,WINDOW_HEIGHT//2 +50, self.map3.get_width(), self.map3.get_height())

        # self.mouse = pygame.transform.scale(self.mouse, (20,20))
        # self.mouse.set_colorkey((255, 255, 255))

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # pygame.mouse.set_visible(False)

    def render(self):
        while True:
            self.clock.tick(60)
            self.screen.fill((0,0,0))
            x, y = pygame.mouse.get_pos()  
            self.screen.blit(self.gamev1,(self.pos_xt,WINDOW_HEIGHT//2-200))
            self.screen.blit(self.start,(self.pos_xs,WINDOW_HEIGHT//2 -50))
            self.screen.blit(self.quit,(self.pos_xq,WINDOW_HEIGHT//2+ 50))  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()     
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(event.pos):
                        self.render_list()
                        return
                    if self.quit_rect.collidepoint(event.pos):
                        sys.exit()
            pygame.display.update()
        
    def render_list(self):
        while True:
            self.clock.tick(60)
            self.screen.fill((0,0,0))
            x, y = pygame.mouse.get_pos() 
            self.screen.blit(self.back,(30,30)) 
            self.screen.blit(self.map1,(self.pos_xm1,WINDOW_HEIGHT//2-150))
            self.screen.blit(self.map2,(self.pos_xm2,WINDOW_HEIGHT//2 -50))
            self.screen.blit(self.map3,(self.pos_xm3,WINDOW_HEIGHT//2+ 50))  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()     
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_rect.collidepoint(event.pos):
                        self.render()
                        return
                    if self.map1_rect.collidepoint(event.pos):
                        return 1
                    if self.map2_rect.collidepoint(event.pos):
                        return 2  
                    if self.map3_rect.collidepoint(event.pos):
                        return 3
            pygame.display.update()
    def back_(self):
        self.clock.tick(60)
        self.screen.blit(self.back,(10,10))    
            

