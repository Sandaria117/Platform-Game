from settings import *

def import_image(*path, alpha = True):
    full_path = join(*path) + ".png"
    return pygame.image.load(full_path).convert_alpha() if alpha else pygame.image.load(full_path).convert() 

def import_folder(*path, width = 64, height = 64):
    frames = []
    for folder_path, sub_folders, file_names in walk(join(*path)):
        for file_name in file_names:
            full_path = join(folder_path, file_name)
            image = pygame.image.load(full_path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (width, height))  # Sử dụng width và height
            frames.append(scaled_image)
    return frames

     # def run(self):
    #     while self.running:
    #         #datatime
    #         dt = self.clock.tick(FRAMRATE) / 1000
    #         #event loop
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 self.running = False
                        
    #         #update
    #         self.dust_canmove_vertical_timer.update()
    #         self.all_sprites.update(dt)
    #         self.check_player_collision()
    #         #draw
    #         self.display_surface.fill(BACKGROUND_COLOR)
    #         self.all_sprites.draw(self.player.hitbox_rect.center)
            
    #         score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
    #         hp_surface = self.font.render(f'Hp: {self.player.hp}', True, (255, 255, 255))
    #         self.display_surface.blit(score_surface, (10, 10))
    #         self.display_surface.blit(hp_surface, (10,50))
    #         pygame.display.update()
    #     pygame.quit()