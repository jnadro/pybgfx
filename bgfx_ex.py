import ctypes
import time

import bgfx


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
        glfw = ctypes.CDLL("glfw3")
        glfw.glfwGetWin32Window.restype = ctypes.c_void_p

        glfw.glfwInit()
        window = glfw.glfwCreateWindow(
            self.width, self.height, self.title, 0, 0)
        glfw.glfwMakeContextCurrent(window)
        handle = glfw.glfwGetWin32Window(window)
        bgfx.set_platform_data(handle)

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
