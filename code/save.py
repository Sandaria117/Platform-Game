from settings import *
from sprites import *
from groups import *
from support import * 
from menu import *
from save import *
import json

class Save:
    def __init__(self, main):
        pygame.init()
        self.a = None
        self.other = main
        self.data = []
    # tao 1 dictionary de luu du lieu
    def obj_save(self, x, y ,w, h,name, hp,state):
        item = {
            "x" : x,
            "y" : y,
            "w": w,
            "h": h,
            "name" : name,
            "hp": hp,
            "state" : state
        }
        self.data.append(item)
    # luu 1 arr gom nhieu dictionary
    def save_to_file(self, name):
        with open(f"data_map{name}.json", "w") as file:
            json.dump(self.data, file, indent=4)
        self.data = []
    
    

# save = Save()
# save.save_to_file()
# save.load_file()

        