from settings import *
from sprites import AnimatedSprite
# class Player(AnimatedSprite): # lớp pygame.sprite.Sprite để tạo các thuộc tính cơ bản cho 1 sprite
#     def __init__(self, pos, groups, collision_sprites, frames):
#         super().__init__(pos, frames, groups)    #super() ->gọi lớp cha, super().init ở đây là khi truyền vào init của player sẽ tạo các thuộc tính trong lớp cha là animated
        
#         #collision
#         self.collision_sprite = collision_sprites
        
#         #movement
#         self.direction = pygame.Vector2()
#         self.speed = 500
#         self.gravity = 50
#         self.can_jump = False
#         #animate
#         self.flip = False
        
#         #hitbox
#         self.hitbox_rect = self.rect.inflate(-30, -0)  #hitbox cho bé đi so với ảnh
#         self.hitbox_attack = pygame.Rect((0,0), (40, self.hitbox_rect.height)) 

#         #timer
#         self.attack_cooldown = Timer(1000)
#         self.attack = False

#     def input(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_q] and self.attack_cooldown.active == False:
#             self.attack = True
#             self.attack_cooldown.activate()
        
#         self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
#         if keys[pygame.K_RIGHT]:
#             self.flip = False
#         elif keys[pygame.K_LEFT]:
#             self.flip = True
#         if keys[pygame.K_UP] and self.can_jump:
#             self.direction.y = -20 
#         self.flip_hitbox_attack()   #cập nhật hướng hitbox

#     def move(self, dt):
#         #ngang 
#         self.hitbox_rect.x += self.direction.x * self.speed * dt      # hitox nhân vật di chuyển
#         self.collision('horizontal')                                  # truyền horizontal vào direction trong phương thức collision
#         #dọc
#         # self.can_jump = False
#         self.direction.y += self.gravity * dt
#         self.hitbox_rect.y += self.direction.y  
#         self.collision('vertical')
#         self.rect.center = self.hitbox_rect.center                    #cập nhật lại tâm của rect theo tâm của hitbox
    
#     def flip_hitbox_attack(self):
#         if self.flip:
#             self.hitbox_attack.midright = self.hitbox_rect.midleft
#         else: 
#             self.hitbox_attack.midleft = self.hitbox_rect.midright
    
#     def get_attack_frame(self):
#         #Trả về chỉ số frame của animation tấn công hiện tại ->mượt hơn
#         if self.current_state == 'attack':
#             return int(self.frame_index)
#         return -1

#     def animate(self, dt):
#         if self.attack:
#             self.set_state('attack')
#         elif self.direction.x == 0 and self.can_jump:  #Nhân vật đứng yên và có thể nhảy
#             self.set_state('idle')                   #self.set_state là phương thức của lớp cha ở AnimateSprite
#         elif self.direction.x and self.can_jump:
#             self.set_state('walk')
#         elif self.direction.y:
#             self.set_state('jump')
        
#         # Gọi hàm animate của lớp AnimatedSprite để cập nhật animation
#         super().animate(dt, flip = self.flip)
        
#     def check_floor(self):
#         #tạo 1 hình chữ nhật bé tý sát dưới hitbox nhân vật để kiểm tra xem có va chạm với nền không
#         bottom_rect = pygame.Rect((0,0), (self.hitbox_rect.width, 1))
#         bottom_rect.midtop = self.hitbox_rect.midbottom

#         level_rect = [sprite.rect for sprite in self.collision_sprite] #lấy cái khối va chạm được truyền vào 1 danh sách
#         if bottom_rect.collidelist(level_rect) >= 0:                   #collidelist: dùng để trả về chỉ số sprite đầu tiên va chạm với level_rect // 0 va chạm trả về -1
#             self.can_jump = True                                       #tức là đang trên floor
#         else: 
#             self.can_jump = False

#     def collision(self, direction):
#         for sprite in self.collision_sprite:
#             if sprite.rect.colliderect(self.hitbox_rect):
#                 if direction == 'horizontal':
#                     if self.direction.x > 0:
#                         self.hitbox_rect.right = sprite.rect.left
#                     if self.direction.x < 0: 
#                         self.hitbox_rect.left = sprite.rect.right
#                 else:
#                     if self.direction.y > 0:   
#                         self.hitbox_rect.bottom = sprite.rect.top
#                     if self.direction.y < 0: 
#                         self.hitbox_rect.top = sprite.rect.bottom  
#                     self.direction.y = 0   #va chạm ở trên -> vector chuyển động mất ngay -> trọng lực kéo xuống mượt


#     def update(self, dt):
#         self.attack_cooldown.update()
#         if self.attack_cooldown.active == False:
#             self.attack = False
#         self.check_floor()
#         self.input()
#         self.move(dt)
#         self.animate(dt)
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