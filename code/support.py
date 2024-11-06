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