# This script creates a graph of a sin function:

import bpy
import math

ob = bpy.data.objects["Cube"]

frame_number = 0

x = 0
y = 0
z = 0

for i in range(0, 500):
    bpy.context.scene.frame_set(frame_number)
    
    x += 0.3
    y += 0.1
    z -= 0.3
    
    ob.location = (-10+x, 30+20*math.sin(y), z)
    ob.keyframe_insert(data_path = "location", index = -1)
    
    frame_number += 1

    # ... Here, create xyz-axis and configure particle system manually before playing...