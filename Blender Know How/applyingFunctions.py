import bpy

# deleting all the objects of the scene:
def deleteAll():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete()
    
# creating four legs:
def legs():
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.transform.resize(value=(.25, .25, 6.25))
    bpy.ops.transform.translate(value=(2, 0, 3))
    
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.transform.resize(value=(.25, .25, 6.25))
    bpy.ops.transform.translate(value=(-2, 0, 3))
    
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.transform.resize(value=(.25, .25, 3))
    bpy.ops.transform.translate(value=(2, 4, 0))
    
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.transform.resize(value=(.25, .25, 3))
    bpy.ops.transform.translate(value=(-2, 4, 0))

# creating seat:
def seat():
    bpy.ops.mesh.primitive_cube_add()
    bpy.ops.transform.resize(value=(2.25, 2.25, .25))
    bpy.ops.transform.translate(value=(0, 2, 3))

# creating back divisions:  
def back():
    for i in range (4, 10):
        bpy.ops.mesh.primitive_cube_add()
        bpy.ops.transform.resize(value=(2, .25, .25))
        bpy.ops.transform.translate(value=(0, 0, i))

# generating chair:
def chair():
    legs()
    seat()
    back()
    
deleteAll()
chair()