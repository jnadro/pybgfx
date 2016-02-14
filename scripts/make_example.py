import sys
import os.path

example_str = """
import bgfx
from bgfx_ex import App


class {0}(App):

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
        bgfx.dbg_text_printf(0, 1, 0x4f, self.title)
        bgfx.frame()

app = {0}(1280, 720, "pybgfx/examples/{1}")
app.run()
"""

if len(sys.argv) < 2:
	print "Usage: make_example.py [example_name]"
	sys.exit()

example_name = sys.argv[1]
class_name = example_name.capitalize()
file_name = example_name + ".py"

if os.path.isfile(file_name):
	print file_name + " already exists!"
	sys.exit()

print "Writing " + file_name
with open(file_name, "w") as file:
	file.write(example_str.format(class_name, example_name))
