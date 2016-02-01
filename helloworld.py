import ctypes.util
import bgfx
from ctypes import c_void_p
import image

width = 1280
height = 720
title = "pybgfx/examples/00-helloworld"

glfw = ctypes.CDLL("glfw3")
glfw.glfwGetWin32Window.restype = c_void_p
glfw.glfwInit()
window = glfw.glfwCreateWindow(width, height, title, 0, 0)
glfw.glfwMakeContextCurrent(window)
handle = glfw.glfwGetWin32Window(window)

bgfx.set_platform_data(handle)
bgfx.init(bgfx.BGFX_RENDERER_TYPE_COUNT, bgfx.BGFX_PCI_ID_NONE, 0, None, None)
bgfx.reset(width, height, bgfx.BGFX_RESET_VSYNC)
bgfx.set_debug(bgfx.BGFX_DEBUG_TEXT)
bgfx.set_view_clear(0, bgfx.BGFX_CLEAR_COLOR | bgfx.BGFX_CLEAR_DEPTH, 0x303030ff, 1.0, 0)

while not glfw.glfwWindowShouldClose(window):
	glfw.glfwPollEvents()

	bgfx.set_view_rect(0, 0, 0, width, height)
	bgfx.touch(0)
	bgfx.dbg_text_clear(0, False)
	bgfx.bgfx_dbg_text_image(max(width/2/8, 20)-20,
		max(height/2/16, 6)-6,
		40,
		12,
		image.s_logo,
		160)
	bgfx.dbg_text_printf(0, 1, 0x4f, title)
	bgfx.dbg_text_printf(0, 2, 0x6f, "Description: Initialization and debug text.");
	bgfx.frame()

bgfx.shutdown()
glfw.glfwTerminate()
