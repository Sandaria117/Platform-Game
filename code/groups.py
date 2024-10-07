from settings import *;

class AllSprite(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface() #lấy bề mặt hiện tại, hiển thị ra màn hình
        self.offset = pygame.Vector2()
        
    def draw(self, target_pos):
        #tịnh tiến tất cả các sprite tọa độ, tâm màn hình từ ở chính giữa map -> tâm là player
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2) 
        self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)
        for sprite in self:
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset) # đặt sprite.image vào vị trí sprite.rect lên màn hình hiển thị