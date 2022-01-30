from image import Image 
from ray import Ray
from point import Point
from color import Color

class RenderEngine:
    ''' Redenders 3D objects into 2D using ray tracing'''
    def render(self, scene):
        width = scene.w
        height = scene.h 
        aspect_ratio = float(width)/float(height)
        x0 = -1.0
        x1 = 1.0
        xstep = (x1 - x0) / (width - 1)
        y0 = -1.0 / aspect_ratio
        y1 = 1.0 / aspect_ratio
        ystep= (y1 - y0) / (height - 1)

        camera = scene.cam 
        pixels = Image(width, height)

        for j in range(height):
            y = y0 + j *ystep 
            for i in range(width):
                x= x0 + i * xstep 
                ray = Ray(camera, Point(x,y) - camera)
                pixels.set_pixel(i, j, self.ray_trace(ray, scene))
        return pixels

    def ray_trace(self, ray, scene):
        color = Color(0, 0, 0)
        #Find the nearest object hit by the ray in the scene
        dist_hit, obj_hit = self.find_nearest(ray, scene)
        if obj_hit is None:
            return color
        hit_pos = ray.origin + ray.dir * dist_hit 
        hit_normal = obj_hit.normal(hit_pos)
        color += self.color_at(obj_hit, hit_pos, hit_normal, scene)
        return color

    def find_nearest(self, ray, scene):
        dist_min = None
        obj_hit= None
        for obj in scene.objs:
            dist = obj.intersects(ray)
            if dist is not None and (obj_hit is None or dist < dist_min):
                dist_min = dist 
                obj_hit= obj
        return (dist_min, obj_hit)

    def color_at(self, obj_hit, hit_pos, hit_normal, scene):
        material = obj_hit.material
        obj_col = material.color_at(hit_pos)
        to_cam = scene.cam - hit_pos 
        color = material.ambient * Color.from_hex("#000000")
        specular_k = 50
        #light calculations mostly needed if we have more than one light source 
        for light in scene.lights:
            to_light = Ray(hit_pos, light.position - hit_pos)
            #diffuse shading 
            color += (obj_col * material.diffuse * max(hit_normal.dot_product(to_light.dir), 0))
            #specular shading 
            half_vector = (to_light.dir + to_cam).normalize()
            color += light.color * material.specular * max(hit_normal.dot_product(half_vector), 0) ** specular_k
        return color 







