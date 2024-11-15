from settings import *
from sprites import *
from groups import *
from support import * 
from timer import *
from menu import *

class Game:
    def __init__(self):
        pygame.init() #khởi tạo
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #bên setting
        pygame.display.set_caption("Flatformer") #tiêu đề 
        self.clock=pygame.time.Clock()  #fps
        self.running = True
        
        #groups
        self.all_sprites = AllSprite()  #tạo 1 nhóm all_sprite để quản lý toàn bộ sprite => update các thứ gọi dễ hơn
        self.collision_sprites = pygame.sprite.Group()    #tạo 1 nhóm để quản lý toàn bộ sprite chướng ngoaij vật
        self.trap_sprites = pygame.sprite.Group()
        self.enermy_vip_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.coin_sprites = pygame.sprite.Group()
        self.checkpoint_sprites = pygame.sprite.Group()
        
        #score, hp
        self.score = 0
        self.font = pygame.font.Font(None, 36)  #tạo 1 font obj -> font in chữ ra màn
        #import
        self.import_assets()

        #save
        self.save = Save(self)
        self.menu = Menu(self)
        self.data = []
        self.lvl = None   
        self.finish =  pygame.sprite.Group() 
        self.back_button = self.font.render("BACK", True, (255,255,255))
        self.back_rect = pygame.Rect(WINDOW_WIDTH-100,20,self.back_button.get_width(), self.back_button.get_height())

    def import_assets(self):
        #frames
        self.player_frames = {
            'idle': import_folder('images','player2','idle'),
            'walk': import_folder('images','player2','walk'),
            'jump': import_folder('images','player2','jump'),
            'attack': import_folder('images','player2','attack'),
            'death': import_folder('images','player2','death'),
            'hurt': import_folder('images','player2','hurt')
        }
        self.enermy2_frames = {
            'walk': import_folder('images','enermy','forest','walk'),    
            'attack': import_folder('images','enermy','forest','attack'),
            'death': import_folder('images','enermy','forest','death'),
            'hurt': import_folder('images','enermy','forest','hurt'),
            'idle': import_folder('images','enermy','forest','idle')
        }
        self.coin_frames = {
            'idle': import_folder('images','accessory','coin', 'idle', width=32, height=32)
        }
        self.checkpoint_frames = {
            'idle': import_folder('images','accessory','checkpoint', 'idle')
        }
        self.platform_frames = {
            'idle': import_folder('images','accessory','platform', 'idle', width=64, height=20)
        }
        self.saw_frames = {
            'idle': import_folder('images','accessory','saw', 'idle')
        }
        #audio
        self.bg_music = pygame.mixer.Sound(join('audio', 'bg_music.ogg'))
        self.bg_music.set_volume(0.4)
        self.coin_audio = pygame.mixer.Sound(join('audio', 'audio_coin.wav'))
        self.coin_audio.set_volume(0.2)
        self.jump_audio = pygame.mixer.Sound(join('audio', 'audio_jump.wav'))
        self.jump_audio.set_volume(0.1)
        self.attack_audio = pygame.mixer.Sound(join('audio', 'audio_attack.wav'))
        self.damage_audio = pygame.mixer.Sound(join('audio', 'audio_damage.wav'))
        self.damage_audio.set_volume(0.5)
        self.active_audio = pygame.mixer.Sound(join('audio', 'audio_active.mp3'))
        self.active_audio.set_volume(0.4)
        self.death_audio = pygame.mixer.Sound(join('audio','audio_death.ogg'))
        self.death_audio.set_volume(0.2)

    def setup(self, name):
        map = load_pygame(join('data', 'tmx', f'map{name}.tmx'))
        #dust
        self.dust_vertical_up_positions = []
        self.dust_vertical_down_positions = []
        # trang trí   
        for x, y, image in map.get_layer_by_name('Decorate').tiles():  # trang trí         
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE  * SCALE_FACTOR), scaled_image, self.all_sprites)
        for x, y, image in map.get_layer_by_name('Background').tiles():
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE * SCALE_FACTOR), scaled_image, self.all_sprites)  #sprite_bg ->all_sprite
        for x, y, image in map.get_layer_by_name('Decorate2').tiles():  # trang trí         
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE  * SCALE_FACTOR), scaled_image, self.all_sprites)
        for x, y, image in map.get_layer_by_name('Finish').tiles():
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE * SCALE_FACTOR), scaled_image,  (self.finish, self.all_sprites))
        # Thực thể
        for obj in map.get_layer_by_name('Object'):             
            if obj.name == 'Player':
                self.player = Player((obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR ), (self.all_sprites, self.player_sprites), self.collision_sprites, self. player_frames, self.jump_audio, self.attack_audio, self.death_audio, 5) 
            if obj.name == 'Enermy_2':
                trangthai = [0,0,0]
                Enermy_2(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.enermy2_frames,(self.enermy_vip_sprites, self.all_sprites), self.player_sprites, trangthai)
            if obj.name == 'Checkpoint':
                Checkpoint((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.checkpoint_frames, (self.all_sprites, self.checkpoint_sprites), self.active_audio)
            if obj.name == 'Coin':
                Coin((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.coin_frames, (self.coin_sprites, self.all_sprites))
            if obj.name == 'Spike':
                scaled_image = pygame.transform.scale(obj.image, (obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
                Spike((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), scaled_image, (self.all_sprites, self.trap_sprites)) 
            if obj.name == 'Saw_1.1':
                Saw_1_1(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.saw_frames,(self.trap_sprites, self.all_sprites), -1 , "bottom") #1 khu vực Skeleton có thể di chuyển 
            if obj.name == 'Saw_1.2':
                Saw_1_2(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.saw_frames,(self.trap_sprites, self.all_sprites), -1 , "right")
            if obj.name == 'Platform_horizontal':
                Dust_canmove_horizontal(pygame.Rect(obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR), self.platform_frames, (self.all_sprites, self.collision_sprites), 1, "left")
            if obj.name == "Platform_vertical":
                Dust_canmove_vertical(pygame.Rect(obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR), self.platform_frames, (self.all_sprites, self.collision_sprites), "return", 1, "top")
            if obj.name == 'Platform_vertical_up':
                self.dust_vertical_up_positions.append((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
            if obj.name == 'Platform_vertical_down':
                self.dust_vertical_down_positions.append((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
        # Đất
        for obj in map.get_layer_by_name('Dust'):        
            scaled_image = pygame.transform.scale(obj.image, (obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
            Sprites((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), scaled_image, (self.all_sprites, self.collision_sprites))   #sprite_collision -> collision_sprite

        def create_dust():
            for position in self.dust_vertical_up_positions:
                Dust_canmove_vertical(pygame.Rect(position), self.platform_frames, (self.all_sprites, self.collision_sprites), "loop", -1, "bottom")
            for position in self.dust_vertical_down_positions:
                Dust_canmove_vertical(pygame.Rect(position), self.platform_frames, (self.all_sprites, self.collision_sprites), "loop", 1, "top")

        #cooldown
        self.cooldown_hp = Timer(500)   #sau 0,5s thì mới có thể ăn dmg lần nữa
        self.dust_canmove_vertical_timer = Timer(3000, func = create_dust, repeat = True, autostart = True)
        self.dust_canmove_vertical_timer.activate()

    def re_map(self, name):
        self.data = []
        self.clear()
        map = load_pygame(join('data', 'tmx', f'map{name}.tmx'))
        with open(f"data_map{name}.json", "r") as file:
            self.data = json.load(file)

        self.dust_vertical_up_positions = []
        self.dust_vertical_down_positions = []
        for x, y, image in map.get_layer_by_name('Decorate').tiles():  # trang trí
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE  * SCALE_FACTOR), scaled_image, (self.all_sprites))
        for x, y, image in map.get_layer_by_name('Background').tiles():
            # Phóng to hình ảnh
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE * SCALE_FACTOR), scaled_image, self.all_sprites)  #sprite_bg ->all_sprite
        for x, y, image in map.get_layer_by_name('Decorate2').tiles():  # trang trí         
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE  * SCALE_FACTOR), scaled_image, self.all_sprites)
        for x, y, image in map.get_layer_by_name('Finish').tiles():
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE * SCALE_FACTOR), scaled_image,  (self.finish, self.all_sprites))
        
        for obj in map.get_layer_by_name('Object'):    
            if obj.name == 'Player':
                x = obj.x * SCALE_FACTOR 
                y = obj.y * SCALE_FACTOR 
                for i in self.data:
                    if i['name'] == 'Checkpoint':
                        x = i['x']
                        y = i['y']
                    if i['name'] == 'Player':
                        self.score = i['h'] 
                        self.player = Player((x, y), (self.all_sprites, self.player_sprites), self.collision_sprites, self. player_frames, self.jump_audio, self.attack_audio, self.death_audio, i['hp'])
                        self.data.remove(i)
                        break
            if obj.name == 'Enermy_2':
                for i in self.data:
                    if i['name'] =='Enermy_2':
                        rect = pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR)
                        if rect.collidepoint(i['x'], i['y']):
                            state = [i['x'],i['y'], i['hp']]
                            Enermy_2(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.enermy2_frames,(self.enermy_vip_sprites, self.all_sprites), self.player_sprites,state)
                            self.data.remove(i)
                            break
            if obj.name == 'Checkpoint':
                Checkpoint((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.checkpoint_frames, (self.all_sprites, self.checkpoint_sprites), self.active_audio)
            if obj.name == 'Spike':
                scaled_image = pygame.transform.scale(obj.image, (obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
                Spike((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), scaled_image, (self.all_sprites, self.trap_sprites))
            if obj.name == 'Coin':
                for i in self.data:
                    if i['name'] =='Coin':
                        Coin((i['x'], i['y']), self.coin_frames, (self.coin_sprites, self.all_sprites))
                        self.data.remove(i)
                        break
            if obj.name == 'Saw_1.1':
                Saw_1_1(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.saw_frames,(self.trap_sprites, self.all_sprites), -1 , "bottom") #1 khu vực Skeleton có thể di chuyển 
            if obj.name == 'Saw_1.2':
                Saw_1_2(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.saw_frames,(self.trap_sprites, self.all_sprites), -1 , "right")
            if obj.name == 'Platform_horizontal':
                Dust_canmove_horizontal(pygame.Rect(obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR), self.platform_frames, (self.all_sprites, self.collision_sprites), 1, "left")
            if obj.name == "Platform_vertical":
                image_obj = pygame.Surface((100, 20))
                Dust_canmove_vertical(pygame.Rect(obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR), self.platform_frames, (self.all_sprites, self.collision_sprites), "return", 1, "top")
            if obj.name == 'Platform_vertical_up':
                self.dust_vertical_up_positions.append((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
            if obj.name == 'Platform_vertical_down':
                self.dust_vertical_down_positions.append((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
        
        for obj in map.get_layer_by_name('Dust'):        
            scaled_image = pygame.transform.scale(obj.image, (obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
            Sprites((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), scaled_image, (self.all_sprites, self.collision_sprites))   #sprite_collision -> collision_sprite
        for i in self.data:
            if i['name'] == 'Checkpoint':
                for checkpoint in self.checkpoint_sprites:
                    if checkpoint.rect.x == i['x']:
                        checkpoint.active = True
                        checkpoint.activate(self.player)
                        self.data.remove(i)
                        break
                     
        def create_dust():
            for position in self.dust_vertical_up_positions:
                Dust_canmove_vertical(pygame.Rect(position), self.platform_frames, (self.all_sprites, self.collision_sprites), "loop", -1, "bottom")
            for position in self.dust_vertical_down_positions:
                Dust_canmove_vertical(pygame.Rect(position), self.platform_frames, (self.all_sprites, self.collision_sprites), "loop", 1, "top")
        #cooldown
        self.cooldown_hp = Timer(500)   #sau 0,5s thì mới có thể ăn dmg lần nữa
        self.dust_canmove_vertical_timer = Timer(3000, func = create_dust, repeat = True, autostart = True)
        self.dust_canmove_vertical_timer.activate()

    def save_map(self, name):
        for enermy in self.enermy_vip_sprites:
            self.save.obj_save(enermy.hitbox_rect.x, enermy.hitbox_rect.y,enermy.hitbox_rect.width, enermy.hitbox_rect.height,'Enermy_2',enermy.enermy_hp,1)
        for coin in self.coin_sprites:
            self.save.obj_save(coin.rect.x, coin.rect.y, 10,10, 'Coin', 10, 1)
        for checkpoint in self.checkpoint_sprites:
            if checkpoint.active == True:
                self.save.obj_save(checkpoint.rect.x, checkpoint.rect.y, 10,10,'Checkpoint',10,1)
        self.save.obj_save(self.player.hitbox_rect.x,self.player.hitbox_rect.y-50,10,self.score,'Player',self.player.hp,1)
        self.save.save_to_file(name)
    
    def check_finish(self):
        for i in self.finish:
            if self.player.hitbox_rect.colliderect(i) and self.score >= 7:
                return 1

    def check_player_collision(self):
        #check checkpoint
        for checkpoint in self.checkpoint_sprites:  
            if not checkpoint.active:
                if self.player.hitbox_rect.colliderect(checkpoint.rect):
                    for other_checkpoint in self.checkpoint_sprites:
                        other_checkpoint.active = False           
                    checkpoint.activate(self.player)
                break
        #check coin 
        for coin in self.coin_sprites:
            if self.player.hitbox_rect.colliderect(coin.rect):
                coin.destroy()
                self.coin_audio.play()
                self.score += 1
        #check player với quái 
        for enermy in self.enermy_vip_sprites:
            if self.player.hitbox_attack.colliderect(enermy.hitbox_rect) and self.player.get_attack_frame() == 4:
                if self.cooldown_hp.active == False:
                    enermy.enermy_hp -= 1
                    self.damage_audio.play()
                    self.cooldown_hp.activate()
                    enermy.is_hurt = True
                    if enermy.enermy_hp == 0:
                        enermy.is_death = True
                        self.score += 2
                        break
            self.cooldown_hp.update()     
        #check quái với player
        for enermy in self.enermy_vip_sprites:
            if self.player.hitbox_rect.colliderect(enermy.hitbox_attack) and enermy.get_attack_frame() == 3:
                if self.cooldown_hp.active == False:
                    self.player.hp -= 1
                    self.damage_audio.play()
                    self.cooldown_hp.activate()
                    if self.player.hp == 0:
                        break
                    self.player.is_hurt = True
            self.cooldown_hp.update()
        #quái thường, cưa
        for trap in self.trap_sprites:
            if self.player.hitbox_rect.colliderect(trap.hitbox_rect):
                self.player.hp = 0
                break
        # chết, hồi sinh
        if self.player.hp <= 0:
            self.player.die()
    
    def clear(self):
        self.all_sprites.empty()
        self.collision_sprites.empty()
        self.trap_sprites.empty()
        self.enermy_vip_sprites.empty()
        self.player_sprites.empty()
        self.coin_sprites.empty()
        self.checkpoint_sprites.empty()
        self.finish.empty() 

    def run(self, name):
        next = 0
        running = True
        self.bg_music.play(-1)
        while running:
            #datatime
            dt = self.clock.tick(FRAMRATE) / 1000
            #event loop
            if self.check_finish() == 1:
                running = False
                next = 3
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_rect.collidepoint(event.pos):
                        running = False   
                        next = 2 
                        self.menu_bg_music.play()
                        
            #update
            self.dust_canmove_vertical_timer.update()
            self.all_sprites.update(dt)
            self.check_player_collision()

            #draw
            self.display_surface.fill(BACKGROUND_COLOR)
            self.all_sprites.draw(self.player.hitbox_rect.center)
          

            for enermy in self.enermy_vip_sprites:
                self.menu.hp(enermy.hitbox_rect.x,enermy.hitbox_rect.y,enermy.hitbox_rect.width,enermy.hitbox_rect.height,5,3,enermy.enermy_hp)
            score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            hp_surface = self.font.render(f'HP:', True, (255, 255, 255))
            text1_surface = self.font.render("Kill 1 = 2 Score", True, (255, 255, 255))
            text2_surface = self.font.render("(Min 7)", True, (255, 255, 255))
            self.display_surface.blit(score_surface, (10, 10))
            self.display_surface.blit(hp_surface, (10,40))
            self.display_surface.blit(text1_surface, (10, 70))
            self.display_surface.blit(text2_surface, (130, 10))
            self.menu.hp_player(53,40)
            self.display_surface.blit(self.back_button,(WINDOW_WIDTH-100,20))

            pygame.display.update()
        self.bg_music.stop()

        if next != 3:
            self.save_map(name)
        if next == 3:
            self.lvl = name
            if os.path.exists(f"data_map{name}.json"):
                os.remove(f"data_map{name}.json")
        self.clear()
        return next 
    
    def run_menu(self):
        state = 1
        restart = 0
        self.menu_bg_music = pygame.mixer.Sound(join('audio', 'menu_music.ogg'))
        self.menu_bg_music.set_volume(0.6)
        self.menu_bg_music.play()
        while state != 0:
            # chay render
            if state == 1:
                state = self.menu.render()
            # chay renderlist
            if state == 2:
                state = self.menu.render_list()
            # chay finish
            if state == 3:
                self.menu_bg_music = pygame.mixer.Sound(join('audio', 'menu_music.ogg'))
                self.menu_bg_music.set_volume(0.6)
                self.menu_bg_music.play()
                state = self.menu.finish(self.score, "Nice",self.lvl)
            # chay map
            if state == 11 or state == 12 or state == 13:
                if os.path.exists(f"data_map{state}.json"):
                    restart = self.menu.note(state)
                    if restart == 1:
                        self.__init__()
                        self.re_map(state)
                        self.menu_bg_music.stop()
                        state = self.run(state)
                    if restart == 0:
                        self.__init__()
                        self.setup(state)
                        self.menu_bg_music.stop()
                        state = self.run(state)
                    if restart == 3:
                        state = 2
                else:
                    self.__init__()
                    self.setup(state)
                    self.menu_bg_music.stop()
                    state = self.run(state)
        sys.exit()
   
if __name__ == '__main__': 
    game = Game()
    game.run_menu()
