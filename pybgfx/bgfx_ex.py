import ctypes
import time
import os

import pybgfx

class Window(ctypes.Structure):
    pass

class App(object):

    def __init__(self):
        pass

    def init(self):
        pass

    def shutdown(self):
        pass

    def update(self, dt):
        pass

    def run(self):
        glfw_dll_path = os.path.dirname(__file__) + "\\glfw3"
        glfw = ctypes.CDLL(glfw_dll_path)

        # Set up arguments and return types so the function calls below succeed
        glfw.glfwCreateWindow.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_char_p]
        glfw.glfwCreateWindow.restype = ctypes.POINTER(Window)

        glfw.glfwMakeContextCurrent.argtypes = [ctypes.POINTER(Window)]

        glfw.glfwGetWin32Window.argtypes = [ctypes.POINTER(Window)]
        glfw.glfwGetWin32Window.restype = ctypes.c_void_p

        glfw.glfwWindowShouldClose.argtypes = [ctypes.POINTER(Window)]
        glfw.glfwWindowShouldClose.restype = ctypes.c_int

        glfw.glfwInit()
        window = glfw.glfwCreateWindow(self.width, self.height, self.title, 0, 0)
        glfw.glfwMakeContextCurrent(window)
        handle = glfw.glfwGetWin32Window(window)
        pybgfx.bgfx.set_platform_data(handle)

        self.init()

        last_time = None

        while not glfw.glfwWindowShouldClose(window):
            glfw.glfwPollEvents()

            now = time.time()
            if last_time == None:
                last_time = now

            frame_time = now - last_time
            last_time = now

            self.update(frame_time)

        self.shutdown()
        glfw.glfwTerminate()
