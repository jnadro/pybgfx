import ctypes
import pybgfx as bgfx


class PosColorTexCoord0Vertex(ctypes.Structure):
    _fields_ = [
        ("m_x", ctypes.c_float),
        ("m_y", ctypes.c_float),
        ("m_z", ctypes.c_float),
        ("m_abgr", ctypes.c_uint32),
        ("m_u", ctypes.c_float),
        ("m_v", ctypes.c_float)
    ]

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

        # Create vertex stream declaration.
        rendererType = bgfx.get_renderer_type()
        self.ms_decl = bgfx.vertex_decl()
        bgfx.vertex_decl_begin(ctypes.byref(self.ms_decl), rendererType)
        bgfx.vertex_decl_add(self.ms_decl, bgfx.BGFX_ATTRIB_POSITION,
                             3, bgfx.BGFX_ATTRIB_TYPE_FLOAT, False, False)
        bgfx.vertex_decl_add(self.ms_decl, bgfx.BGFX_ATTRIB_COLOR0,
                             4, bgfx.BGFX_ATTRIB_TYPE_UINT8, True, False)
        bgfx.vertex_decl_add(self.ms_decl, bgfx.BGFX_ATTRIB_TEXCOORD0,
                             2, bgfx.BGFX_ATTRIB_TYPE_FLOAT, False, False)
        bgfx.vertex_decl_end(self.ms_decl)

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
