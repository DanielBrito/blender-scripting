# generates an object similar to a rubik's cube

import bpy

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cube_add()

bpy.ops.object.modifier_add(type="ARRAY")
bpy.data.objects[0].modifiers["Array"].count = 3
bpy.data.objects[0].modifiers["Array"].relative_offset_displace[0] = 1.1     # x-axis

bpy.ops.object.modifier_add(type="ARRAY")
bpy.data.objects[0].modifiers["Array.001"].count = 3
bpy.data.objects[0].modifiers["Array.001"].relative_offset_displace[0] = 0   # x-axis
bpy.data.objects[0].modifiers["Array.001"].relative_offset_displace[1] = 1.1 # y-axis

bpy.ops.object.modifier_add(type="ARRAY")
bpy.data.objects[0].modifiers["Array.002"].count = 3
bpy.data.objects[0].modifiers["Array.002"].relative_offset_displace[0] = 0   # x-axis
bpy.data.objects[0].modifiers["Array.002"].relative_offset_displace[1] = 0   # y-axis
bpy.data.objects[0].modifiers["Array.002"].relative_offset_displace[2] = 1.1 # z-axis

bpy.ops.object.select_all(action="DESELECT")