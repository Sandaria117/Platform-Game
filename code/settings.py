import pygame
from os.path import join  #os.path.join -> thêm "\" để tạo đường dẫn
from os import walk
from pytmx.util_pygame import load_pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 720
TITLE_SIZE = 64
FRAMRATE = 60
BACKGROUND_COLOR = 'black'
SCALE_FACTOR = 2