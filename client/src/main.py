from panda3d.core import Shader
from direct.showbase.ShowBase import ShowBase

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        
        shader = Shader.load(Shader.SL_GLSL,
                     vertex="shaders/vert.glsl",
                     fragment="shaders/frag.glsl")

        self.render.set_shader(shader)
        

app = MyApp()
app.run()