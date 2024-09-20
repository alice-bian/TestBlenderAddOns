bl_info = {
    "name" : "Object Adder",
    "author" : "Alice Bian",
    "version" : (1, 0),
    "blender" : (3, 6, 5),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",
}



import bpy

class AddObjectPanel(bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "PT_AddObjectPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Add-On'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Add an object", icon='OBJECT_ORIGIN')
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon='CUBE')
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon='SPHERE')
        row = layout.row()
        row.operator("object.text_add", icon='FILE_FONT')


class PanelA(bpy.types.Panel):
    bl_label = "Scale"
    bl_idname = "PT_PanelA"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Add-On'
    bl_parent_id = 'PT_AddObjectPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="This is Panel A", icon='FONT_DATA')


class PanelB(bpy.types.Panel):
    bl_label = "Panel B"
    bl_idname = "PT_PanelB"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Object Add-On'
    bl_parent_id = 'PT_AddObjectPanel'
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="This is Panel B", icon='COLOR_BLUE')


def register():
    bpy.utils.register_class(AddObjectPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)
    
def unregister():
    bpy.utils.unregister_class(AddObjectPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)

if __name__ == "__main__":
    register()