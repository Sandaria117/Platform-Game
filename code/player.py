from settings import *
from sprites import AnimatedSprite

class Player(AnimatedSprite): # lớp pygame.sprite.Sprite để tạo các thuộc tính cơ bản cho 1 sprite
    def __init__(self, pos, groups, collision_sprites, frames):
        super().__init__(frames, pos, groups)    #thêm đối tượng Player vào group được truyền vào//super để gọi phương thức của lớp cha là pygame.sprite.Sprite
        
        #movement
        self.direction = pygame.Vector2()
        self.speed = 500
        self.gravity = 50
        self.collision_sprite = collision_sprites

        #animation
        # self.player_idle = []
        # self.player_idle.append(pygame.transform.scale(pygame.image.load(join('images','player2','idle','idle1.png')),(64,64)))
        
        self.current_idle = 0
        self.current_jump = 0
        self.image = self.player_idle[self.current_idle].convert_alpha()
        # self.image = self.player_jump[self.current_jump].convert_alpha()
        
        self.rect = self.image.get_rect(center = pos)
        self.hitbox_rect = self.rect.inflate(-0, -0)  #hitbox cho bé đi so với ảnh 
        

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        if keys[pygame.K_UP] and self.can_jump:
            self.direction.y = -20 
        # self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        # self.direction = self.direction.normalize() if self.direction else self.direction  #chuẩn hóa vector về đơn vị độ dài bằng 1, giữ nguyên hướng -> đi chéo không cấn

    def move(self, dt):
        #ngang 
        self.hitbox_rect.x += self.direction.x * self.speed * dt      # hitox nhân vật di chuyển
        self.collision('horizontal')                                  # truyền horizontal vào direction trong phương thức collision
        #dọc
        # self.can_jump = False
        self.direction.y += self.gravity * dt
        self.hitbox_rect.y += self.direction.y  
        self.collision('vertical')
        self.rect.center = self.hitbox_rect.center                    #cập nhật lại tâm của rect theo tâm của hitbox

    def check_floor(self):
        #tạo 1 hình chữ nhật bé tý sát dưới hitbox nhân vật để kiểm tra xem có va chạm với nền không
        bottom_rect = pygame.Rect((0,0), (self.rect.width, 2))
        bottom_rect.midtop = self.hitbox_rect.midbottom

        level_rect = [sprite.rect for sprite in self.collision_sprite] #lấy cái khối va chạm được truyền vào 1 danh sách
        if bottom_rect.collidelist(level_rect) >= 0:                   #collidelist: dùng để trả về chỉ số sprite đầu tiên va chạm với level_rect // 0 va chạm trả về -1
            self.can_jump = True                                       #tức là đang trên floor
        else: 
            self.can_jump = False

    def collision(self, direction):
        for sprite in self.collision_sprite:
            if sprite.rect.colliderect(self.hitbox_rect):
                # print("ýe")
                if direction == 'horizontal':
                    if self.direction.x > 0:
                        self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: 
                        self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y > 0:   
                        self.hitbox_rect.bottom = sprite.rect.top
                    if self.direction.y < 0: 
                        self.hitbox_rect.top = sprite.rect.bottom  
                    self.direction.y = 0   #va chạm ở trên -> vector chuyển động mất ngay -> trọng lực kéo xuống mượt

    def update(self, dt):

        self.check_floor()
        self.input()
        self.move(dt)