from settings import *
from sprites import *
from groups import *
from support import *
from save import*

class Menu:
    # color rgb
    white = (255,255,255)
    black = (0,0,0)
    blue = (100,149,237)
    red = (254,92,92)
    xam = (59, 68, 75)
    def __init__(self, main):
        pygame.init()
        self.clock=pygame.time.Clock()  #fps
        self.screen = main.display_surface
        self.main = main
        self.bg = pygame.image.load(join('images','New folder', 'Background_0.png'))
        self.bg = pygame.transform.scale(self.bg,(347*(1200/347),275*(1200/275)))
        self.hp_ = pygame.image.load(r"images\New folder\heart.png")
        self.hp_ = pygame.transform.scale(self.hp_,(17*1.5, 17*1.5))
        self.hp_.set_colorkey((0,0,0))

        self.save = Save(self)
        # font sảnh
        self.font = pygame.font.Font(None, 70)
        self.font10 = pygame.font.Font(None, 90) 
        # font listmap
        self.font1 = pygame.font.Font(None, 40)
        self.font2 = pygame.font.Font(None, 60)
        # font finish
        self.font3 = pygame.font.Font(None, 45) 

    # tao hinh chu nhat mờ
    def rect_depth(self,size,depth,color):
        rect = pygame.Surface(size)
        rect.fill(color)
        rect.set_alpha(depth)
        return rect
    # chay menu
    def render(self):
        # tao nut
        title = self.font10.render("Game Version 1", True, self.white)

        start = self.font.render("Start", True, self.white)
        rect_start = pygame.Rect(WINDOW_WIDTH/2-start.get_width()/2, WINDOW_HEIGHT/2-50, start.get_width(), start.get_height())

        quit = self.font.render("Quit", True, self.white)
        rect_quit = pygame.Rect(WINDOW_WIDTH/2-quit.get_width()/2, WINDOW_HEIGHT/2+50, quit.get_width(), quit.get_height())

        rect_sound = pygame.Rect(WINDOW_WIDTH-100,WINDOW_HEIGHT-100, 50,50)

        next = 0
        running = True
        # self.menu_bg_music.stop()
        while running:
            self.clock.tick(60)
            self.screen.blit(self.bg,(0,0))
            # in nut ra man hinh
            pygame.draw.rect(self.screen,self.red,rect_sound,border_radius=10)
            self.screen.blit(title,(WINDOW_WIDTH/2-title.get_width()/2, WINDOW_HEIGHT/2-200))
            self.screen.blit(start,(WINDOW_WIDTH/2-start.get_width()/2, WINDOW_HEIGHT/2-50))
            self.screen.blit(quit,(WINDOW_WIDTH/2-quit.get_width()/2, WINDOW_HEIGHT/2+50))  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect_start.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        running = False
                        next = 2
                    if rect_quit.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        next = 0
                        running = False
                    if rect_sound.collidepoint(event.pos):
                        self.sound()
                # doi mau neu di chuot vao nut
                if event.type == pygame.MOUSEMOTION:
                    if rect_start.collidepoint(event.pos):
                       start = self.font.render("Start", True, self.red)
                    else:
                       start = self.font.render("Start", True, self.white)
                    if rect_quit.collidepoint(event.pos):
                       quit = self.font.render("Quit", True, self.red)
                    else:
                       quit = self.font.render("Quit", True, self.white)
            pygame.display.update()
        return next
    # chay danh sach map va chon map 
    def render_list(self):
        # tao nut
        map1 = self.font2.render("Map 1", True, self.white)
        rect_map1 = pygame.Rect(WINDOW_WIDTH/2-map1.get_width()/2,WINDOW_HEIGHT/2-150, map1.get_width(), map1.get_height())

        map2 = self.font2.render("Map 2", True, self.white)
        rect_map2 = pygame.Rect(WINDOW_WIDTH/2-map2.get_width()/2,WINDOW_HEIGHT/2-50, map2.get_width(), map2.get_height())

        map3 = self.font2.render("Map 3", True, self.white)
        rect_map3 = pygame.Rect(WINDOW_WIDTH/2-map3.get_width()/2,WINDOW_HEIGHT/2+50, map3.get_width(), map3.get_height())

        back = self.font1.render("Back", True, self.white)
        back_rect = pygame.Rect(30,30, back.get_width(), back.get_height())

        next = 0
        running = True
        while running:
            self.clock.tick(60)
            self.screen.blit(self.bg,(0,0))
            # in nut ra man hinh
            self.screen.blit(back,(30,30)) 
            self.screen.blit(map1,(WINDOW_WIDTH/2-map1.get_width()/2,WINDOW_HEIGHT/2-150))
            self.screen.blit(map2,(WINDOW_WIDTH/2-map2.get_width()/2,WINDOW_HEIGHT/2-50))
            self.screen.blit(map3,(WINDOW_WIDTH/2-map3.get_width()/2,WINDOW_HEIGHT/2+50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        self.screen.blit(self.bg,(0,0))
                        running = False
                        next = 1
                    if rect_map1.collidepoint(event.pos):
                        running = False
                        next = 11
                    if rect_map2.collidepoint(event.pos):
                        running = False
                        next = 12
                    if rect_map3.collidepoint(event.pos):
                        running = False
                        next = 13
                # doi mau nut
                if event.type == pygame.MOUSEMOTION:
                    if rect_map1.collidepoint(event.pos):
                       map1 = self.font2.render("Map 1", True, self.red)
                    else:
                       map1 = self.font2.render("Map 1", True, self.white)
                    if rect_map2.collidepoint(event.pos):
                       map2 = self.font2.render("Map 2", True, self.red)
                    else:
                       map2 = self.font2.render("Map 2", True, self.white)
                    if rect_map3.collidepoint(event.pos):
                       map3 = self.font2.render("Map 3", True, self.red)
                    else:
                       map3 = self.font2.render("Map 3", True, self.white)
                    if back_rect.collidepoint(event.pos):
                       back = self.font1.render("Back", True, self.red)
                    else:
                       back = self.font1.render("Back", True, self.white)
            pygame.display.update()
        return next 
    # chay khung hien thi diem sau khi finish
    def finish(self, score, time, name):
        #  khung finish
        X = WINDOW_WIDTH/2-300
        Y = WINDOW_HEIGHT/2-200
        W = 600
        H = 400
        # back ----next
        # ----score---
        # ----text----
        # restart--menu
        text1 = self.font3.render(f"Score: {score}", True, self.white)
        text2 = self.font3.render(f"Good job", True, self.white)
        # tao nut
        img_back = self.font3.render("Back", True, self.white)
        rect_back = pygame.Rect(X+50,Y+50, img_back.get_width(), img_back.get_height())
        
        img_next = self.font3.render("Next", True, self.white)
        rect_next = pygame.Rect(X+W-img_next.get_width()-50,Y+50, img_next.get_width(), img_next.get_height())

        img_restart = self.font3.render("Restart", True, self.white)
        rect_restart = pygame.Rect(X+50,Y+H-80, img_restart.get_width(), img_restart.get_height())

        img_menu = self.font3.render("Menu", True, self.white)
        rect_menu = pygame.Rect(X+W-img_menu.get_width()-50,Y+H-80, img_menu.get_width(), img_menu.get_height())

        next = 0
        running = True
        while running:
            rect = pygame.Rect(X,Y,W,H)
            pygame.draw.rect(self.screen, self.blue, rect, border_radius=20)

            self.screen.blit(text1,(X+W/2-text1.get_width()/2,Y+H/2-50))
            self.screen.blit(text2,(X+W/2-text2.get_width()/2,Y+H/2+20))
            self.screen.blit(img_back,(X+50,Y+50))
            self.screen.blit(img_next,(X+W-img_next.get_width()-50,Y+50))
            self.screen.blit(img_restart,(X+50,Y+H-80))
            self.screen.blit(img_menu,(X+W-img_menu.get_width()-50,Y+H-80))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
                # doi mau chu
                if event.type == pygame.MOUSEMOTION:
                    if rect_back.collidepoint(event.pos):
                       img_back = self.font3.render("Back", True, self.red)
                    else:
                       img_back = self.font3.render("Back", True, self.white)
                    if rect_menu.collidepoint(event.pos):
                       img_menu = self.font3.render("Menu", True, self.red)
                    else:
                       img_menu = self.font3.render("Menu", True, self.white)
                    if rect_next.collidepoint(event.pos):
                       img_next = self.font3.render("Next", True, self.red)
                    else:
                       img_next = self.font3.render("Next", True, self.white)
                    # restart
                    if rect_restart.collidepoint(event.pos):
                       img_restart = self.font3.render("Restart", True, self.red)
                    else:
                       img_restart = self.font3.render("Restart", True, self.white) 
            pygame.display.update() 
        return next
    # chay khung lua chon tiep tuc hay restart khi chon map 
    def note(self, name):
        # khung cua note
        W = WINDOW_WIDTH//2-150
        H = WINDOW_HEIGHT//2-100
        rect = pygame.Rect(W, H, 300,200)
        font = pygame.font.Font(None, 70)
        font1 = pygame.font.Font(None, 50)
        if name == 11:
            title = font.render("Map 1", True, self.white)
        if name == 12:
            title = font.render("Map 2", True, self.white)
        if name == 13:
            title = font.render("Map 3", True, self.white)
        continue_ = font1.render("Continue", True, self.white)
        rect_continue = pygame.Rect(W+300/2-continue_.get_width()/2,H+50,continue_.get_width(), continue_.get_height())
        restart = font1.render("Restart", True, self.white)
        rect_restart = pygame.Rect(W+300/2-restart.get_width()/2,H+130,restart.get_width(), restart.get_height())
        next = 3
        running = True
        while running:
            self.screen.blit(self.bg,(0,0))
            self.screen.blit(title, (WINDOW_WIDTH/2-title.get_width()//2,WINDOW_HEIGHT//2-150))

            self.screen_note = pygame.draw.rect(self.screen, self.blue, rect, border_radius=20)
            self.screen.blit(continue_,(W+300/2-continue_.get_width()/2,H+50))
            self.screen.blit(restart,(W+300/2-restart.get_width()/2,H+130))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    next = 0
                    running = False
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
                    if rect_continue.collidepoint(event.pos):
                       continue_ = font1.render("Continue", True, self.red)
                    else:
                       continue_ = font1.render("Continue", True, self.white)
                    if rect_restart.collidepoint(event.pos):
                       restart = font1.render("Restart", True, self.red)
                    else:
                       restart = font1.render("Restart", True, self.white)
            pygame.display.update()
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
    # hp player
    def hp_player(self, x, y):
        i = 0
        while i < (self.main.player.hp) * self.hp_.get_width():
            self.screen.blit(self.hp_,(x+i,y))
            i+=self.hp_.get_width()

    def sound(self):
        # khung
        W = WINDOW_WIDTH-400
        H = WINDOW_HEIGHT-300
        rect = pygame.Rect(W, H, 350, 250)

        volume = self.font1.render("Volume Bg", True, self.white)
        rect1 = pygame.Rect(W+350/2-200/2, H+250-70, 200, 10)
        rect_1 = pygame.Rect(W+350/2-200/2+2, H+250-70+2, 200-4,10-4)
        rect_1_ = pygame.Rect(W+350/2-200/2+2, H+250-70+2, 100,10-4)

        effect = self.font1.render("Volume Effect", True, self.white)
        rect2 = pygame.Rect(W+350/2-200/2, H+70, 200, 10)
        rect_2 = pygame.Rect(W+350/2-200/2+2, H+70+2, 200-4,10-4)
        rect_2_ = pygame.Rect(W+350/2-200/2+2, H+70+2, 100,10-4)

        running = True
        press1 = False
        press2 = False
        while running:
            self.clock.tick(60)
            pygame.draw.rect(self.screen,self.blue,rect,border_radius=20)

            pygame.draw.rect(self.screen,self.white,rect1,border_radius=20)
            pygame.draw.rect(self.screen,self.black,rect_1,border_radius=20)
            pygame.draw.rect(self.screen,self.red,rect_1_,border_radius=20)

            pygame.draw.rect(self.screen,self.white,rect2,border_radius=20)
            pygame.draw.rect(self.screen,self.black,rect_2,border_radius=20)
            pygame.draw.rect(self.screen,self.red,rect_2_,border_radius=20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False 
                if event.type == pygame.MOUSEBUTTONUP:
                    press1 = False
                    press2 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect1.collidepoint(event.pos):
                        press1 = True
                    else:
                        press1 = False
                    if rect2.collidepoint(event.pos):
                        press2 = True
                    else:
                        press2 = False
                    if not rect.collidepoint(event.pos):
                        running = False
                if press1 == True:
                    if event.pos[0] > W+350/2-200/2+2 and event.pos[0] < W+350/2-200/2+2 + 200-4:
                        rect_1_ = pygame.Rect(W+350/2-200/2+2, H+250-70+2, event.pos[0]-(W+350/2-200/2+2),10-4)
                if press2 == True:
                    if event.pos[0] > W+350/2-200/2+2 and event.pos[0] < W+350/2-200/2+2 + 200-4:
                        rect_2_ = pygame.Rect(W+350/2-200/2+2, H+70+2, event.pos[0]-(W+350/2-200/2+2),10-4)

            pygame.display.update()
        return

    def enter_map(self):
        self.menu_bg_music.stop()
     
# Menu().render()
# Menu().finish() 
# Menu().render()   
        

        

            

