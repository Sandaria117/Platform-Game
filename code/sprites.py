from settings import *
from timer import *

class Sprites(pygame.sprite.Sprite):    #lớp vật thể chung
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

class AnimatedSprite(Sprites):
    def __init__(self, pos, frames, groups):
        # 'frames' ở đây là một dictionary với các key là các trạng thái ('idle', 'walk') và giá trị là danh sách các hình ảnh
        self.frames = frames
        self.frame_index = 0
        self.animation_speed = 5
        self.current_state = 'idle'  # Bắt đầu với trạng thái 'idle'
        # cờ kiểm tra trạng thái
        self.is_attacking = False
        self.is_death = False
        self.is_hurt = False
        # cờ kiểm tra loại đối tượng
        self.is_player = False
        self.is_enermy = False
        
        super().__init__(pos, self.frames[self.current_state][self.frame_index], groups)
    
    def animate(self, dt, flip):
        # Cập nhật chỉ số frame dựa trên thời gian và tốc độ animation
        self.frame_index += self.animation_speed * dt
        
        if self.frame_index >= len(self.frames[self.current_state]):
            self.frame_index = 0  # Lặp lại từ đầu khi hết ảnh
            # Kiểm tra các trạng thái kết thúc hoạt ảnh
            if self.current_state == 'hurt':
                self.is_hurt = False  # Dừng trạng thái 'hurt' khi hoạt ảnh kết thúc
            elif self.current_state == 'attack':
                self.is_attacking = False  # Dừng trạng thái 'attack'
            elif self.current_state == 'death':
                if self.is_player:
                        self.respawn()
                elif self.is_enermy:
                    self.kill()  # Có thể kill đối tượng khi 'death' kết thúc
                
        # Cập nhật ảnh hiện tại từ trạng thái hiện tại
        self.image = self.frames[self.current_state][int(self.frame_index)]
        if flip == True:
            self.image = pygame.transform.flip(self.image, True, False)

    def set_state(self, new_state): 
        # Đổi trạng thái animation
        if new_state != self.current_state:
            self.current_state = new_state
            self.frame_index = 0  # Reset lại frame index khi chuyển sang trạng thái mới
        if self.current_state == 'attack' or self.current_state == 'death' or self.current_state == 'jump':
            self.animation_speed = 10
        else:
            self.animation_speed = 5

class Enermy(AnimatedSprite):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames, groups)
        self.flip = False
        self.is_enermy = True

    def destroy(self):
        self.kill()

class Enermy_2(Enermy):
    def __init__(self, rect, frames , groups, player_sprite, trangthai):
        super().__init__(rect.topleft, frames, groups)
        self.enermy_hp = 3
        self.rect.bottomleft = rect.midbottom
        if trangthai[0] != 0 and trangthai[1] != 0:
            self.rect.x = trangthai[0]
            self.rect.y = trangthai[1]
            self.enermy_hp = trangthai[2]
        self.main_rect = rect   #hình chữ nhật giới hạn di chuyển
        self.hitbox_rect = self.rect.inflate(-10, -0)
        self.hitbox_attack = pygame.Rect((0,0), (50, self.hitbox_rect.height)) 
        self.speed = 100
        self.direction = 0
        self.follow = False
        self.is_enermy = True

        self.player_sprite = player_sprite

    def move(self, dt):
        if self.follow == True and self.is_attacking == False and self.is_hurt == False:
            self.rect.x += self.direction * self.speed * dt
        self.hitbox_rect.topleft = self.rect.topleft

    def animated(self, dt):
        if self.is_death == True:
            self.set_state('death')
        elif self.is_hurt == True:
            self.set_state('hurt')
            self.is_attacking = False
        elif self.follow == False and self.is_attacking == False and self.is_hurt == False:
        # elif self.direction == 0 and self.follow == False:          # nếu không thêm điều kiện sẽ
            self.set_state('idle')
        # elif self.direction != 0 and self.follow == True:
        elif self.follow == True and self.is_attacking == False and self.is_hurt == False:
            self.set_state('walk')
        for player in self.player_sprite:
            if player.hitbox_rect.colliderect(self.hitbox_rect) and player.is_death == False and self.is_hurt == False:
                self.follow = False
                self.is_attacking = True
                self.set_state('attack') 
            elif player.is_death == True: 
                    self.follow = False
            else: 
                if self.is_attacking == False:
                    self.follow = True
        super().animate(dt, flip=self.flip)
    
    def get_attack_frame(self):
        #Trả về chỉ số frame của animation tấn công hiện tại ->mượt hơn
        if self.current_state == 'attack':
            return int(self.frame_index)
        return -1

    def following(self):
        for player in self.player_sprite:
            if player.hitbox_rect.colliderect(self.main_rect):# and player.is_death == False:
                self.follow = True
                distance_x = player.rect.x - self.rect.x  # khoảng cách để không bị flip liên tục
                if abs(distance_x) > 15:
                    if player.rect.x > self.rect.x:
                        self.flip = False
                        self.direction = 1
                    else: 
                        self.flip = True
                        self.direction = -1
            else:
                self.follow = False
                # self.direction = 0

    def set_hitbox(self):
        if self.flip:
            self.hitbox_attack.midright = self.hitbox_rect.center
        else: 
            self.hitbox_attack.midleft = self.hitbox_rect.center

    def update(self, dt):
        self.following()
        self.set_hitbox()
        self.move(dt)
        self.animated(dt)

class Saw_1(Enermy):
    def __init__(self, rect, frames, groups, speed, direction, pos_start):
        self.main_rect = rect  
        self.pos_start = pos_start
        super().__init__(rect.topleft, frames, groups) 
        self.pos_end = pygame.Rect(0, 0, 1, 1)
        if self.pos_start == "bottom":
            self.rect.midbottom = self.main_rect.midbottom
            # self.pos_end.midtop = self.main_rect.midtop
        elif self.pos_start == "top":
            self.rect.midtop = self.main_rect.midtop
            # self.pos_end.midbottom = self.main_rect.midbottom
        elif self.pos_start == "left":
            self.rect.midleft = self.main_rect.midleft
        elif self.pos_start == "right":
            self.rect.midright = self.main_rect.midright                 
        self.speed = speed
        self.direction = direction
        self.hitbox_rect = self.rect.inflate(0, 0)

    def move(self, dt):
        if self.pos_start == "left" or self.pos_start == "right":
            self.rect.x += self.direction * self.speed * dt
        else:
            self.rect.y += self.direction * self.speed * dt
        self.hitbox_rect.topleft = self.rect.topleft

    def constraint(self):
        if self.pos_start == "left" or self.pos_start == "right":
            if self.rect.midleft < self.main_rect.midleft:
                self.direction *= -1
                self.flip = True
            if self.rect.midright > self.main_rect.midright:
                self.direction *= -1
                self.flip = False
        else:
            if self.rect.midtop < self.main_rect.midtop:
                self.direction *= -1
                self.flip = True
            if self.rect.midbottom > self.main_rect.midbottom:
                self.direction *= -1
                self.flip = False
            
    def update(self, dt):
        self.animation_speed = 20
        self.move(dt)
        self.constraint()
        self.animate(dt, flip = self.flip)

class Player(AnimatedSprite): # lớp pygame.sprite.Sprite để tạo các thuộc tính cơ bản cho 1 sprite
    def __init__(self, pos, groups, collision_sprites, frames, jump_audio, attack_audio, hp):
        super().__init__(pos, frames, groups)    #super() ->gọi lớp cha, super().init ở đây là khi truyền vào init của player sẽ tạo các thuộc tính trong lớp cha là animated
        #player
        self.is_player = True
        #collision
        self.collision_sprite = collision_sprites
        self.platform = None
        self.hp = hp
        #movement
        self.direction = pygame.Vector2()
        self.speed = 500
        self.gravity = 50
        self.can_jump = False
        #animate
        self.flip = False
        #respawn
        self.respawn_point = pos
        #hitbox
        self.hitbox_rect = self.rect.inflate(-30, -0)  #hitbox cho bé đi so với ảnh
        self.hitbox_attack = pygame.Rect((0,0), (20, self.hitbox_rect.height)) 
        #audio
        self.attack_audio = attack_audio
        self.jump_audio = jump_audio

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and self.is_attacking == False:
            self.is_attacking = True
            self.attack_audio.play()
        if self.can_jump:
            self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        else:
            self.direction.x = (int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])) * 0.75
        if keys[pygame.K_RIGHT]:
            self.flip = False
        elif keys[pygame.K_LEFT]:
            self.flip = True
        if keys[pygame.K_UP] and self.can_jump:
            self.direction.y = -18 
            self.jump_audio.play()
        self.set_hitbox()   #cập nhật hướng hitbox

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
    
    def set_hitbox(self):
        if self.flip:
            self.hitbox_attack.midright = self.hitbox_rect.midleft
        else: 
            self.hitbox_attack.midleft = self.hitbox_rect.midright
    
    def get_attack_frame(self):
        #Trả về chỉ số frame của animation tấn công hiện tại ->mượt hơn
        if self.current_state == 'attack':
            return int(self.frame_index)
        return -1

    def animated(self, dt):
        if self.is_death:
            self.set_state('death')
        elif self.is_hurt == True:
            self.set_state('hurt')
            self.is_attacking = False   #bị ăn dmg thì ko đấm nữa 
        elif self.is_attacking == True:
            self.set_state('attack')
        elif self.can_jump == False:
            self.set_state('jump')
        elif self.direction.x == 0 and self.can_jump:  #Nhân vật đứng yên và có thể nhảy
            self.set_state('idle')                   #self.set_state là phương thức của lớp cha ở AnimateSprite
        elif self.direction.x and self.can_jump:
            self.set_state('walk')
        
        # Gọi hàm animate của lớp AnimatedSprite để cập nhật animation
        super().animate(dt, flip = self.flip)
        
    def move_along_the_platform(self, dt):
        if self.platform:
            self.hitbox_rect.x += self.platform.direction_x * self.platform.speed * dt
            self.hitbox_rect.y += self.platform.direction_y * self.platform.speed * dt

    def check_floor(self):
        #tạo 1 hình chữ nhật bé tý sát dưới hitbox nhân vật để kiểm tra xem có va chạm với nền không
        floor_rect = pygame.Rect((0,0), (self.hitbox_rect.width, 3))
        floor_rect.midtop = self.hitbox_rect.midbottom

        level_rect = [sprite.rect for sprite in self.collision_sprite] #lấy cái khối va chạm được truyền vào 1 danh sách
        if floor_rect.collidelist(level_rect) >= 0:                   #collidelist: dùng để trả về chỉ số sprite đầu tiên va chạm với level_rect // 0 va chạm trả về -1
            self.can_jump = True                                       #tức là đang trên floor
        else: 
            self.can_jump = False
        
        self.platform = None
        for sprite in [sprite for sprite in self.collision_sprite.sprites() if hasattr(sprite, "moving")]:
            if sprite.rect.colliderect(floor_rect):
                self.platform = sprite
                
    def collision(self, direction):
        for sprite in self.collision_sprite:
            if sprite.rect.colliderect(self.hitbox_rect):
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

    def die(self):
        self.is_death = True
    
    def respawn(self):
        self.hitbox_rect.center = self.respawn_point
        self.is_death = False
        self.hp = 5

    def update(self, dt):
        if self.is_death == False:
            self.input()
            self.check_floor()
            self.move_along_the_platform(dt)
            self.move(dt)

        self.animated(dt)

class Coin(AnimatedSprite):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames, groups)

    def destroy(self):
        self.kill()
    
    def update(self, dt):
        self.animation_speed = 10
        self.animate(dt, False)

class Checkpoint(AnimatedSprite):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames, groups)
        self.active = False

    def activate(self, player):
        self.active = True
        player.respawn_point = self.rect.center

    def update(self, dt):
        self.animation_speed = 20
        if self.active:
            self.animate(dt, False)    #checkpoint nào gần nhất mới có animation
        
class Dust_canmove_horizontal(AnimatedSprite):
    # self.pos
    def __init__(self, rect, frames, groups, direction, pos_start):
        self.main_rect = rect 
        super().__init__(rect.topleft, frames, groups)
        self.pos_end = pygame.Rect(0, 0, 1, 1)
        if pos_start == "left":
            self.rect.midleft = self.main_rect.midleft
            # self.pos_end.midright = self.main_rect.midright
        elif pos_start == "right":
            self.rect.midright = self.main_rect.midright
            # self.pos_end.midleft = self.main_rect.midleft
        self.flip = False 
        self.direction_x = direction
        self.direction_y = 0
        self.speed = 100
        self.moving = True

    def move(self, dt):
        self.rect.x += self.direction_x * self.speed * dt

    def check_flip(self):
        if self.rect.left < self.main_rect.left:
            self.direction_x *= -1
        if self.rect.right > self.main_rect.right:
            self.direction_x *= -1

    def update(self, dt):
        self.animation_speed = 20
        self.move(dt)
        self.animate(dt, False)
        self.check_flip()

class Dust_canmove_vertical(AnimatedSprite):
    def __init__(self, rect, frames, groups , func, direction, pos_start):
        super().__init__(rect.topleft, frames, groups)
        self.main_rect = rect
        # self.rect.midbottom = self.main_rect.midbottom
        self.pos_end = pygame.Rect(0, 0, 1, 1)
        if pos_start == "bottom":
            self.rect.midbottom = self.main_rect.midbottom
            self.pos_end.topleft = self.main_rect.midtop
        elif pos_start == "top":
            self.rect.midtop = self.main_rect.midtop
            self.pos_end.topleft = self.main_rect.midbottom
        self.flip = False
        self.direction_y = direction
        self.direction_x = 0
        self.speed = 100
        self.moving = True
        self.func = func
    
    def check_flip(self):
        if self.rect.midbottom > self.main_rect.midbottom:
            self.direction_y *= -1
        elif self.rect.midtop < self.main_rect.midtop:
            self.direction_y *= -1

    def destroy(self):
        if self.direction_y == 1 and self.rect.midbottom > self.pos_end.midbottom:
            self.kill()
        if self.direction_y == -1 and self.rect.midtop < self.pos_end.midtop:
            self.kill()
        
    def move(self,dt):
        self.rect.y += self.direction_y * self.speed * dt
    
    def update(self, dt):
        self.move(dt)
        self.animation_speed = 20
        self.animate(dt, False)
        if self.func == "return":
            self.check_flip()
        elif self.func == "loop":
            self.destroy()
