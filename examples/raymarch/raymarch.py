import ctypes
import pybgfx as bgfx


class Raymarch(bgfx.App):

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def init(self):
        init = bgfx.bgfx_init_t()
        bgfx.init_ctor(ctypes.pointer(init))
        bgfx.init(ctypes.pointer(init))

        bgfx.reset(self.width, self.height, bgfx.BGFX_RESET_VSYNC, init.resolution.format)

        bgfx.set_debug(bgfx.BGFX_DEBUG_TEXT)
        bgfx.set_view_clear(0, bgfx.BGFX_CLEAR_COLOR |
                            bgfx.BGFX_CLEAR_DEPTH, 0x303030ff, 1.0, 0)

    def shutdown(self):
        bgfx.shutdown()

    def update(self, dt):
        bgfx.set_view_rect(0, 0, 0, self.width, self.height)
        bgfx.touch(0)
        bgfx.dbg_text_clear(0, False)
        bgfx.dbg_text_printf(0, 1, 0x4f, self.title)
        bgfx.frame(False)

app = Raymarch(1280, 720, b"pybgfx/examples/raymarch")
app.run()
