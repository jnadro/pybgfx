import ctypes
import pybgfx as bgfx
import python_image


class HelloWorld(bgfx.App):

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def init(self):
        init = bgfx.bgfx_init_t()
        bgfx.init_ctor(ctypes.pointer(init))
        bgfx.init(ctypes.pointer(init))

        bgfx.reset(self.width, self.height, bgfx.BGFX_RESET_VSYNC, init.resolution.format)

        # enable debug text.
        bgfx.set_debug(bgfx.BGFX_DEBUG_TEXT)

        bgfx.set_view_clear(0, bgfx.BGFX_CLEAR_COLOR | bgfx.BGFX_CLEAR_DEPTH, 0x303030ff, 1.0, 0)

    def shutdown(self):
        bgfx.shutdown() 

    def update(self, dt):
        bgfx.set_view_rect(0, 0, 0, self.width, self.height)
        bgfx.touch(0)
        bgfx.dbg_text_clear(0, False)
        bgfx.dbg_text_image(int(max(self.width / 2 / 8, 20)) - 20,
                            int(max(self.height / 2 / 16, 6)) - 12,
                            40,
                            27,
                            python_image.s_python_logo,
                            80)
        bgfx.dbg_text_printf(0, 1, 0x4f, self.title)
        bgfx.dbg_text_printf(0, 2, 0x6f, b"Description: Initialization and debug text.")
        bgfx.frame(False)

app = HelloWorld(1280, 720, b"pybgfx/examples/00-helloworld")
app.run()
