import bpy
import random
import math
import mathutils

path='content/data/rot_cub-'
cube_z_rot = 0
rad = math.radians(1)

scene = bpy.context.scene

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.resolution_x = 128
bpy.context.scene.render.resolution_y = 128
bpy.context.scene.render.resolution_percentage = 100


for i in range(0,1):
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    cube_z_rot = random.random() * rad * 360
    rot = (0, 0, random.random() * rad * 360)
    plane = bpy.ops.mesh.primitive_plane_add(size=500, view_align=False, enter_editmode=False, location=(0, 0, 0))

    bpy.ops.mesh.primitive_cube_add(size=2, view_align=False, enter_editmode=False, location=(0, 0, 1), rotation=rot)
    
    # Create the camera
    cam_data = bpy.data.cameras.new('camera')
    cam = bpy.data.objects.new('camera', cam_data)
    bpy.context.collection.objects.link(cam)
    scene.camera = cam
    # Create sun
    bpy.ops.object.light_add(type='SUN', radius=1, view_align=False, location=(0, 0, 10), rotation=(0, 30 * rad, 0))

    cam.location = mathutils.Vector((0, -10, 2))
    cam.rotation_euler = mathutils.Euler((90 * rad, 0 , 0))
    
    scene.render.image_settings.file_format = 'PNG'
    print(path + str(i) + '-' + str(cube_z_rot) + '.png')
    scene.render.filepath = path + str(i) + '-' + str(cube_z_rot) + '.png'
    bpy.ops.render.render(animation = False, write_still = True)

