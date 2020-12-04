# creating a set of objects inside a given scope:

import bpy
from random import randint

number = 200

for i in range(0, number):

		# scope dimension:
    x = randint(-5, 5)
    y = randint(-5, 5)
    z = randint(-5, 5)
    
    bpy.ops.mesh.primitive_cube_add(location=(x, y, z))