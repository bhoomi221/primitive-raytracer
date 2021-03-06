from color import Color

class Material:
    ''' Material has color and properties that tell teh light how to react'''

    def __init__(self, color=Color.from_hex("#FFFFFF"), ambient = 0.05, diffuse=1.0, specular= 1.0):
        self.color = color
        self.ambient = ambient 
        self.diffuse = diffuse
        self.specular = specular

    def color_at(self, position):
        return self.color

