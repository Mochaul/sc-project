class Ships:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def shot_by_enemy(self):
        self.size -= 1
        self.is_destroyed()

    def is_destroyed(self):
        if self.size == 0:
            return True
        return False

    def get_category(self):
        return self.name
    
    def get_size(self):
        return self.size