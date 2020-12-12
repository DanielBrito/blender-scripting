import bpy

# selecting cube from the scene:
myObject = bpy.data.objects[1].data

# turning cube into a plane:
for i in range(len(myObject.vertices)):
	myObject.vertices[i].co.z = 1