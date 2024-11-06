from settings import *
from sprites import *
from groups import *
from support import * 
from timer import *
from menu import *

class Game:
    def __init__(self):
        #setup
        pygame.init() #khởi tạo
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #bên setting
        pygame.display.set_caption("game test") #tiêu đề 
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
        self.player_hp = 5
        self.font = pygame.font.Font(None, 36)  #tạo 1 font obj -> font in chữ ra màn

        # dust
        # self.dust_surface = pygame.Surface((100, 20))
        self.dust_vertical_up_positions = []
        self.dust_vertical_down_positions = []

        #import
        self.import_assets()
        self.setup() #import bên map vào

        #cooldown
        self.cooldown_hp = Timer(500)   #sau 0,5s thì mới có thể ăn dmg lần nữa
        self.dust_canmove_vertical_timer = Timer(3000, func = self.create_dust, repeat = True, autostart = True)
        self.dust_canmove_vertical_timer.activate()
    
    def create_dust(self):
        for position in self.dust_vertical_up_positions:
            Dust_canmove_vertical(pygame.Rect(position), self.platform_frames, (self.all_sprites, self.collision_sprites), "loop", -1, "bottom")
        for position in self.dust_vertical_down_positions:
            Dust_canmove_vertical(pygame.Rect(position), self.platform_frames, (self.all_sprites, self.collision_sprites), "loop", 1, "top")
            
    def import_assets(self):
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
        
    def setup(self):
        map = load_pygame(join('data', 'tmx', 'testmap6.tmx'))
        # Phóng to các tile của layer map
        # Phóng to các đối tượng va chạm (objects) phải * 2 lên vì mình đang phóng to tất cả các hình ảnh lên gấp đôi, do đó tọa độ cũng phải x2
        
        # background
        for x, y, image in map.get_layer_by_name('Background').tiles():
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE * SCALE_FACTOR), scaled_image, self.all_sprites)  #sprite_bg ->all_sprite
        # trang trí   
        for x, y, image in map.get_layer_by_name('Decorate').tiles():  # trang trí         
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE  * SCALE_FACTOR), scaled_image, self.all_sprites)
        # thực thể
        for obj in map.get_layer_by_name('Object'):             
            
            if obj.name == 'Player':
                self.player = Player((obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR ), (self.all_sprites, self.player_sprites), self.collision_sprites, self. player_frames) 
            
            if obj.name == 'Saw_1.1':
                Saw_1(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.saw_frames,(self.trap_sprites, self.all_sprites), 150, -1 ,pos_start= "bottom") #1 khu vực Skeleton có thể di chuyển 
            if obj.name == 'Saw_1.2':
                Saw_1(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.saw_frames,(self.trap_sprites, self.all_sprites), 150, 1 ,pos_start= "left")

            if obj.name == 'Enermy_2':
                Enermy_2(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.enermy2_frames,(self.enermy_vip_sprites, self.all_sprites), self.player_sprites)
            
            if obj.name == 'Checkpoint':
                Checkpoint((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.checkpoint_frames, (self.all_sprites, self.checkpoint_sprites))
            
            if obj.name == 'Coin':
                Coin((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.coin_frames, (self.coin_sprites, self.all_sprites))
            
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

    def check_player_collision(self):
        #check checkpoint
        for checkpoint in self.checkpoint_sprites:  
            if self.player.hitbox_rect.colliderect(checkpoint.rect):
                for other_checkpoint in self.checkpoint_sprites:
                    other_checkpoint.active = False            # đặt tất cả các check point cũ không active,, chỉ active checkpoint mới nhất
                checkpoint.activate(self.player)
        
        #check coin 
        for coin in self.coin_sprites:
            if self.player.hitbox_rect.colliderect(coin.rect):
                coin.destroy()
                self.score += 1
        #check player với quái 
        for enermy in self.enermy_vip_sprites:
            if self.player.hitbox_attack.colliderect(enermy.hitbox_rect) and self.player.get_attack_frame() == 4:
                if self.cooldown_hp.active == False:
                    enermy.enermy_hp -= 1
                    self.cooldown_hp.activate()
                    enermy.is_hurt = True
                    if enermy.enermy_hp == 0:
                        enermy.is_death = True
                        break
            self.cooldown_hp.update()
                
        #check quái với player
        for enermy in self.enermy_vip_sprites:
            if self.player.hitbox_rect.colliderect(enermy.hitbox_attack) and enermy.get_attack_frame() == 3:
                if self.cooldown_hp.active == False:
                    self.player_hp -= 1
                    self.cooldown_hp.activate()
                    if self.player_hp == 0:
                        break
                    self.player.is_hurt = True
            self.cooldown_hp.update()
        #quái thường, cưa
        for trap in self.trap_sprites:
            if self.player.hitbox_rect.colliderect(trap.rect):
                self.player_hp = 0
                break

            self.cooldown_hp.update()
        # chết, hồi sinh
        if self.player_hp == 0:
            self.player.die()
            self.player_hp = 5 
      

    def run(self):
        while self.running:
            #datatime
            dt = self.clock.tick(FRAMRATE) / 1000
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                        
            #update
            self.dust_canmove_vertical_timer.update()
            self.all_sprites.update(dt)
            self.check_player_collision()
            #draw
            self.display_surface.fill(BACKGROUND_COLOR)
            self.all_sprites.draw(self.player.hitbox_rect.center)
            
            score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            hp_surface = self.font.render(f'Hp: {self.player_hp}', True, (255, 255, 255))
            self.display_surface.blit(score_surface, (10, 10))
            self.display_surface.blit(hp_surface, (10,50))
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__': #không cho file khác import được hàm này
    game = Game()
    game.run()
