#!/usr/bin/env python

from image import Image 
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from engine import RenderEngine
from light import Light
from material import Material


def main():
    WIDTH = 320
    HEIGHT = 200
    camera = Vector(0, 0, -1)
    objects = [Sphere(Point(0, -0.25, 0), 0.1, Material(Color.from_hex("#00FF00"))), Sphere(Point(-0.3, 0, -0.5), 0.1, Material(Color.from_hex("#bd00ff"))), Sphere(Point(-0.3, 0, 2), 0.7, Material(Color.from_hex("#000FF0"))) ]
    lights = [Light(Point(-1.5, 0, -10), Color.from_hex("#FFFFFF"))]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
    engine = RenderEngine()
    image = engine.render(scene)

    
    with open("test.ppm", 'w') as img_file:
        image.write_ppm(img_file)





if __name__ == "__main__":
    main()