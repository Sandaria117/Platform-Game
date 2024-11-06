import pygame
import sys
from settings import *
from sprites import *
from groups import *
from support import *
from save import*

class Menu:
    # color rgb
    white = (255,255,255)
    black = (0,0,0)
    blue = (0, 0, 255)
    red = (254,92,92)
    xam = (59, 68, 75)
    # tao cac nut bam 
    def __init__(self, main):
        pygame.init()
        self.clock=pygame.time.Clock()  #fps
        self.screen = main.display_surface
        self.main = main
        self.bg = pygame.image.load(r"images\New folder\snapedit_1730894044855.jpeg")
        self.bg = pygame.transform.scale(self.bg,(347*(1200/347),275*(1200/275)))
        self.hp_ = pygame.image.load(r"images\New folder\heart.png")
        self.hp_ = pygame.transform.scale(self.hp_,(17*1.5, 17*1.5))
        self.hp_.set_colorkey((0,0,0))

        self.save = Save(self)

        self.font = pygame.font.Font(None, 70)
        self.font1 = pygame.font.Font(None, 40)
        self.font2 = pygame.font.Font(None, 60)
        font5 = pygame.font.Font(None, 36)
        font6= pygame.font.Font(None, 45)
        self.font10 = pygame.font.Font(None, 90) 

        # tao nut bam
        text = "Game Version 1"
        self.title = self.font10.render(text, True, self.white)
        self.x_title, self.y_title = self.title.get_size()
        self.pos_xt = WINDOW_WIDTH // 2 - self.x_title // 2

        text = "Start"
        self.start = self.font.render(text, True, self.white)
        self.x_start, self.y_start = self.start.get_size()
        self.pos_xs = WINDOW_WIDTH // 2 - self.x_start // 2
        self.start_rect = pygame.Rect(self.pos_xs,WINDOW_HEIGHT//2 - 50, self.start.get_width(), self.start.get_height())
        # self.start_rect = pygame.draw.rect(self.screen, self.blue, rect, border_radius=20)

        text = "Quit"
        self.quit = self.font.render(text, True, self.white)
        self.x_quit, self.y_quit = self.quit.get_size()
        self.pos_xq = WINDOW_WIDTH // 2 - self.x_quit // 2
        self.quit_rect = pygame.Rect(self.pos_xq,WINDOW_HEIGHT//2 +50, self.quit.get_width(), self.quit.get_height())
        # self.quit_rect = pygame.draw.rect(self.screen, self.blue, rect, border_radius=20)

        text = "Map 1"
        self.map1 = self.font2.render(text, True, self.white)
        self.x_map1, self.y_map1 = self.map1.get_size()
        self.pos_xm1 = WINDOW_WIDTH // 2 - self.x_map1 // 2
        self.map1_rect = pygame.Rect(self.pos_xm1,WINDOW_HEIGHT//2 -150, self.map1.get_width(), self.map1.get_height())

        text = "Map 2"
        self.map2 = self.font2.render(text, True, self.white)
        self.x_map2, self.y_map2 = self.map2.get_size()
        self.pos_xm2 = WINDOW_WIDTH // 2 - self.x_map2 // 2
        self.map2_rect = pygame.Rect(self.pos_xm2,WINDOW_HEIGHT//2 -50, self.map2.get_width(), self.map2.get_height())

        text = "Map 3"
        self.map3 = self.font2.render(text, True, self.white)
        self.x_map3, self.y_map3 = self.map3.get_size()
        self.pos_xm3 = WINDOW_WIDTH // 2 - self.x_map3 // 2
        self.map3_rect = pygame.Rect(self.pos_xm3,WINDOW_HEIGHT//2 +50, self.map3.get_width(), self.map3.get_height())

        text = "Back"
        self.back = self.font1.render(text, True, self.white)
        self.x_back, self.y_back = self.back.get_size()
        self.pos_xback = WINDOW_WIDTH // 2 - self.x_back // 2

        text = "RESTART"
        self.restart = self.font1.render(text, True, self.white)
        self.x_restart, self.y_restart = self.restart.get_size()

        text = "CONTINUE"
        self.continue_ = self.font1.render(text, True, self.white)
        self.x_continue, self.y_continue = self.continue_.get_size()

        # tao nut bam
        text = "Game Version 1"
        self.title = self.font10.render(text, True, self.white)
        self.x_title, self.y_title = self.title.get_size()
        self.pos_xt = WINDOW_WIDTH // 2 - self.x_title // 2

        text = "Start"
        self.start = self.font.render(text, True, self.white)
        self.x_start, self.y_start = self.start.get_size()
        self.pos_xs = WINDOW_WIDTH // 2 - self.x_start // 2
        self.start_rect = pygame.Rect(self.pos_xs,WINDOW_HEIGHT//2 - 50, self.start.get_width(), self.start.get_height())
        # self.start_rect = pygame.draw.rect(self.screen, self.blue, rect, border_radius=20)

        text = "Quit"
        self.quit = self.font.render(text, True, self.white)
        self.x_quit, self.y_quit = self.quit.get_size()
        self.pos_xq = WINDOW_WIDTH // 2 - self.x_quit // 2
        self.quit_rect = pygame.Rect(self.pos_xq,WINDOW_HEIGHT//2 +50, self.quit.get_width(), self.quit.get_height())
        # self.quit_rect = pygame.draw.rect(self.screen, self.blue, rect, border_radius=20)

        text = "Map 1"
        self.map1 = self.font2.render(text, True, self.white)
        self.x_map1, self.y_map1 = self.map1.get_size()
        self.pos_xm1 = WINDOW_WIDTH // 2 - self.x_map1 // 2
        self.map1_rect = pygame.Rect(self.pos_xm1,WINDOW_HEIGHT//2 -150, self.map1.get_width(), self.map1.get_height())

        text = "Map 2"
        self.map2 = self.font2.render(text, True, self.white)
        self.x_map2, self.y_map2 = self.map2.get_size()
        self.pos_xm2 = WINDOW_WIDTH // 2 - self.x_map2 // 2
        self.map2_rect = pygame.Rect(self.pos_xm2,WINDOW_HEIGHT//2 -50, self.map2.get_width(), self.map2.get_height())

        text = "Map 3"
        self.map3 = self.font2.render(text, True, self.white)
        self.x_map3, self.y_map3 = self.map3.get_size()
        self.pos_xm3 = WINDOW_WIDTH // 2 - self.x_map3 // 2
        self.map3_rect = pygame.Rect(self.pos_xm3,WINDOW_HEIGHT//2 +50, self.map3.get_width(), self.map3.get_height())

        text = "Back"
        self.back = self.font1.render(text, True, self.white)
        self.x_back, self.y_back = self.back.get_size()
        self.pos_xback = WINDOW_WIDTH // 2 - self.x_back // 2

        text = "RESTART"
        self.restart = self.font1.render(text, True, self.white)
        self.x_restart, self.y_restart = self.restart.get_size()

        text = "CONTINUE"
        self.continue_ = self.font1.render(text, True, self.white)
        self.x_continue, self.y_continue = self.continue_.get_size()
    # tao hinh chu nhat mờ
    def rect_depth(self,size,depth,color):
        rect = pygame.Surface(size)
        rect.fill(color)
        rect.set_alpha(depth)
        return rect
    # chay menu
    def render(self):
        running = True
        next = 0
        while running:
            self.clock.tick(60)
            self.screen.blit(self.bg,(0,0))
            # self.screen.fill(self.xam)

            # screen.fill((0,0,0))
            self.screen.blit(self.title,(self.pos_xt,WINDOW_HEIGHT//2 -200))
            self.screen.blit(self.start,(self.pos_xs,WINDOW_HEIGHT//2 -50))
            self.screen.blit(self.quit,(self.pos_xq,WINDOW_HEIGHT//2+ 50))  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.quit()     
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_rect.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        running = False
                        next = 2
                        # return  self.render_list()
                    if self.quit_rect.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        sys.exit()
                        next = 0
                        running = False
                if event.type == pygame.MOUSEMOTION:
                    if self.start_rect.collidepoint(event.pos):
                       self.start = self.font.render("Start", True, self.red)
                    else:
                       self.start = self.font.render("Start", True, self.white)
                    if self.quit_rect.collidepoint(event.pos):
                       self.quit = self.font.render("Quit", True, self.red)
                    else:
                       self.quit = self.font.render("Quit", True, self.white)
            pygame.display.update()
        print("chay het render")
        # if next == 2:
        #     self.render_list()
        # print(next)
        return next
    # chay danh sach map va chon map 
    def render_list(self):
        running = True
        next = 0
        while running:
            self.clock.tick(60)
            self.screen.blit(self.bg,(0,0))
            self.screen.blit(self.back,(30,30)) 
            self.back_rect = pygame.Rect(30,30, self.back.get_width(), self.back.get_height())

            self.screen.blit(self.map1,(self.pos_xm1,WINDOW_HEIGHT//2-150))
            self.screen.blit(self.map2,(self.pos_xm2,WINDOW_HEIGHT//2 -50))
            self.screen.blit(self.map3,(self.pos_xm3,WINDOW_HEIGHT//2+ 50))  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    running = False
                    next = 0   
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_rect.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        running = False
                        next = 1
                    if self.map1_rect.collidepoint(event.pos):
                        running = False
                        next = 11
                        # return sys.exit()
                    if self.map2_rect.collidepoint(event.pos):
                        running = False
                        next = 12
                        # return
                    if self.map3_rect.collidepoint(event.pos):
                        running = False
                        next = 13
                        # return
                if event.type == pygame.MOUSEMOTION:
                    if self.map1_rect.collidepoint(event.pos):
                       self.map1 = self.font2.render("Map 1", True, self.red)
                    else:
                       self.map1 = self.font2.render("Map 1", True, self.white)
                    if self.map2_rect.collidepoint(event.pos):
                       self.map2 = self.font2.render("Map 2", True, self.red)
                    else:
                       self.map2 = self.font2.render("Map 2", True, self.white)
                    if self.map3_rect.collidepoint(event.pos):
                       self.map3 = self.font2.render("Map 3", True, self.red)
                    else:
                       self.map3 = self.font2.render("Map 3", True, self.white)
                    if self.back_rect.collidepoint(event.pos):
                       self.back = self.font1.render("Back", True, self.red)
                    else:
                       self.back = self.font1.render("Back", True, self.white)
            pygame.display.update()
        print("chay het render_list")
        # if next == 1:
        #     self.render()
        # print(next)
        return next 
    # chay khung hien thi diem sau khi finish
    def finish(self, score, time, name):
        #  khung finish
        W = WINDOW_WIDTH//2-300 
        H = WINDOW_HEIGHT//2-200
        
        # display.set_mode((600,400))
        font = pygame.font.Font(None, 36)
        font2 = pygame.font.Font(None, 50)

        # tao nut
        text1 = "Score: " + str(score)
        text2 = time

        text = "MENU"
        img_menu = font.render(text, True, self.white)
        xm, ym = img_menu.get_size()
        rect_menu = pygame.Rect(W+600//2+xm+60,H+400-100, img_menu.get_width(), img_menu.get_height())

        text = "NEXT"
        img_next = font.render(text, True, self.white)
        xn, yn = img_next.get_size()
        rect_next = pygame.Rect(W+600-xn-20,H+20, img_next.get_width(), img_next.get_height())

        text = "BACK"
        img_back = font.render(text, True, self.white)
        xb, yb= img_back.get_size()
        rect_back = pygame.Rect(W+20,H+20, img_back.get_width(), img_back.get_height())

        text = "RESTART"
        img_restart = font.render(text, True, self.white)
        xr, yr = img_restart.get_size()
        rect_restart = pygame.Rect(W+600//2-xr-60,H+400-100, img_restart.get_width(), img_restart.get_height())

        img_text1 = font2.render(text1, True, self.white)
        xt1, yt1 = img_text1.get_size()

        img_text2 = font2.render(text2, True, self.white)
        xt2 ,yt2 = img_text2.get_size()

        next = 0
        running = True
        while running:
            rect = pygame.Rect(W, H, 600,400)
            # rect = self.rect_depth((600,400),10,self.black)
            # screen.blit(rect,(W,H))
            pygame.draw.rect(self.screen, self.blue, rect, border_radius=20)
            self.screen.blit(img_text1,(W+600//2 - xt1//2,H+100))
            self.screen.blit(img_text2,(W+600//2 - xt2//2,H+180))

            self.screen.blit(img_next,(W+600-xn-20,H+20))
            # rect_next = pygame.Rect(600-xn-20,20, img_next.get_width(), img_next.get_height())

            self.screen.blit(img_back,(W+20,H+20))
            # rect_back = pygame.Rect(20,20, img_back.get_width(), img_back.get_height())

            self.screen.blit(img_restart,(W+600//2-xr-60,H+400-100))
            # rect_restart = pygame.Rect(600//2-xr-60,400-100, img_restart.get_width(), img_restart.get_height())

            self.screen.blit(img_menu,(W+600//2+xm+60,H+400-100))
            # rect_menu = pygame.Rect(600//2+xm+60,400-100, img_menu.get_width(), img_menu.get_height())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    next = 0
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_menu.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        running = False
                        next = 1
                    if rect_back.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        running = False
                        next = 2
                    if rect_next.collidepoint(event.pos):
                        if name == 13:
                            return 11
                        else:
                            return name+1
                    if rect_restart.collidepoint(event.pos):
                        return name
                if event.type == pygame.MOUSEMOTION:
                    # back
                    if rect_back.collidepoint(event.pos):
                       img_back = font.render("BACK", True, self.red)
                    else:
                       img_back = font.render("BACK", True, self.white)
                    # menu
                    if rect_menu.collidepoint(event.pos):
                       img_menu = font.render("MENU", True, self.red)
                    else:
                       img_menu = font.render("MENU", True, self.white)
                    # next
                    if rect_next.collidepoint(event.pos):
                       img_next = font.render("NEXT", True, self.red)
                    else:
                       img_next = font.render("NEXT", True, self.white)
                    # restart
                    if rect_restart.collidepoint(event.pos):
                       img_restart = font.render("RESTART", True, self.red)
                    else:
                       img_restart = font.render("RESTART", True, self.white) 
            pygame.display.update() 
        print("chay het finish")
        # print(next)
        return next
        # if next == 1:
        #     self.render()
        # if next == 2:
        #     self.render_list()
    # chay khung lua chon tiep tuc hay restart khi chon map 
    def note(self, name):
        # khung cua note
        W = WINDOW_WIDTH//2-150
        H = WINDOW_HEIGHT//2-100
        rect = pygame.Rect(W, H, 300,200)

        # touch_area cua cac nut trong note
        font = pygame.font.Font(None, 50)
        if name == 11:
            title = font.render("Map 1", True, self.white)
        if name == 12:
            title = font.render("Map 2", True, self.white)
        if name == 13:
            title = font.render("Map 3", True, self.white)
        rect_continue = pygame.Rect(W+300//2-self.x_continue//2,H+50, self.continue_.get_width(), self.continue_.get_height())
        rect_restart = pygame.Rect(W+300//2-self.x_restart//2,H+130, self.restart.get_width(), self.restart.get_height())
        running = True

        while running:
            self.screen.blit(self.bg,(0,0))
            self.screen.blit(title, (WINDOW_WIDTH//2-title.get_width()//2,WINDOW_HEIGHT//2-150))
            self.screen_note = pygame.draw.rect(self.screen, self.blue, rect, border_radius=20)
            self.screen.blit(self.continue_,(W+300//2-self.x_continue//2,H+50))
            self.screen.blit(self.restart,(W+300//2-self.x_restart//2,H+130))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_continue.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        running = False
                        next = 1
                    elif rect_restart.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        running = False
                        next = 0
                    else:
                        running = False
                        next = 3
                if event.type == pygame.MOUSEMOTION:
                    # CONTINUE
                    if rect_continue.collidepoint(event.pos):
                       self.continue_ = self.font1.render("CONTINUE", True, self.red)
                    else:
                       self.continue_ = self.font1.render("CONTINUE", True, self.white)
                    if rect_restart.collidepoint(event.pos):
                       self.restart = self.font1.render("RESTART", True, self.red)
                    else:
                       self.restart = self.font1.render("RESTART", True, self.white)
            pygame.display.update()
        print("chay het note")
        return next
    # hp quai
    def hp(self, x, y, width, height, h, hp, curhp):
        sx = x-self.main.player.hitbox_rect.x + WINDOW_WIDTH / 2 - width/2+10
        sy = y-self.main.player.hitbox_rect.y + WINDOW_HEIGHT / 2 - height//2
        # gia tri 1 cuc hp
        value = width/hp
        # khung hp
        rect = pygame.Rect(sx, sy, width, h)
        # vien khung hp
        rect_ = pygame.Rect(sx+1,sy+1,width-2,h-2)
        # vach hp
        rect_hp = pygame.Rect(sx+1,sy+1,value*curhp,h-2)
        pygame.draw.rect(self.screen,self.white,rect)
        pygame.draw.rect(self.screen,self.black,rect_)
        pygame.draw.rect(self.screen,self.red,rect_hp)
    
    def hp_player(self, x, y):
        i = 0
        while i < (self.main.player.hp)*self.hp_.get_width():
            self.screen.blit(self.hp_,(x+i,y))
            i+=self.hp_.get_width()
        # for i in (0,self.main.player_hp*self.hp_.get_width(),self.hp_.get_width()):
        #     self.screen.blit(self.hp_,(x+i,y))


     
# Menu().render()
# Menu().finish() 
# Menu().render()   

            

