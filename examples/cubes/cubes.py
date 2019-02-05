from ctypes import Structure, c_float, c_int, c_uint8, c_uint16, c_uint32, c_uint64, POINTER, pointer, byref, cast, sizeof, c_void_p, byref
import time

import pybgfx as bgfx
import matrix


class PosColorVertex(Structure):
    _fields_ = [("m_x", c_float),
                ("m_y", c_float),
                ("m_z", c_float),
                ("m_abgr", c_uint32)]

num_vertices = 8
s_cubeVertices = (PosColorVertex * num_vertices)(
    PosColorVertex(-1.0,  1.0,  1.0, 0xff000000),
    PosColorVertex(1.0,  1.0,  1.0, 0xff0000ff),
    PosColorVertex(-1.0, -1.0,  1.0, 0xff00ff00),
    PosColorVertex(1.0, -1.0,  1.0, 0xff00ffff),
    PosColorVertex(-1.0,  1.0, -1.0, 0xffff0000),
    PosColorVertex(1.0,  1.0, -1.0, 0xffff00ff),
    PosColorVertex(-1.0, -1.0, -1.0, 0xffffff00),
    PosColorVertex(1.0, -1.0, -1.0, 0xffffffff),
)

num_indices = 36
s_cubeIndices = (c_uint16 * num_indices)(
    *[0, 1, 2,  # 0
        1, 3, 2,
        4, 6, 5,  # 2
        5, 6, 7,
        0, 2, 4,  # 4
        4, 2, 6,
        1, 5, 3,  # 6
        5, 7, 3,
        0, 4, 1,  # 8
        4, 5, 1,
        2, 3, 6,  # 10
        6, 3, 7])


class Cubes(bgfx.App):

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.title = title

        self.m_ibh = None

    def init(self):
        init = bgfx.bgfx_init_t()
        bgfx.init_ctor(pointer(init))
        bgfx.init(pointer(init))

        bgfx.reset(self.width, self.height, bgfx.BGFX_RESET_VSYNC, init.resolution.format)

        # Enable debug text.
        bgfx.set_debug(bgfx.BGFX_DEBUG_TEXT)

        # Set view 0 clear state.
        bgfx.set_view_clear(0, bgfx.BGFX_CLEAR_COLOR | bgfx.BGFX_CLEAR_DEPTH, 0x303030ff, 1.0, 0)

        # Create vertex stream declaration.
        rendererType = bgfx.get_renderer_type()
        self.ms_decl = bgfx.vertex_decl()
        bgfx.vertex_decl_begin(byref(self.ms_decl), rendererType)
        bgfx.vertex_decl_add(self.ms_decl, bgfx.BGFX_ATTRIB_POSITION,
                             3, bgfx.BGFX_ATTRIB_TYPE_FLOAT, False, False)
        bgfx.vertex_decl_add(self.ms_decl, bgfx.BGFX_ATTRIB_COLOR0,
                             4, bgfx.BGFX_ATTRIB_TYPE_UINT8, True, False)
        bgfx.vertex_decl_end(self.ms_decl)

        # Create static vertex buffer
        vb_memory = bgfx.copy(cast(s_cubeVertices, c_void_p),
                              sizeof(PosColorVertex) * num_vertices)
        self.m_vbh = bgfx.create_vertex_buffer(
            vb_memory, byref(self.ms_decl), bgfx.BGFX_BUFFER_NONE)

        # Create static index buffer
        ib_memory = bgfx.copy(cast(s_cubeIndices, c_void_p),
                              sizeof(c_uint16) * num_indices)
        self.m_ibh = bgfx.create_index_buffer(ib_memory, bgfx.BGFX_BUFFER_NONE)

        # Create program from shaders.
        self.program = bgfx.loadProgram("vs_cubes", "fs_cubes")
        self.elapsed_time = 0

    def shutdown(self):
        # cleanup
        bgfx.destroy_index_buffer(self.m_ibh)
        bgfx.destroy_vertex_buffer(self.m_vbh)
        bgfx.destroy_program(self.program)
        bgfx.shutdown()

    def update(self, dt):
        self.elapsed_time += dt

        bgfx.dbg_text_clear(0, False)
        bgfx.dbg_text_printf(0, 1, 0x4f, b"pybgfx/examples/01-cube")
        bgfx.dbg_text_printf(0, 2, 0x6f, b"Description: Rendering simple static mesh.")
        bgfx.dbg_text_printf(0, 3, 0x0f, b"Frame: %.3f [ms]" % (dt * 1000))

        at = (c_float * 3)(*[0.0, 0.0, 0.0])
        eye = (c_float * 3)(*[0.0, 0.0, -35.0])
        up = (c_float * 3)(*[0.0, 1.0, 0.0])

        view = matrix.look_at(eye, at, up)
        proj = matrix.proj(60.0, self.width / self.height, 0.1, 100.0)

        bgfx.set_view_transform(0, view, proj)

        # Set view 0 default viewport.
        bgfx.set_view_rect(0, 0, 0, self.width, self.height)

        # This dummy draw call is here to make sure that view 0 is cleared
        # if no other draw calls are submitted to view 0.
        bgfx.touch(0)

        for yy in range(0, 11):
            for xx in range(0, 11):

                mtx = (c_float * 16)(*[1.0, 0.0, 0.0, 0.0,
                                       0.0, 1.0, 0.0, 0.0,
                                       0.0, 0.0, 1.0, 0.0,
                                       0.0, 0.0, 0.0, 1.0])
                matrix.rotate_xy(mtx, self.elapsed_time + xx*0.21, self.elapsed_time + yy*0.37)
                mtx[12] = -15.0 + xx*3.0
                mtx[13] = -15.0 + yy*3.0
                mtx[14] = 0.0
                bgfx.set_transform(mtx, 1)

                # Set vertex and index buffer.
                bgfx.set_vertex_buffer(0, self.m_vbh, 0, num_vertices)
                bgfx.set_index_buffer(self.m_ibh, 0, num_indices)

                bgfx.set_state(bgfx.BGFX_STATE_DEFAULT, 0)

                bgfx.submit(0, self.program, 0, False)

        # Advance to next frame. Rendering thread will be kicked to
        # process submitted rendering primitives.
        bgfx.frame(False)

app = Cubes(1280, 720, b"Cubes")
app.run()
