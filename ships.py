class ships:
    def __init__(self, category, size, position):
        self.category = category
        self.size = size
        self.position = position
    
    def isShot(self, coordinates):
        for i in self.position:
            if coordinates == i:
                #guess correctly
                i = "x"
                self.isDestroyed()
                return True
        return False

    def isDestroyed(self):
        for i in self.position:
            if i != "x":
                return False
        return True

    def getCategory(self):
        return self.category
    
    def getSize(self):
        return self.size

    def getPosition(self):
        return self.position