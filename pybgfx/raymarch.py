from ctypes import Structure, c_float, c_int, c_uint8, c_uint16, c_uint32, c_uint64, POINTER, byref, cast, sizeof, c_void_p, byref
import time

import bgfx
import bgfx_utils
from bgfx_ex import App


class PosColorTexCoord0Vertex(Structure):
    _fields_ = [("m_x", c_float),
                ("m_y", c_float),
                ("m_z", c_float),
                ("m_abgr", c_uint32),
                ("m_u", c_float),
                ("m_v", c_float)]

def render_screen_space_quad(view, program, x, y, width, height):
    pass 

class Raymarch(App):

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

        # Create vertex stream declaration.
        rendererType = bgfx.get_renderer_type()
        self.ms_decl = bgfx.vertex_decl()
        bgfx.vertex_decl_begin(byref(self.ms_decl), rendererType)
        bgfx.vertex_decl_add(self.ms_decl, bgfx.BGFX_ATTRIB_POSITION,
                             3, bgfx.BGFX_ATTRIB_TYPE_FLOAT, False, False)
        bgfx.vertex_decl_add(self.ms_decl, bgfx.BGFX_ATTRIB_COLOR0,
                             4, bgfx.BGFX_ATTRIB_TYPE_UINT8, True, False)
        bgfx.vertex_decl_add(self.ms_decl, bgfx.BGFX_ATTRIB_TEXCOORD0, 2, False, False)
        bgfx.vertex_decl_end(self.ms_decl)

        self.u_mtx = bgfx.create_uniform("u_mtx", bgfx.BGFX_UNIFORM_TYPE_MAT4, 1)
        self.u_light_dir_time = bgfx.create_uniform("u_lightDirTime", bgfx.BGFX_UNIFORM_TYPE_VEC4, 1)

        # Create program from shaders.
        self.raymarching = bgfx_utils.loadProgram("vs_raymarching", "fs_raymarching")

    def shutdown(self):
        bgfx.destroy_program(self.raymarching)

        bgfx.destroy_uniform(self.u_mtx)
        bgfx.destroy_uniform(self.u_light_dir_time)

        bgfx.shutdown()

    def update(self, dt):
        # Set view 0 default viewport
        bgfx.set_view_rect(0, 0, 0, self.width, self.height)

        # Set view 1 default viewport
        bgfx.set_view_rect(1, 0, 0, self.width, self.height)

        bgfx.touch(0)

        bgfx.dbg_text_clear(0, False)
        bgfx.dbg_text_printf(0, 1, 0x4f, self.title)
        bgfx.dbg_text_printf(0, 2, 0x6f, "Description: Updating shader uniforms.")
        bgfx.dbg_text_printf(0, 3, 0x0f, "Frame: %.3f [ms]" % (dt * 1000))

        at = (c_float * 3)(*[0.0, 0.0, 0.0])
        eye = (c_float * 3)(*[0.0, 0.0, -15.0])

        view = (c_float * 16)(*[1.0, 0.0, 0.0, 0.0,
                                0.0, 1.0, 0.0, 0.0,
                                0.0, 0.0, 1.0, 0.0,
                                -0.0, -0.0, 15.0, 1.0])
        proj = (c_float * 16)(*[0.974278629, 0.0, 0.0, 0.0,
                                0.0, 1.73205090, 0.0, 0.0,
                                0.0, -0.0, 1.00100100, 1.0,
                                0.0, 0.0, -0.100100100, 0.0])

        bgfx.set_view_transform(0, view, proj)

        ortho = (c_float * 16)(*[0.00156250002, 0.0, 0.0, 0.0,
                                0.0, -0.00277777785, 0.0, 0.0,
                                0.0, 0.0, 0.00999999978, 1.0,
                                -1.0, 1.0, -0.0, 1.0])

        bgfx.set_view_transform(1, None, ortho)

        light_dir = (c_float * 4)(*[-0.3369, -0.4209, -0.842, 0.000136])
        bgfx.set_uniform(self.u_light_dir_time, light_dir, 1)

        inv_mvp = (c_float * 16)(*[1.02640045, 0.0, 0.0, 0.0,
                                   0.0, 0.577350199, 0.0, 0.0,
                                   0.00756994542, -0.0204593129, 149.849350, -9.98995686,
                                  -0.00752700586, 0.0203432590, -148.999344, 9.99995613])
        bgfx.set_uniform(self.u_mtx, inv_mvp, 1)

        render_screen_space_quad(1, self.raymarching, 0.0, 0.0, self.width, self.height)

        bgfx.frame()

app = Raymarch(1280, 720, "pybgfx/examples/raymarch")
app.run()
