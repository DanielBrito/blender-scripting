import bpy

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

bpy.ops.mesh.primitive_plane_add()
bpy.ops.object.editmode_toggle()

bpy.ops.mesh.subdivide(number_cuts=10)