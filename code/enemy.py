import random
from settings import * 
from time import sleep
from sprites import *
# class AnimatedSprite(Sprites):
#     def __init__(self, pos, frames, groups):
#         # 'frames' ở đây là một dictionary với các key là các trạng thái ('idle', 'walk') và giá trị là danh sách các hình ảnh
#         self.frames = frames
#         self.frame_index = 0
#         self.animation_speed = 5
#         self.current_state = 'idle'  # Bắt đầu với trạng thái 'idle'
#         super().__init__(pos, self.frames[self.current_state][self.frame_index], groups)
    
#     def animate(self, dt, flip):
#         # Cập nhật chỉ số frame dựa trên thời gian và tốc độ animation
#         self.frame_index += self.animation_speed * dt
#         if self.frame_index >= len(self.frames[self.current_state]):
#             self.frame_index = 0  # Lặp lại từ đầu khi hết ảnh
        
#         # Cập nhật ảnh hiện tại từ trạng thái hiện tại
#         self.image = self.frames[self.current_state][int(self.frame_index)]
#         if flip == True:
#             self.image = pygame.transform.flip(self.image, True, False)

#     def set_state(self, new_state): 
#         # Đổi trạng thái animation
#         if new_state != self.current_state:
#             self.current_state = new_state
#             self.frame_index = 0  # Reset lại frame index khi chuyển sang trạng thái mới
#         # chỉnh riêng cho speed attack
#         if self.current_state == 'attack':
#             self.animation_speed = 8.5
#         else:
#             self.animation_speed = 5
# class Enermy(AnimatedSprite):
#     def __init__(self, pos, frames, groups):
#         super().__init__(pos, frames, groups)
#         self.flip = False

#     def destroy(self):
#         self.kill()

# class Skeleton1(Enermy):
#     def __init__(self, rect, frames , groups, player_sprite):
#         super().__init__(rect.topleft, frames, groups)
#         self.rect.bottomleft = rect.bottomleft
#         self.main_rect = rect   #hình chữ nhật giới hạn di chuyển
#         self.hitbox_rect = pygame.Rect((0, 0), (40, 64))
#         self.speed = 50
#         self.direction = 0
#         self.follow = False

#         self.player_sprite = player_sprite

#     def move(self, dt):
#         if self.follow:
#             self.rect.x += self.direction * self.speed * dt

#     def animate(self, dt):
#         if self.direction == 0:
#             self.set_state('idle')
#         if self.direction != 0:
#             self.set_state('walk')
#         for player in self.player_sprite:
#             if player.hitbox_rect.colliderect(self.hitbox_rect):
#                 self.follow = False 
#                 self.set_state('attack')
#         super().animate(dt, flip = self.flip)
    
#     def following(self):
#         for player in self.player_sprite:
#             if player.hitbox_rect.colliderect(self.main_rect):
#                 self.follow = True
#                 if player.rect.x > self.rect.x:
#                     self.flip = False
#                     self.direction = 1
#                 else: 
#                     self.flip = True
#                     self.direction = -1
#             else:
#                 self.follow = False
#                 self.direction = 0

#     def set_hitbox(self):
#         if self.flip == False:
#             self.hitbox_rect.midleft = self.rect.midleft
#         else:
#             self.hitbox_rect.midright = self.rect.midright

#     def update(self, dt):
#         self.following()
#         self.set_hitbox()
#         self.animate(dt)
#         self.move(dt)

    #     self.is_idle=False
    #     # self.enemy_idle_sprite=[]
    #     # self.enemy_attack_sprite=[]
    #     # self.enemy_death_sprite=[]
    #     # self.enemy_hurt_sprite=[]
    #     # self.enemy_walk_sprite=[]
    #     # self.enemy_react_sprite=[]
    #     self.current_idle_image=0
    #     self.idle_image=self.enemy_idle_sprite[int(self.current_idle_image)].convert_alpha()
    #     self.pos=[0,0]
    #     self.health=10
    #     self.velocity=1
    #     self.rect = pygame.Rect(self.pos[0], self.pos[1], 64, 64)
    #     self.is_on_way=True
    #     self.direction=1
    #     self.x=float(self.rect.x)
    #     self.current_attack_image=0
    #     self.attack_image=self.enemy_attack_sprite[int(self.current_attack_image)].convert_alpha()
    #     self.current_walk_image=0
    #     self.walk_image=self.enemy_walk_sprite[int(self.current_walk_image)].convert_alpha()
    #     self.is_walking=True
    #     self.current_attack_image=0
    #     self.attack_image=self.enemy_attack_sprite[int(self.current_attack_image)].convert_alpha()
    #     self.is_attacking=False
    #     self.attack_area=pygame.Rect(self.rect.x//2,self.rect.y//2,48,70)
    #     self.enemy_area=pygame.Rect(0,0,0,0)
    #     self.current_hit_image=0
    #     self.hit_image=self.enemy_hurt_sprite[int(self.current_hit_image)].convert_alpha()
    #     self.is_hit = False
    #     self.dam=1
    #     self.health=1000
    #     self.is_death=False
    #     self.current_death_image=0
    #     self.death_image=self.enemy_death_sprite[int(self.current_death_image)].convert_alpha()
    #     self.end_animation=False
    #     self.offset=pygame.Vector2()
    #     self.enemy_area=pygame.Rect(obj.x*SCALE_FACTOR , obj.y*SCALE_FACTOR, obj.width*SCALE_FACTOR, obj.height*SCALE_FACTOR)
    # def update(self,interval):
     
    #     if not self.end_animation:
    #      if self.is_death:
    #          self.current_death_image+=0.1
    #          if self.current_death_image<len(self.enemy_death_sprite):
    #              self.death_image = self.enemy_death_sprite[int(self.current_death_image)].convert_alpha()
    #          else:
    #              self.is_death=False
    #              self.current_death_image = 0
    #              self.end_animation=True
    #      if self.is_hit:
    #          self.current_hit_image+=0.1
    #          if self.current_hit_image>=len(self.enemy_hurt_sprite):
    #             self.current_hit_image=0
    #          self.hit_image=self.enemy_hurt_sprite[int(self.current_hit_image)].convert_alpha()
    #      if self.is_idle:
    #         self.current_idle_image+= interval
    #         if self.current_idle_image>len(self.enemy_idle_sprite):
    #            self.current_idle_image=0
    #         self.idle_image = self.enemy_idle_sprite[int(self.current_idle_image)].convert_alpha()
    #      if self.is_walking:
    #          self.current_walk_image+=interval
    #          if self.current_walk_image>len(self.enemy_walk_sprite):
    #             self.current_walk_image=0
    #          self.walk_image = self.enemy_walk_sprite[int(self.current_walk_image)].convert_alpha()
    #      if self.is_attacking:
    #          self.current_attack_image+=interval
    #          if self.current_attack_image>len(self.enemy_attack_sprite):
    #             self.current_attack_image=0
    #          self.attack_image = self.enemy_attack_sprite[int(self.current_attack_image)].convert_alpha()
    #      self.attack_area = pygame.Rect(self.rect.x // 2, self.rect.y // 2, 32, 70)
    #      self.attack_area.center=self.rect.center
    # def set_pos(self,target_pos,WINDOW_WIDTH,WINDOW_HEIGHT):
    #     # self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2) 
    #     # self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)
    #     self.pos[0]=self.enemy_area.x
    #     self.pos[1]=self.enemy_area.y+20
    #     # self.pos[1]+=self.offset.y
    #     # self.pos[0]+=self.offset.x
    #     self.rect = pygame.Rect(self.pos[0], self.pos[1], 64, 70)
    #     self.x=float(self.rect.x)
    # def blit_enemy(self,target_pos,WINDOW_WIDTH,WINDOW_HEIGHT):
    #     if not self.end_animation:
    #      self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2) 
    #      self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)
    #      if self.direction<0:
    #          self.walk_image=pygame.transform.flip(self.walk_image,True,False)
    #          self.idle_image=pygame.transform.flip(self.idle_image,True,False)
    #          self.attack_image=pygame.transform.flip(self.attack_image,True,False)
    #          self.hit_image=pygame.transform.flip(self.hit_image,True,False)
    #          self.death_image=pygame.transform.flip(self.death_image,True,False)
    #      if self.is_idle and not self.is_walking and not self.is_attacking and not self.is_hit and not self.is_death:
    #          self.idle_image.set_colorkey((0,230,230))
    #          self.idle_image=pygame.transform.scale(self.idle_image, (64, 64))
    #          self.screen.blit(self.idle_image, (self.rect.x+self.offset.x,self.rect.y+self.offset.y))
    #      if self.is_walking and not self.is_attacking and not self.is_hit and not self.is_death:
    #          self.walk_image.set_colorkey((0,230,230))
    #          self.walk_image=pygame.transform.scale(self.walk_image,(48,64))
    #          self.screen.blit(self.walk_image,(self.rect.x+self.offset.x,self.rect.y+self.offset.y))
    #      if self.is_attacking and not self.is_hit and not self.is_death:
    #          self.attack_image.set_colorkey((0,230,230))
    #          self.attack_image=pygame.transform.scale(self.attack_image,(80,80))
    #          self.screen.blit(self.attack_image, (self.rect.x+self.offset.x,self.rect.y+self.offset.y-16))
    #      if self.is_death and not self.is_hit:
    #          self.death_image.set_colorkey((0,230,230))
    #          self.death_image=pygame.transform.scale(self.death_image,(48,64))
    #          self.screen.blit(self.death_image, (self.rect.x+self.offset.x,self.rect.y+self.offset.y))
    #      if self.is_hit:
    #          self.hit_image.set_colorkey((0,230,230))
    #          self.hit_image=pygame.transform.scale(self.hit_image,(48,64))
    #          self.screen.blit(self.hit_image, (self.rect.x+self.offset.x,self.rect.y+self.offset.y))
    # def move_set(self):
    #     if  not self.is_on_way:
    #         self.rect.y+=10
    #     if self.is_walking and not self.is_attacking and not self.is_hit and not self.is_death:
    #        self.x+=self.velocity*self.direction
    #        self.rect.x=self.x
    # def change_direction(self):
    #     if self.rect.right<self.enemy_area.left+20 or self.rect.left>self.enemy_area.right-20:
    #         self.is_idle=True
    #         self.direction*=-1
    # def attack(self,char):
    #     if self.attack_area.colliderect(char.hitbox_rect) and not self.is_hit and not self.is_death:
    #         self.is_attacking=True
    #         self.rect.height=86
    #     else:
    #         self.is_attacking=False
    #         self.rect.y=self.pos[1]
    #         self.rect.height=70
    # def hit(self,char):
    #     if self.rect.colliderect(char.hitbox_rect) and char.attack and not self.is_death:
    #         self.is_walking=False
    #         self.is_hit=True
    #     # self.health-=char.dam
    #     else:
    #         self.is_hit=False
    #         self.is_walking=True
    # def death(self):
    #     if self.health==0:
    #         self.is_death=True
    #         self.is_hit=False
    # # def set_enemy_area(self,obj,SCALE_FACTOR):
       