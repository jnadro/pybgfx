import os

from ctypes import cast, c_void_p

import pybgfx as bgfx

runtimeDir = "../runtime/"


def loadMem(filePath):
    filePath = runtimeDir + filePath
    with open(filePath, "rb") as f:
        read_data = f.read()
        size = len(read_data)
        memory = bgfx.copy(cast(read_data, c_void_p), size)
        return memory
    return None


def loadShader(shaderName):
    shaderPath = "shaders/dx9/"
    rendererType = bgfx.get_renderer_type()
    shaderPath = {
        bgfx.BGFX_RENDERER_TYPE_DIRECT3D11.value: "shaders/dx11/",
        bgfx.BGFX_RENDERER_TYPE_DIRECT3D12.value: "shaders/dx11/",
        bgfx.BGFX_RENDERER_TYPE_OPENGL.value: "shaders/glsl/",
        bgfx.BGFX_RENDERER_TYPE_METAL.value: "shaders/metal/",
        bgfx.BGFX_RENDERER_TYPE_OPENGLES.value: "shaders/gles/",
    }.get(rendererType, "shaders/dx9/")
    filePath = shaderPath + shaderName + ".bin"
    fileMemory = loadMem(filePath)
    shader = bgfx.create_shader(fileMemory)
    return shader


def loadProgram(vsName, fsName):
    vsh = loadShader(vsName)
    fsh = bgfx.BGFX_INVALID_HANDLE
    if (fsName != None):
        fsh = loadShader(fsName)
    return bgfx.create_program(vsh, fsh, True)
