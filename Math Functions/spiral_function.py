# This script creates a graph of a spiral function:

import bpy
import math

ob = bpy.data.objects["Cube"]

frame_number = 0

n = 80
r = 10
x = 0
const = 0

for i in range(0, 500):
    bpy.context.scene.frame_set(frame_number)
    
    angle = ((i-1)*4*math.pi)/n
    z = r*math.cos(angle)
    y = r*math.sin(angle)
    const += 0.3
    
    ob.location = (x, y+const, z-const)
    ob.keyframe_insert(data_path = "location", index = -1)
    
    frame_number += 1
    
    x += 0.4
    
    # ... Here, create xyz-axis and configure particle system manually ...