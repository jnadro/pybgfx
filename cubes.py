import bgfx
from bgfx_ex import App

class Cubes(App):

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def init(self):
        bgfx.init(bgfx.BGFX_RENDERER_TYPE_COUNT, bgfx.BGFX_PCI_ID_NONE, 0, None, None)
        bgfx.reset(self.width, self.height, bgfx.BGFX_RESET_VSYNC)
        bgfx.set_debug(bgfx.BGFX_DEBUG_TEXT)
        bgfx.set_view_clear(0, bgfx.BGFX_CLEAR_COLOR | bgfx.BGFX_CLEAR_DEPTH, 0x303030ff, 1.0, 0)

    def shutdown(self):
        bgfx.shutdown()

    def update(self):
        bgfx.touch(0)
        bgfx.frame()

app = Cubes(1280, 720, "Cubes")
app.run()
