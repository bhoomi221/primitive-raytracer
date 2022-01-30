class Scene:
    ''' scene has all the information needed for the ray tracing engine'''
    def __init__(self, cam, objs, lights, w, h):
        self.cam = cam 
        self.objs = objs 
        self.lights = lights
        self.w = w
        self.h = h 
