# Working in the console:

# Checking objects collection in the scene
D.objects # Output = <bpy_collection[3], BlendDataObjects>

# Accessing each object
D.objects[0] # Output = bpy.data.objects['Camera']

# Copying objects to a list
myObjects = list(bpy.data.objects)

print(myObjects) # bpy.data.objects['Camera'], bpy.data.objects['Cube'], bpy.data.objects['Light']

# Storing 'cube' for manipulation
myCube = myObjects['Cube']

print(myCube.delta.location) # vector((0.0, 0.0, 0.0))