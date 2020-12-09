import bpy

# deletes all the objects from the scene:
def deleteAll():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()

# creates a line of cubes along the y-axis:
def formLooper(repeatValue):
    for i in range(repeatValue):
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.transform.translate(value=(0, i*2, 0))

deleteAll()
formLooper(10)