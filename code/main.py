from settings import *
from sprites import *
from groups import *
from support import * 

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
        self.coin_sprites = pygame.sprite.Group()
        # self.player_attack_sprites = pygame.sprite.Group()
        
        #import
        self.import_assets()
        self.setup() #import bên map vào
        
        #score
        self.score = 0
        self.font = pygame.font.Font(None, 36)  #tạo 1 font obj -> font in chữ ra màn

    
    def import_assets(self):
        self.player_frames = {
            'idle': import_folder64x64('images','player2','idle'),
            'walk': import_folder64x64('images','player2','walk'),
            'jump': import_folder64x64('images','player2','jump'),
            'attack': import_folder64x64('images','player2','attack')
        }
        self.enermy_frames = {
            'idle': import_folder64x64('images','enermy','Skeletonwalk','Skeletonwalk')
        }
        self.coin_frames ={
            'idle': import_folder32x32('images', 'coin', 'idle')
        }
        
    def setup(self):
        map = load_pygame(join('data', 'tmx', 'testmap6.tmx'))
        # Phóng to các tile của layer map
        for x, y, image in map.get_layer_by_name('Tile Layer 1').tiles():   # background
            # Phóng to hình ảnh
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE * SCALE_FACTOR), scaled_image, self.all_sprites)  #sprite_bg ->all_sprite

        for x, y, image in map.get_layer_by_name('Tile Layer 2').tiles():  # trang trí
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE * SCALE_FACTOR), scaled_image, self.all_sprites)
        
        # Phóng to các đối tượng va chạm (objects) phải * 2 lên vì mình đang phóng to tất cả các hình ảnh lên gấp đôi, do đó tọa độ cũng phải x2
        for obj in map.get_layer_by_name('Object Layer 1'):        # đất để đứng
            scaled_image = pygame.transform.scale(obj.image, (obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
            Sprites((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), scaled_image, (self.all_sprites, self.collision_sprites))   #sprite_collision -> collision_sprite
        
        for obj in map.get_layer_by_name('Can move'):               # vật có thể di chuy
            if obj.name == 'Player':
                self.player = Player((obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR ), self.all_sprites, self.collision_sprites, self. player_frames)
            if obj.name == 'Skeleton':
                Skeleton(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.enermy_frames,(self.enermy_sprites, self.all_sprites), 50) #1 khu vực Skeleton có thể di chuyển 
            if obj.name == 'Coin':
                Coin((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.coin_frames, (self.coin_sprites, self.all_sprites))

    def check_attack_collision(self):
        if self.player.get_attack_frame() == 4:
            for enermy in self.enermy_sprites:
                if self.player.hitbox_attack.colliderect(enermy.rect):
                    enermy.destroy()
        
        for coin in self.coin_sprites:
            if self.player.hitbox_rect.colliderect(coin.rect):
                coin.destroy()
                self.score += 1
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
            #render
            score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
            self.display_surface.blit(score_surface, (10, 10))
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__': #không cho file khác import được hàm này
    game = Game()
    game.run()
