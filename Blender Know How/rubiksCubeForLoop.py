# generates an object similar to a rubik's cube

import bpy

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

for i in range(3):
	for j in range(3):
		for k in range(3):
			bpy.ops.mesh.primitive_cube_add(location=(-i*2.1, j*2.1, k*2.1))

bpy.ops.object.select_all(action="DESELECT")