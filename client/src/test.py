import os
path = os.path.join(os.getcwd(),"client","src","shaders")

with open(os.path.join(path,"vert.glsl"),"r") as vertFile:
    vertSrc = vertFile.read()