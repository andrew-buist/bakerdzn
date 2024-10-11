bl_info = {
    "name": "Baker's Dozen",
    "author": "Andrew Buist",
    "description": "Adding mixing and discrete layer selection to texture/vertex baking.",
    "blender": (4, 2, 0),
    "version": (1, 0, 0),
    "location": "Render > Bake",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Bake"
}

from . import operators, ui, property_groups

# Each package has a register and unregister functions defined in their own __init__.py files
packages = [operators, ui, property_groups]


def register():
    for package in packages:
        package.register()

def unregister():
    for package in packages:
        package.unregister()