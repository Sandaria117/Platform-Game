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

        self.import_assets()
        self.setup() #import bên map vào
        # self.enermy = Enermy((760, 1176),self.enermy_frames, self.all_sprites)
    
    def import_assets(self):
        self.player_frames = {
            'idle': import_folder('images','player2','idle'),
            'walk': import_folder('images','player2','walk'),
            'jump': import_folder('images','player2','jump'),
            'attack': import_folder('images','player2','attack')
        }
        self.enermy_frames = {
            'idle': import_folder('images','enermy','Skeletonwalk','Skeletonwalk')
        }
        
    def setup(self):
        map = load_pygame(join('data', 'tmx', 'testmap6.tmx'))
        # Phóng to các tile của layer map
        for x, y, image in map.get_layer_by_name('Tile Layer 1').tiles():
            # Phóng to hình ảnh
            scaled_image = pygame.transform.scale(image, (TITLE_SIZE * SCALE_FACTOR, TITLE_SIZE * SCALE_FACTOR))  
            Sprites((x * TITLE_SIZE * SCALE_FACTOR, y * TITLE_SIZE * SCALE_FACTOR), scaled_image, self.all_sprites)  #sprite_bg ->all_sprite

        # Phóng to các đối tượng va chạm (objects) phải * 2 lên vì mình đang phóng to tất cả các hình ảnh lên gấp đôi, do đó tọa độ cũng phải x2
        for obj in map.get_layer_by_name('Object Layer 1'):
            scaled_image = pygame.transform.scale(obj.image, (obj.width * SCALE_FACTOR, obj.height * SCALE_FACTOR))
            Sprites((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), scaled_image, (self.all_sprites, self.collision_sprites))   #sprite_collision -> collision_sprite
        for obj in map.get_layer_by_name('Can move'):
            if obj.name == 'Player':
                self.player = Player((obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR ), self.all_sprites, self.collision_sprites, self. player_frames)
            if obj.name == 'Skeleton':
                Skeleton(pygame.Rect(obj.x *SCALE_FACTOR , obj.y * SCALE_FACTOR, obj.width * SCALE_FACTOR, obj.height* SCALE_FACTOR), self.enermy_frames, self.all_sprites, 50) #1 khu vực Skeleton có thể di chuyển 
           
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
            #draw
            self.display_surface.fill(BACKGROUND_COLOR)
            self.all_sprites.draw(self.player.hitbox_rect.center)
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__': #không cho file khác import được hàm này
    game = Game()
    game.run()
