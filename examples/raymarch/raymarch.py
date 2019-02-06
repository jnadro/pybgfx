import ctypes
import pybgfx as bgfx
import matrix

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

        # Create uniforms
        self.u_mtx = bgfx.create_uniform("u_mtx", bgfx.BGFX_UNIFORM_TYPE_MAT4, 1)
        self.u_light_dir_time = bgfx.create_uniform("u_lightDirTime", bgfx.BGFX_UNIFORM_TYPE_VEC4, 1)

        # Create program from shaders
        self.m_program = bgfx.loadProgram("vs_raymarching", "fs_raymarching")
        self.elapsed_time = 0.0


    def shutdown(self):
        bgfx.destroy_program(self.m_program)
        bgfx.destroy_uniform(self.u_mtx)
        bgfx.destroy_uniform(self.u_light_dir_time)

        bgfx.shutdown()

    def render_screen_space_quad(self, view, program, x, y, width, height):
        tvb = bgfx.transient_vertex_buffer()
        tib = bgfx.bgfx_transient_index_buffer()

        if bgfx.alloc_transient_buffers(ctypes.pointer(tvb), ctypes.pointer(self.ms_decl), 4, ctypes.pointer(tib), 6):
            vertex = ctypes.cast(tvb.data, ctypes.POINTER(PosColorTexCoord0Vertex))

            zz = 0.0

            minx = x
            maxx = x + width
            miny = y
            maxy = y + height

            minu = -1.0, minv = -1.0, maxu = 1.0, maxv = 1.0



            bgfx.set_state(bgfx.BGFX_STATE_DEFAULT)
            bgfx.set_index_buffer(tib)
            bgfx.set_vertex_buffer(0, tvb)
            bgfx.submit(view, self.m_program)

    def update(self, dt):
        self.elapsed_time += dt

        bgfx.set_view_rect(0, 0, 0, self.width, self.height)
        bgfx.set_view_rect(1, 0, 0, self.width, self.height)

        bgfx.touch(0)

        at = (ctypes.c_float * 3)(*[0.0, 0.0, 0.0])
        eye = (ctypes.c_float * 3)(*[0.0, 0.0, -15.0])
        up = (ctypes.c_float * 3)(*[0.0, 1.0, 0.0])

        view = matrix.look_at(eye, at, up)
        proj = matrix.proj(60.0, self.width / self.height, 0.1, 100.0)

        ortho = matrix.ortho(0., self.width, self.height, 0.0, 0.0, 100.0, 0.0)

        NULL = ctypes.POINTER(ctypes.c_void_p)()
        bgfx.set_view_transform(1, NULL, ortho)

        mtx_inv = (ctypes.c_float * 16)(*[1.0, 0.0, 0.0, 0.0,
                                           0.0, 1.0, 0.0, 0.0,
                                           0.0, 0.0, 1.0, 0.0,
                                           0.0, 0.0, 0.0, 1.0])
        matrix.rotate_xy(mtx_inv, self.elapsed_time, self.elapsed_time + 0.37)

        light_dir_model = matrix.normalize()
        light_dir_time = (ctypes.c_float * 3)(*[0.0, 0.0, 0.0])
        bgfx.set_uniform(self.u_light_dir_time, light_dir_time, 1)

        bgfx.set_uniform(self.u_mtx, inv_mvp, 1)

        render_screen_space_quad(1, self.m_program, 0.0, 0.0, self.width, self.height)

        bgfx.dbg_text_clear(0, False)
        bgfx.dbg_text_printf(0, 1, 0x4f, self.title)

        bgfx.frame(False)

app = Raymarch(1280, 720, b"pybgfx/examples/raymarch")
app.run()
