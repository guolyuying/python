class beedoo:
    def __init__(self, name, size, material, franticness):
        self.name = name
        self.size = size
        self.material = material
        self.franticness = franticness

    def beeg(self):
        if self.size >2:
            return True
        else:
            return False
