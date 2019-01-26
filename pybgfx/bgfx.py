'''
Python bindings for bgfx.
'''

__author__ = "Jason Nadro"
__copyright__ = "Copyright 2016, Jason Nadro"
__credits__ = ["Jason Nadro"]
__license__ = "BSD 2-clause"
__version__ = "0.0.1"
__maintainer__ = "Jason Nadro"
__email__ = ""
__status__ = "Development"

import ctypes
from ctypes import Structure, POINTER, cast, byref
from ctypes import c_bool, c_int, c_uint8, c_uint16, c_uint32, c_uint64, c_float, c_char_p, c_void_p
import os

bgfx_dll_path = os.path.dirname(__file__) + "\\bgfx-shared-libRelease"
_bgfx = ctypes.CDLL(bgfx_dll_path)

# bgfx_renderer_type
BGFX_RENDERER_TYPE_NULL = 0
BGFX_RENDERER_TYPE_DIRECT3D9 = 1
BGFX_RENDERER_TYPE_DIRECT3D11 = 2
BGFX_RENDERER_TYPE_DIRECT3D12 = 3
BGFX_RENDERER_TYPE_METAL = 4
BGFX_RENDERER_TYPE_OPENGLES = 5
BGFX_RENDERER_TYPE_OPENGL = 6
BGFX_RENDERER_TYPE_VULKAN = 7
BGFX_RENDERER_TYPE_COUNT = 8

# bgfx_access
BGFX_ACCESS_READ = 0
BGFX_ACCESS_WRITE = 1
BGFX_ACCESS_READWRITE = 2
BGFX_ACCESS_COUNT = 3

# bgfx_attrib
BGFX_ATTRIB_POSITION = 0
BGFX_ATTRIB_NORMAL = 1
BGFX_ATTRIB_TANGENT = 2
BGFX_ATTRIB_BITANGENT = 3
BGFX_ATTRIB_COLOR0 = 4
BGFX_ATTRIB_COLOR1 = 5
BGFX_ATTRIB_INDICES = 6
BGFX_ATTRIB_WEIGHT = 7
BGFX_ATTRIB_TEXCOORD0 = 8
BGFX_ATTRIB_TEXCOORD1 = 9
BGFX_ATTRIB_TEXCOORD2 = 10
BGFX_ATTRIB_TEXCOORD3 = 11
BGFX_ATTRIB_TEXCOORD4 = 12
BGFX_ATTRIB_TEXCOORD5 = 13
BGFX_ATTRIB_TEXCOORD6 = 14
BGFX_ATTRIB_TEXCOORD7 = 15
BGFX_ATTRIB_COUNT = 16

# bgfx_attrib_type
BGFX_ATTRIB_TYPE_UINT8 = 0
BGFX_ATTRIB_TYPE_UINT10 = 1
BGFX_ATTRIB_TYPE_INT16 = 2
BGFX_ATTRIB_TYPE_HALF = 3
BGFX_ATTRIB_TYPE_FLOAT = 4
BGFX_ATTRIB_TYPE_COUNT = 5

# bgfx_uniform_type
BGFX_UNIFORM_TYPE_INT1 = 0
BGFX_UNIFORM_TYPE_END = 1

BGFX_UNIFORM_TYPE_VEC4 = 2
BGFX_UNIFORM_TYPE_MAT3 = 3
BGFX_UNIFORM_TYPE_MAT4 = 4

BGFX_UNIFORM_TYPE_COUNT = 5

BGFX_PCI_ID_NONE = 0x0000
BGFX_PCI_ID_SOFTWARE_RASTERIZER = 0x0001
BGFX_PCI_ID_AMD = 0x1002
BGFX_PCI_ID_INTEL = 0x8086
BGFX_PCI_ID_NVIDIA = 0x10de

BGFX_RESET_NONE = 0x00000000  # //!< No reset flags.
BGFX_RESET_FULLSCREEN = 0x00000001  # //!< Not supported yet.
BGFX_RESET_FULLSCREEN_SHIFT = 0          # //!< Fullscreen bit shift.
BGFX_RESET_FULLSCREEN_MASK = 0x00000001  # //!< Fullscreen bit mask.
BGFX_RESET_MSAA_X2 = 0x00000010  # //!< Enable 2x MSAA.
BGFX_RESET_MSAA_X4 = 0x00000020  # //!< Enable 4x MSAA.
BGFX_RESET_MSAA_X8 = 0x00000030  # //!< Enable 8x MSAA.
BGFX_RESET_MSAA_X16 = 0x00000040  # //!< Enable 16x MSAA.
BGFX_RESET_MSAA_SHIFT = 4          # //!< MSAA mode bit shift.
BGFX_RESET_MSAA_MASK = 0x00000070  # //!< MSAA mode bit mask.
BGFX_RESET_VSYNC = 0x00000080  # //!< Enable V-Sync.
BGFX_RESET_MAXANISOTROPY = 0x00000100  # //!< Turn on/off max anisotropy.
BGFX_RESET_CAPTURE = 0x00000200  # //!< Begin screen capture.
BGFX_RESET_HMD = 0x00000400  # //!< HMD stereo rendering.
BGFX_RESET_HMD_DEBUG = 0x00000800  # //!< HMD stereo rendering debug mode.
BGFX_RESET_HMD_RECENTER = 0x00001000  # //!< HMD calibration.
# //!< Flush rendering after submitting to GPU.
BGFX_RESET_FLUSH_AFTER_RENDER = 0x00002000
# //!< This flag  specifies where flip occurs. Default behavior is that flip occurs before rendering new frame. This flag only has effect when `BGFX_CONFIG_MULTITHREADED=0`.
BGFX_RESET_FLIP_AFTER_RENDER = 0x00004000
BGFX_RESET_SRGB_BACKBUFFER = 0x00008000  # //!< Enable sRGB backbuffer.
BGFX_RESET_HIDPI = 0x00010000  # //!< Enable HiDPI rendering.
BGFX_RESET_DEPTH_CLAMP = 0x00020000  # //!< Enable depth clamp.
BGFX_RESET_RESERVED_SHIFT = 31         # //!< Internal bits shift.
BGFX_RESET_RESERVED_MASK = 0x80000000  # //!< Internal bits mask.

BGFX_CLEAR_NONE = 0x0000
BGFX_CLEAR_COLOR = 0x0001
BGFX_CLEAR_DEPTH = 0x0002
BGFX_CLEAR_STENCIL = 0x0004
BGFX_CLEAR_DISCARD_COLOR_0 = 0x0008
BGFX_CLEAR_DISCARD_COLOR_1 = 0x0010
BGFX_CLEAR_DISCARD_COLOR_2 = 0x0020
BGFX_CLEAR_DISCARD_COLOR_3 = 0x0040
BGFX_CLEAR_DISCARD_COLOR_4 = 0x0080
BGFX_CLEAR_DISCARD_COLOR_5 = 0x0100
BGFX_CLEAR_DISCARD_COLOR_6 = 0x0200
BGFX_CLEAR_DISCARD_COLOR_7 = 0x0400
BGFX_CLEAR_DISCARD_DEPTH = 0x0800
BGFX_CLEAR_DISCARD_STENCIL = 0x1000

BGFX_CLEAR_DISCARD_COLOR_MASK = 0 | BGFX_CLEAR_DISCARD_COLOR_0 | BGFX_CLEAR_DISCARD_COLOR_1 | BGFX_CLEAR_DISCARD_COLOR_2 | BGFX_CLEAR_DISCARD_COLOR_3 | BGFX_CLEAR_DISCARD_COLOR_4 | BGFX_CLEAR_DISCARD_COLOR_5 | BGFX_CLEAR_DISCARD_COLOR_6 | BGFX_CLEAR_DISCARD_COLOR_7
BGFX_CLEAR_DISCARD_MASK = 0 | BGFX_CLEAR_DISCARD_COLOR_MASK | BGFX_CLEAR_DISCARD_DEPTH | BGFX_CLEAR_DISCARD_STENCIL

BGFX_DEBUG_NONE = 0x00000000  # //!< No debug.
BGFX_DEBUG_WIREFRAME = 0x00000001  # //!< Enable wireframe for all primitives.
BGFX_DEBUG_IFH = 0x00000002
BGFX_DEBUG_STATS = 0x00000004  # //!< Enable statistics display.
BGFX_DEBUG_TEXT = 0x00000008  # //!< Enable debug text display.

BGFX_BUFFER_NONE = 0x0000

BGFX_INVALID_HANDLE = 0xFFFF


class bgfx_index_buffer_handle(Structure):
    _fields_ = [("idx", c_uint16)]


class bgfx_vertex_buffer_handle(Structure):
    _fields_ = [("idx", c_uint16)]


class bgfx_program_handle(Structure):
    _fields_ = [("idx", c_uint16)]


class bgfx_shader_handle(Structure):
    _fields_ = [("idx", c_uint16)]


class bgfx_uniform_handle(Structure):
    _fields_ = [("idx", c_uint16)]


class bgfx_vertex_decl_handle(Structure):
    _fields_ = [("idx", c_uint16)]


class bgfx_memory(Structure):
    _fields_ = [("data", POINTER(c_uint8)),
                ("size", c_uint32)]


class vertex_decl(Structure):
    _fields_ = [("hash", c_uint32),
                ("stride", c_uint16),
                ("offset", c_uint16 * BGFX_ATTRIB_COUNT),
                ("attributes", c_uint16 * BGFX_ATTRIB_COUNT)]


class transient_index_buffer(Structure):
    _fields_ = [("data", POINTER(c_uint8)),
                ("size", c_uint32),
                ("handle", bgfx_index_buffer_handle),
                ("startIndex", c_uint32)]


class transient_vertex_buffer(Structure):
    _fields_ = [("data", POINTER(c_uint8)),
                ("size", c_uint32),
                ("startVertex", c_uint32),
                ("stride", c_uint16),
                ("handle", bgfx_vertex_buffer_handle),
                ("decl", bgfx_vertex_decl_handle)] 


def _bind(funcname, args=None, returns=None):
    func = getattr(_bgfx, funcname)
    func.argtypes = args
    func.restype = returns
    return func

vertex_decl_begin = _bind("bgfx_vertex_decl_begin", [
                          POINTER(vertex_decl), c_uint32])
vertex_decl_add = _bind("bgfx_vertex_decl_add", [POINTER(
    vertex_decl), c_uint32, c_uint8, c_uint32, c_bool])
vertex_decl_skip = _bind("bgfx_vertex_decl_skip", [
                         POINTER(vertex_decl), c_uint8])
vertex_decl_end = _bind("bgfx_vertex_decl_end", [POINTER(vertex_decl)])
init = _bind("bgfx_init")
shutdown = _bind("bgfx_shutdown")
reset = _bind("bgfx_reset")
frame = _bind("bgfx_frame")
alloc = _bind("bgfx_alloc", [c_uint32], POINTER(bgfx_memory))
copy = _bind("bgfx_copy", [c_void_p, c_uint32], POINTER(bgfx_memory))
get_renderer_type = _bind("bgfx_get_renderer_type", [], c_int)
set_debug = _bind("bgfx_set_debug")
dbg_text_clear = _bind("bgfx_dbg_text_clear")
dbg_text_printf = _bind("bgfx_dbg_text_printf")
dbg_text_image = _bind("bgfx_dbg_text_image", [
                       c_uint16, c_uint16, c_uint16, c_uint16, c_void_p, c_uint16])
create_index_buffer = _bind("bgfx_create_index_buffer", [
                            POINTER(bgfx_memory), c_uint16], bgfx_index_buffer_handle)
destroy_index_buffer = _bind("bgfx_destroy_index_buffer", [
                             bgfx_index_buffer_handle])
create_vertex_buffer = _bind("bgfx_create_vertex_buffer", [POINTER(
    bgfx_memory), POINTER(vertex_decl), c_uint16], bgfx_vertex_buffer_handle)
destroy_vertex_buffer = _bind("bgfx_destroy_vertex_buffer", [bgfx_vertex_buffer_handle])
alloc_transient_buffers = _bind("bgfx_alloc_transient_buffers", [POINTER(transient_vertex_buffer),
                                POINTER(vertex_decl), c_uint32, POINTER(transient_index_buffer),
                                c_uint32], c_bool)
create_shader = _bind("bgfx_create_shader", [
                      POINTER(bgfx_memory)], bgfx_shader_handle)
create_program = _bind("bgfx_create_program", [
                       bgfx_shader_handle, bgfx_shader_handle, c_bool], bgfx_program_handle)
destroy_program = _bind("bgfx_destroy_program", [bgfx_program_handle])
create_uniform = _bind("bgfx_create_uniform", [c_char_p, c_uint32, c_uint16], bgfx_uniform_handle)
destroy_uniform = _bind("bgfx_destroy_uniform", [bgfx_uniform_handle])
set_state = _bind("bgfx_set_state", [c_uint64, c_uint32])
set_transform = _bind("bgfx_set_transform", [c_void_p, c_uint16], c_uint32)
set_uniform = _bind("bgfx_set_uniform", [bgfx_uniform_handle, c_void_p, c_uint16])
set_index_buffer = _bind("bgfx_set_index_buffer", [
                         bgfx_index_buffer_handle, c_uint32, c_uint32])

set_transient_index_buffer = _bind("bgfx_set_transient_index_buffer", [POINTER(transient_index_buffer), c_uint32, c_uint32])

set_transient_vertex_buffer = _bind("bgfx_set_transient_vertex_buffer", [POINTER(transient_vertex_buffer), c_uint32, c_uint32])

set_vertex_buffer = _bind("bgfx_set_vertex_buffer", [
                          bgfx_vertex_buffer_handle, c_uint32, c_uint32])

set_view_rect = _bind("bgfx_set_view_rect",
                      args=[c_uint16, c_uint16, c_uint16, c_uint16, c_uint16],
                      returns=None)
                      
set_view_clear = _bind("bgfx_set_view_clear", [
                       c_uint8, c_uint16, c_uint32, c_float, c_uint8])
set_view_transform = _bind("bgfx_set_view_transform", [
                           c_uint8, c_void_p, c_void_p])

touch = _bind("bgfx_touch",
              args=[c_uint16],
              returns=None)

submit = _bind("bgfx_submit", [c_uint8, bgfx_program_handle, c_int], c_uint32)


class BGFX_PLATFORM_DATA(Structure):
    _fields_ = [("ndt", c_void_p),
                ("nwh", c_void_p),
                ("context", c_void_p),
                ("backBuffer", c_void_p),
                ("backBufferDS", c_void_p)]
_bgfx.bgfx_set_platform_data.argtypes = [POINTER(BGFX_PLATFORM_DATA)]


def set_platform_data(handle):
    platform_data = BGFX_PLATFORM_DATA(None, handle, None, None, None)
    _bgfx.bgfx_set_platform_data(byref(platform_data))
