from settings import *

class Timer:
    def __init__(self, duration, func = None, repeat = None, autostart = False):
        self.duration = duration
        self.start_time = 0
        self.active = False
        self.func = func
        self.repeat = repeat
        self.last = 0


        if autostart == True:
            self.activate()

    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()
    
    def deactivate(self):
        self.active = False
        self.start_time = 0
        if self.repeat == True:
            self.activate()
            
    def credust(self):
        cur = pygame.time.get_ticks()
        # print(cur -self.last)
        if cur - self.last >= self.duration:
            self.func()
            self.last = cur


    def update(self):
        if pygame.time.get_ticks() - self.start_time >=self.duration:
            if self.func and self.start_time != 0:
                self.func()
            self.deactivate()