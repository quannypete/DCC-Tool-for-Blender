import bpy

def create_material(name, color):
    mat = bpy.data.materials.new(name=name)
    mat.diffuse_color = color
    return mat

def create_light(name, light_type, location):
    bpy.ops.object.light_add(type=light_type, location=location)
    return bpy.context.active_object

def setup_scene_based_on_metadata(obj):
    if "metal" in obj.name:
        metal_material = create_material("Metal_Mat", (0.8, 0.8, 0.8, 1))
        obj.data.materials.append(metal_material)
        create_light("Spotlight", 'SPOT', (0, 0, 2))

    elif "glass" in obj.name:
        glass_material = create_material("Glass_Mat", (0.4, 0.6, 0.8, 0.5))
        obj.data.materials.append(glass_material)
        create_light("AreaLight", 'AREA', (2, 2, 2))

def main():
    for obj in bpy.context.selected_objects:
        setup_scene_based_on_metadata(obj)
