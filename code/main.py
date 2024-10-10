from settings import *
from sprites import *
from groups import *
from support import * 
from timer import *

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
        self.enermy_sprites = pygame.sprite.Group()
        self.enermy_vip_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.coin_sprites = pygame.sprite.Group()
        self.checkpoint_sprites = pygame.sprite.Group()
        
        #import
        self.import_assets()
        self.setup() #import bên map vào
        
        #score, hp
        self.score = 0
        self.player_hp = 5
        self.font = pygame.font.Font(None, 36)  #tạo 1 font obj -> font in chữ ra màn

        #cooldown
        self.cooldown_hp = Timer(500)   #sau 0,5s thì mới có thể ăn dmg lần nữa
    
    def import_assets(self):
        self.player_frames = {
            'idle': import_folder64x64('images','player2','idle'),
            'walk': import_folder64x64('images','player2','walk'),
            'jump': import_folder64x64('images','player2','jump'),
            'attack': import_folder64x64('images','player2','attack'),
            'death': import_folder64x64('images','player2','death'),
            'hurt': import_folder64x64('images','player2','hurt')
        }
        self.skeleton_frames = {
            'walk': import_folder64x64('images','enermy','skeleton','walk'),    
            'attack': import_folder64x64('images','enermy','skeleton','attack'),
            'death': import_folder64x64('images','enermy','skeleton','death'),
            'hurt': import_folder64x64('images','enermy','skeleton','hurt'),
            'idle': import_folder64x64('images','enermy','skeleton','idle')
        }
        self.coin_frames = {
            'idle': import_folder32x32('images','accessory','coin', 'idle')
        }
        self.checkpoint_frames = {
            'idle': import_folder64x64('images','accessory','checkpoint', 'idle')
        }
        
    def setup(self):
        map = load_pygame(join('data', 'tmx', 'testmap6.tmx'))
        # Phóng to các tile của layer map
        for x, y, image in map.get_layer_by_name('Background').tiles():   # background
            # Phóng to hình ảnh
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE * SCALE_FACTOR), scaled_image, self.all_sprites)  #sprite_bg ->all_sprite

        for x, y, image in map.get_layer_by_name('Decorate').tiles():  # trang trí
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE  * SCALE_FACTOR), scaled_image, self.all_sprites)
        
        # Phóng to các đối tượng va chạm (objects) phải * 2 lên vì mình đang phóng to tất cả các hình ảnh lên gấp đôi, do đó tọa độ cũng phải x2
        for obj in map.get_layer_by_name('Dust'):        # đất để đứng
            scaled_image = pygame.transform.scale(obj.image, (obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
            Sprites((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), scaled_image, (self.all_sprites, self.collision_sprites))   #sprite_collision -> collision_sprite
        
        for obj in map.get_layer_by_name('Object'):               # thực thể
            if obj.name == 'Player':
                self.player = Player((obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR ), (self.all_sprites, self.player_sprites), self.collision_sprites, self. player_frames)
            if obj.name == 'Skeleton':
                Skeleton(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.skeleton_frames,(self.enermy_sprites, self.all_sprites), 50) #1 khu vực Skeleton có thể di chuyển 
            if obj.name == 'Coin':
                Coin((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.coin_frames, (self.coin_sprites, self.all_sprites))
            if obj.name == 'Skeleton1':
                Skeleton1(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.player_frames,(self.enermy_vip_sprites, self.all_sprites), self.player_sprites)
            if obj.name == 'Checkpoint':
                Checkpoint((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.checkpoint_frames, (self.all_sprites, self.checkpoint_sprites))


    def check_attack_collision(self):
        for checkpoint in self.checkpoint_sprites:  # List or group of checkpoints
            if self.player.hitbox_rect.colliderect(checkpoint.rect):
                checkpoint.activate(self.player)

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
                
        #coincard
        for coin in self.coin_sprites:
            if self.player.hitbox_rect.colliderect(coin.rect):
                coin.destroy()
                self.score += 1
        #quái đấm mình
        for enermy in self.enermy_vip_sprites:
            if self.player.hitbox_rect.colliderect(enermy.hitbox_attack) and enermy.get_attack_frame() == 4:
                if self.cooldown_hp.active == False:
                    self.player_hp -= 1
                    self.cooldown_hp.activate()
                    if self.player_hp == 0:
                        break
                    self.player.is_hurt = True
                    # if self.player_hp == 0:
                    #     self.player.die()
                    #     # self.player.is_death == True
                    #     self.player_hp = 5
            self.cooldown_hp.update()

        for enermy in self.enermy_sprites:
            if self.player.hitbox_rect.colliderect(enermy.rect):
                if self.cooldown_hp.active == False:
                    self.player_hp -= 1
                    self.cooldown_hp.activate()
                    if self.player_hp == 0:
                        self.player.is_death = True
                        break
            self.cooldown_hp.update()
        if self.player_hp == 0:
                    self.player.die()
                    # self.player.is_death == True
                    self.player_hp = 5 
        # sprite_collision = pygame.sprite.spritecollide(self.player, self.enermy_sprites, False, pygame.sprite.collide_mask)
        # if sprite_collision:
        #     #
        #     for sprite in sprite_collision:
        #         sprite.destroy()

    def run(self):
        while self.running:
            #datatime
            dt = self.clock.tick(FRAMRATE) / 1000
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            #update
            self.all_sprites.update(dt)
            self.check_attack_collision()
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
