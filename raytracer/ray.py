class Ray:
    ''' Ray is half a line with a normalized direction '''
    def __init__(self, origin, dir):
        self.dir = dir.normalize()
        self.origin = origin 
