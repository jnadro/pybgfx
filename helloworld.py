import bgfx
from bgfx_ex import App
import python_image


class HelloWorld(App):

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

    def init(self):
        bgfx.init(bgfx.BGFX_RENDERER_TYPE_COUNT,
                  bgfx.BGFX_PCI_ID_NONE, 0, None, None)
        bgfx.reset(self.width, self.height, bgfx.BGFX_RESET_VSYNC)
        bgfx.set_debug(bgfx.BGFX_DEBUG_TEXT)
        bgfx.set_view_clear(0, bgfx.BGFX_CLEAR_COLOR |
                            bgfx.BGFX_CLEAR_DEPTH, 0x303030ff, 1.0, 0)

    def shutdown(self):
        bgfx.shutdown()

    def update(self):
        bgfx.set_view_rect(0, 0, 0, self.width, self.height)
        bgfx.touch(0)
        bgfx.dbg_text_clear(0, False)
        bgfx.dbg_text_image(max(self.width / 2 / 8, 20) - 20,
                            max(self.height / 2 / 16, 6) - 12,
                            40,
                            27,
                            python_image.s_python_logo,
                            80)
        bgfx.dbg_text_printf(0, 1, 0x4f, self.title)
        bgfx.dbg_text_printf(
            0, 2, 0x6f, "Description: Initialization and debug text.")
        bgfx.frame()

app = HelloWorld(1280, 720, "pybgfx/examples/00-helloworld")
app.run()
