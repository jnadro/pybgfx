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
from ctypes import Structure, POINTER, cast, byref, CFUNCTYPE
from ctypes import c_bool, c_int, c_int8, c_int16, c_int32, c_int64, c_uint8, c_uint16, c_uint32, c_uint64, c_float, c_char_p, c_void_p, c_size_t, c_char
import os

bgfx_dll_path = os.path.dirname(__file__) + "\\bgfx-shared-libRelease"
_bgfx = ctypes.CDLL(bgfx_dll_path)

enum_type = c_int

# bgfx_renderer_type
bgfx_renderer_type = enum_type
(
    BGFX_RENDERER_TYPE_NOOP,
    BGFX_RENDERER_TYPE_DIRECT3D9,
    BGFX_RENDERER_TYPE_DIRECT3D11,
    BGFX_RENDERER_TYPE_DIRECT3D12,
    BGFX_RENDERER_TYPE_GNM,
    BGFX_RENDERER_TYPE_METAL,
    BGFX_RENDERER_TYPE_OPENGLES,
    BGFX_RENDERER_TYPE_OPENGL,
    BGFX_RENDERER_TYPE_VULKAN,

    BGFX_RENDERER_TYPE_COUNT
) = map(bgfx_renderer_type,range(10))

# bgfx_access
bgfx_access = enum_type
(
    BGFX_ACCESS_READ,
    BGFX_ACCESS_WRITE,
    BGFX_ACCESS_READWRITE,

    BGFX_ACCESS_COUNT
) = map(bgfx_access, range(4))

# bgfx_attrib
bgfx_attrib = enum_type
(
    BGFX_ATTRIB_POSITION,
    BGFX_ATTRIB_NORMAL,
    BGFX_ATTRIB_TANGENT,
    BGFX_ATTRIB_BITANGENT,
    BGFX_ATTRIB_COLOR0,
    BGFX_ATTRIB_COLOR1,
    BGFX_ATTRIB_COLOR2,
    BGFX_ATTRIB_COLOR3,
    BGFX_ATTRIB_INDICES,
    BGFX_ATTRIB_WEIGHT,
    BGFX_ATTRIB_TEXCOORD0,
    BGFX_ATTRIB_TEXCOORD1,
    BGFX_ATTRIB_TEXCOORD2,
    BGFX_ATTRIB_TEXCOORD3,
    BGFX_ATTRIB_TEXCOORD4,
    BGFX_ATTRIB_TEXCOORD5,
    BGFX_ATTRIB_TEXCOORD6,
    BGFX_ATTRIB_TEXCOORD7,

    BGFX_ATTRIB_COUNT
) = map(bgfx_attrib, range(19))

# bgfx_attrib_type
bgfx_attrib_type = enum_type
(
    BGFX_ATTRIB_TYPE_UINT8,
    BGFX_ATTRIB_TYPE_UINT10,
    BGFX_ATTRIB_TYPE_INT16,
    BGFX_ATTRIB_TYPE_HALF,
    BGFX_ATTRIB_TYPE_FLOAT,

    BGFX_ATTRIB_TYPE_COUNT
) = map(bgfx_attrib_type, range(6))

# bgfx_texture_format
bgfx_texture_format = enum_type
(
    BGFX_TEXTURE_FORMAT_BC1,
    BGFX_TEXTURE_FORMAT_BC2,
    BGFX_TEXTURE_FORMAT_BC3,
    BGFX_TEXTURE_FORMAT_BC4,
    BGFX_TEXTURE_FORMAT_BC5,
    BGFX_TEXTURE_FORMAT_BC6H,
    BGFX_TEXTURE_FORMAT_BC7,
    BGFX_TEXTURE_FORMAT_ETC1,
    BGFX_TEXTURE_FORMAT_ETC2,
    BGFX_TEXTURE_FORMAT_ETC2A,
    BGFX_TEXTURE_FORMAT_ETC2A1,
    BGFX_TEXTURE_FORMAT_PTC12,
    BGFX_TEXTURE_FORMAT_PTC14,
    BGFX_TEXTURE_FORMAT_PTC12A,
    BGFX_TEXTURE_FORMAT_PTC14A,
    BGFX_TEXTURE_FORMAT_PTC22,
    BGFX_TEXTURE_FORMAT_PTC24,
    BGFX_TEXTURE_FORMAT_ATC,
    BGFX_TEXTURE_FORMAT_ATCE,
    BGFX_TEXTURE_FORMAT_ATCI,
    BGFX_TEXTURE_FORMAT_ASTC4x4,
    BGFX_TEXTURE_FORMAT_ASTC5x5,
    BGFX_TEXTURE_FORMAT_ASTC6x6,
    BGFX_TEXTURE_FORMAT_ASTC8x5,
    BGFX_TEXTURE_FORMAT_ASTC8x6,
    BGFX_TEXTURE_FORMAT_ASTC10x5,

    BGFX_TEXTURE_FORMAT_UNKNOWN,

    BGFX_TEXTURE_FORMAT_R1,
    BGFX_TEXTURE_FORMAT_A8,
    BGFX_TEXTURE_FORMAT_R8,
    BGFX_TEXTURE_FORMAT_R8I,
    BGFX_TEXTURE_FORMAT_R8U,
    BGFX_TEXTURE_FORMAT_R8S,
    BGFX_TEXTURE_FORMAT_R16,
    BGFX_TEXTURE_FORMAT_R16I,
    BGFX_TEXTURE_FORMAT_R16U,
    BGFX_TEXTURE_FORMAT_R16F,
    BGFX_TEXTURE_FORMAT_R16S,
    BGFX_TEXTURE_FORMAT_R32I,
    BGFX_TEXTURE_FORMAT_R32U,
    BGFX_TEXTURE_FORMAT_R32F,
    BGFX_TEXTURE_FORMAT_RG8,
    BGFX_TEXTURE_FORMAT_RG8I,
    BGFX_TEXTURE_FORMAT_RG8U,
    BGFX_TEXTURE_FORMAT_RG8S,
    BGFX_TEXTURE_FORMAT_RG16,
    BGFX_TEXTURE_FORMAT_RG16I,
    BGFX_TEXTURE_FORMAT_RG16U,
    BGFX_TEXTURE_FORMAT_RG16F,
    BGFX_TEXTURE_FORMAT_RG16S,
    BGFX_TEXTURE_FORMAT_RG32I,
    BGFX_TEXTURE_FORMAT_RG32U,
    BGFX_TEXTURE_FORMAT_RG32F,
    BGFX_TEXTURE_FORMAT_RGB8,
    BGFX_TEXTURE_FORMAT_RGB8I,
    BGFX_TEXTURE_FORMAT_RGB8U,
    BGFX_TEXTURE_FORMAT_RGB8S,
    BGFX_TEXTURE_FORMAT_RGB9E5F,
    BGFX_TEXTURE_FORMAT_BGRA8,
    BGFX_TEXTURE_FORMAT_RGBA8,
    BGFX_TEXTURE_FORMAT_RGBA8I,
    BGFX_TEXTURE_FORMAT_RGBA8U,
    BGFX_TEXTURE_FORMAT_RGBA8S,
    BGFX_TEXTURE_FORMAT_RGBA16,
    BGFX_TEXTURE_FORMAT_RGBA16I,
    BGFX_TEXTURE_FORMAT_RGBA16U,
    BGFX_TEXTURE_FORMAT_RGBA16F,
    BGFX_TEXTURE_FORMAT_RGBA16S,
    BGFX_TEXTURE_FORMAT_RGBA32I,
    BGFX_TEXTURE_FORMAT_RGBA32U,
    BGFX_TEXTURE_FORMAT_RGBA32F,
    BGFX_TEXTURE_FORMAT_R5G6B5,
    BGFX_TEXTURE_FORMAT_RGBA4,
    BGFX_TEXTURE_FORMAT_RGB5A1,
    BGFX_TEXTURE_FORMAT_RGB10A2,
    BGFX_TEXTURE_FORMAT_RG11B10F,

    BGFX_TEXTURE_FORMAT_UNKNOWN_DEPTH,

    BGFX_TEXTURE_FORMAT_D16,
    BGFX_TEXTURE_FORMAT_D24,
    BGFX_TEXTURE_FORMAT_D24S8,
    BGFX_TEXTURE_FORMAT_D32,
    BGFX_TEXTURE_FORMAT_D16F,
    BGFX_TEXTURE_FORMAT_D24F,
    BGFX_TEXTURE_FORMAT_D32F,
    BGFX_TEXTURE_FORMAT_D0S8,

    BGFX_TEXTURE_FORMAT_COUNT
) = map(bgfx_texture_format, range(86))

# bgfx_uniform_type
bgfx_uniform_type = enum_type
(
    BGFX_UNIFORM_TYPE_SAMPLER,
    BGFX_UNIFORM_TYPE_END,

    BGFX_UNIFORM_TYPE_VEC4,
    BGFX_UNIFORM_TYPE_MAT3,
    BGFX_UNIFORM_TYPE_MAT4,

    BGFX_UNIFORM_TYPE_COUNT
) = map(bgfx_uniform_type, range(6))

# backbuffer_ratio
backbuffer_ratio = enum_type
(
    BGFX_BACKBUFFER_RATIO_EQUAL,
    BGFX_BACKBUFFER_RATIO_HALF,
    BGFX_BACKBUFFER_RATIO_QUARTER,
    BGFX_BACKBUFFER_RATIO_EIGHTH,
    BGFX_BACKBUFFER_RATIO_SIXTEENTH,
    BGFX_BACKBUFFER_RATIO_DOUBLE,

    BGFX_BACKBUFFER_RATIO_COUNT
) = map(backbuffer_ratio, range(7))

# occlusion_query_result
occlusion_query_result = enum_type
(
    BGFX_OCCLUSION_QUERY_RESULT_INVISIBLE,
    BGFX_OCCLUSION_QUERY_RESULT_VISIBLE,
    BGFX_OCCLUSION_QUERY_RESULT_NORESULT,

    BGFX_OCCLUSION_QUERY_RESULT_COUNT
) = map(occlusion_query_result, range(4))

# topology
topology = enum_type
(
    BGFX_TOPOLOGY_TRI_LIST,
    BGFX_TOPOLOGY_TRI_STRIP,
    BGFX_TOPOLOGY_LINE_LIST,
    BGFX_TOPOLOGY_LINE_STRIP,
    BGFX_TOPOLOGY_POINT_LIST,

    BGFX_TOPOLOGY_COUNT
) = map(topology, range(6))

# topology_convert
topology_convert = enum_type
(
    BGFX_TOPOLOGY_CONVERT_TRI_LIST_FLIP_WINDING,
    BGFX_TOPOLOGY_CONVERT_TRI_STRIP_FLIP_WINDING,
    BGFX_TOPOLOGY_CONVERT_TRI_LIST_TO_LINE_LIST,
    BGFX_TOPOLOGY_CONVERT_TRI_STRIP_TO_TRI_LIST,
    BGFX_TOPOLOGY_CONVERT_LINE_STRIP_TO_LINE_LIST,

    BGFX_TOPOLOGY_CONVERT_COUNT
) = map(topology_convert, range(6))

# topology_sort
topology_sort = enum_type
(
    BGFX_TOPOLOGY_SORT_DIRECTION_FRONT_TO_BACK_MIN,
    BGFX_TOPOLOGY_SORT_DIRECTION_FRONT_TO_BACK_AVG,
    BGFX_TOPOLOGY_SORT_DIRECTION_FRONT_TO_BACK_MAX,
    BGFX_TOPOLOGY_SORT_DIRECTION_BACK_TO_FRONT_MIN,
    BGFX_TOPOLOGY_SORT_DIRECTION_BACK_TO_FRONT_AVG,
    BGFX_TOPOLOGY_SORT_DIRECTION_BACK_TO_FRONT_MAX,
    BGFX_TOPOLOGY_SORT_DISTANCE_FRONT_TO_BACK_MIN,
    BGFX_TOPOLOGY_SORT_DISTANCE_FRONT_TO_BACK_AVG,
    BGFX_TOPOLOGY_SORT_DISTANCE_FRONT_TO_BACK_MAX,
    BGFX_TOPOLOGY_SORT_DISTANCE_BACK_TO_FRONT_MIN,
    BGFX_TOPOLOGY_SORT_DISTANCE_BACK_TO_FRONT_AVG,
    BGFX_TOPOLOGY_SORT_DISTANCE_BACK_TO_FRONT_MAX,

    BGFX_TOPOLOGY_SORT_COUNT
) = map(topology_sort, range(13))

# view_mode
view_mode = enum_type
(
    BGFX_VIEW_MODE_DEFAULT,
    BGFX_VIEW_MODE_SEQUENTIAL,
    BGFX_VIEW_MODE_DEPTH_ASCENDING,
    BGFX_VIEW_MODE_DEPTH_DESCENDING,

    BGFX_VIEW_MODE_CCOUNT
) = map(view_mode, range(5))

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

class bgfx_dynamic_index_buffer_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_dynamic_vertex_buffer_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_frame_buffer_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_index_buffer_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_indirect_buffer_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_occlusion_query_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_program_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_shader_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_texture_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_uniform_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_vertex_buffer_handle(Structure):
    _fields_ = [("idx", c_uint16)]

class bgfx_vertex_decl_handle(Structure):
    _fields_ = [("idx", c_uint16)]

RELEASEFUNC = CFUNCTYPE(None, c_void_p, c_void_p)

def bgfx_release_fn(ptr, user_data):
    return

class bgfx_memory(Structure):
    _fields_ = [("data", POINTER(c_uint8)),
                ("size", c_uint32)]

class bgfx_transform(Structure):
    _fields_ = [("data", POINTER(c_float)),
                ("num", c_uint16)]

bgfx_view_id = c_uint16

class bgfx_view_stats(Structure):
    _fields_ = [("name", c_char * 256),
                ("view", bgfx_view_id),
                ("cpuTimeElapsed", c_int64),
                ("gpuTimeElapsed", c_int64)]

class bgfx_encoder_stats(Structure):
    _fields_ = [("cpuTimeBegin", c_int64),
                ("cpuTimeEnd", c_int64)]

class bgfx_stats(Structure):
    _fields_ = [
    ("cpuTimeFrame", c_int64),
    ("cpuTimeBegin", c_int64),
    ("cpuTimeEnd", c_int64),
    ("cpuTimerFreq", c_int64),

    ("gpuTimeBegin", c_int64),
    ("gpuTimeEnd", c_int64),
    ("gpuTimerFreq", c_int64),

    ("waitRender", c_int64),
    ("waitSubmit", c_int64),

    ("numDraw", c_uint32),
    ("numCompute", c_uint32),
    ("numBlit", c_uint32),
    ("maxGpuLatency", c_uint32),

    ("numDynamicIndexBuffers", c_uint16),
    ("numDynamicVertexBuffers", c_uint16),
    ("numFrameBuffers", c_uint16),
    ("numIndexBuffers", c_uint16),
    ("numOcclusionQueries", c_uint16),
    ("numPrograms", c_uint16),
    ("numShaders", c_uint16),
    ("numTextures", c_uint16),
    ("numUniforms", c_uint16),
    ("numVertexBuffers", c_uint16),
    ("numVertexDecls", c_uint16),

    ("textureMemoryUsed", c_int64),
    ("rtMemoryUsed", c_int64),
    ("transientVbUsed", c_uint32),
    ("transientIbUsed", c_uint32),

    ("numPrims", c_uint32 * BGFX_TOPOLOGY_COUNT.value),

    ("gpuMemoryMax", c_int64),
    ("gpuMemoryUsed", c_int64),

    ("width", c_uint16),
    ("height", c_uint16),
    ("textWidth", c_uint16),
    ("textHeight", c_uint16),

    ("numViews", c_uint16),
    ("viewStats", POINTER(bgfx_view_stats)),

    ("numEncoders", c_uint8),
    ("encoderStats", POINTER(bgfx_encoder_stats))]

class vertex_decl(Structure):
    _fields_ = [("hash", c_uint32),
                ("stride", c_uint16),
                ("offset", c_uint16 * BGFX_ATTRIB_COUNT.value),
                ("attributes", c_uint16 * BGFX_ATTRIB_COUNT.value)]


class bgfx_transient_index_buffer(Structure):
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

class bgfx_instance_data_buffer(Structure):
    _fields_ = [
        ("data", c_uint8),
        ("size", c_uint32),
        ("offset", c_uint32),
        ("num", c_uint32),
        ("stride", c_uint16),
        ("handle", bgfx_vertex_buffer_handle)
    ]

class texture_info(Structure):
    _fields_ = [
        ("format", bgfx_texture_format),
        ("storageSize", c_uint32),
        ("width", c_uint16),
        ("height", c_uint16),
        ("depth", c_uint16),
        ("numLayers", c_uint16),
        ("numMips", c_uint8),
        ("bitsPerPixel", c_uint8),
        ("cubeMap", c_bool)
    ]

class uniform_info(Structure):
    _fields_ = [
        ("name", c_char * 256),
        ("type", bgfx_uniform_type),
        ("num", c_uint16)
    ]

class attachment(Structure):
    _fields_ = [
        ("access", bgfx_access),
        ("handle", bgfx_texture_handle),
        ("mip", c_uint16),
        ("layer", c_uint16),
        ("resolve", c_uint8)
    ]

class caps_gpu(Structure):
    _fields_ = [
        ("vendorId", c_uint16),
        ("deviceId", c_uint16)
    ]

class cap_limits(Structure):
    _fields_ = [
        ("maxDrawCalls", c_uint32),
        ("maxBlits", c_uint32),
        ("maxTextureSize", c_uint32),
        ("maxTextureLayers", c_uint32),
        ("maxViews", c_uint32),
        ("maxFrameBuffers", c_uint32),
        ("maxFBAttachments", c_uint32),
        ("maxPrograms", c_uint32),
        ("maxShaders", c_uint32),
        ("maxTextures", c_uint32),
        ("maxTextureSamplers", c_uint32),
        ("maxComputeBindings", c_uint32),
        ("maxVertexDecls", c_uint32),
        ("maxVertexStreams", c_uint32),
        ("maxIndexBuffers", c_uint32),
        ("maxVertexBuffers", c_uint32),
        ("maxDynamicIndexBuffers", c_uint32),
        ("maxDynamicVertexBuffers", c_uint32),
        ("maxUniforms", c_uint32),
        ("maxOcclusionQueries", c_uint32),
        ("maxEncoders", c_uint32),
        ("transientVbSize", c_uint32),
        ("transientIbSize", c_uint32)
    ]

class caps(Structure):
    _fields_ = [
        ("rendererType", bgfx_renderer_type),
        ("supported", c_uint64),
        ("vendorId", c_uint16),
        ("deviceId", c_uint16),
        ("homogeneousDepth", c_bool),
        ("originBottomLeft", c_bool),
        ("numGPUs", c_uint8),
        ("gpu", caps_gpu * 4),
        ("limits", cap_limits),
        ("formats", c_uint16 * BGFX_TEXTURE_FORMAT_COUNT.value)
    ]

# bgfx_fatal
bgfx_fatal = enum_type
(
    BGFX_FATAL_DEBUG_CHECK,
    BGFX_FATAL_INVALID_SHADER,
    BGFX_FATAL_UNABLE_TO_INITIALIZE,
    BGFX_FATAL_UNABLE_TO_CREATE_TEXTURE,
    BGFX_FATAL_DEVICE_LOST,

    BGFX_FATAL_COUNT
) = map(bgfx_fatal, range(6))

#fatal = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s), c_char_p, c_uint16, c_int, c_char_p)
#trace_vargs = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s), c_char_p, c_uint16, c_char_p) # BUG va_list _argList
#profiler_begin = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s), c_char_p, c_uint32, c_char_p, c_uint16)
#profiler_begin_literal = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s), c_char_p, c_uint32, c_char_p, c_uint16)
#profiler_end = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s))
#cache_read_size = CFUNCTYPE(c_uint32, POINTER(bgfx_callback_interface_s), c_uint64)
#cache_read = CFUNCTYPE(c_bool, POINTER(bgfx_callback_interface_s), c_uint64, c_void_p, c_uint32)
#cache_write = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s), c_uint64, c_void_p, c_uint32)
#screen_shot = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s), c_char_p, c_uint32, c_uint32, c_uint32, c_void_p, c_uint32, c_bool)
#capture_begin = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s), c_uint32, c_uint32, c_uint32, c_int, c_bool)
#capture_end = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s))
#capture_frame = CFUNCTYPE(None, POINTER(bgfx_callback_interface_s), c_void_p, c_uint32)

#class bgfx_callback_vtbl_s(Structure):
#    _fields_ = [
#        ("fatal", fatal)
#        ("trace_vargs", trace_vargs)
#        ("profiler_begin", profiler_begin)
#        ("profiler_begin_literal", profiler_begin_literal)
#        ("profiler_end", profiler_end)
#        ("cache_read_size", cache_read_size)
#        ("cache_read", cache_read)
#        ("cache_write", cache_write)
#        ("screen_shot", screen_shot)
#        ("capture_begin", capture_begin)
#        ("capture_end", capture_end)
#        ("capture_frame", capture_frame)
#    ]

#class bgfx_callback_interface_s(Structure):
#    _fields_ = [
#        ("vtbl", POINTER(bgfx_callback_vtbl_s))
#    ]

class bgfx_callback_interface_t(Structure):
    _fields_ = []

#realloc = CFUNCTYPE(c_void_p, POINTER(bgfx_allocator_interface_s), c_void_p, c_size_t, c_size_t, c_char_p, c_uint32)
#
#class bgfx_allocator_interface_s(Structure):
#    _fields_ = [
#        ("realloc", realloc)
#    ]

class bgfx_allocator_interface_t(Structure):
    _fields_ = []

class bgfx_platform_data(Structure):
    _fields_ = [
        ("ndt", c_void_p),
        ("nwh", c_void_p),
        ("context", c_void_p),
        ("backBuffer", c_void_p),
        ("backBufferDS", c_void_p)
    ]

class bgfx_resolution_s(Structure):
    _fields_ = [
        ("format", c_int),
        ("width", c_uint32),
        ("height", c_uint32),
        ("reset", c_uint32),
        ("numBackBuffers", c_uint8),
        ("maxFrameLatency", c_uint8)
    ]

class bgfx_init_limits_s(Structure):
    _fields_ = [
        ("maxEncoders", c_uint16),
        ("transientVbSize", c_uint32),
        ("transientIbSize", c_uint32)
    ]

# https://bkaradzic.github.io/bgfx/bgfx.html#_CPPv2N4bgfx4InitE
class bgfx_init_t(Structure):
    _fields_ = [
        ("type", c_int),
        ("vendorId", c_uint16),
        ("deviceId", c_uint16),
        ("debug", c_bool),
        ("profile", c_bool),
        
        ("platformData", bgfx_platform_data),
        ("resolution", bgfx_resolution_s),
        ("limits", bgfx_init_limits_s),
        ("callback", POINTER(bgfx_callback_interface_t)),
        ("allocator", POINTER(bgfx_allocator_interface_t))
    ]


def _bind(funcname, args=None, returns=None):
    func = getattr(_bgfx, funcname)
    func.argtypes = args
    func.restype = returns
    return func

vertex_decl_begin = _bind("bgfx_vertex_decl_begin",
    args=[POINTER(vertex_decl), bgfx_renderer_type],
    returns=None)

vertex_decl_add = _bind("bgfx_vertex_decl_add",
    args=[POINTER(vertex_decl), bgfx_attrib, c_uint8, bgfx_attrib_type, c_bool, c_bool],
    returns=None)

vertex_decl_decode = _bind("bgfx_vertex_decl_decode",
    args=[POINTER(vertex_decl), bgfx_attrib, POINTER(c_uint8), POINTER(bgfx_attrib_type), POINTER(c_bool), POINTER(c_bool)],
    returns=None)

vertex_decl_has = _bind("bgfx_vertex_decl_has",
    args=[POINTER(vertex_decl), c_uint8],
    returns=c_bool)

vertex_decl_skip = _bind("bgfx_vertex_decl_skip",
    args=[POINTER(vertex_decl), c_uint8],
    returns=None)

vertex_decl_end = _bind("bgfx_vertex_decl_end",
    args=[POINTER(vertex_decl)],
    returns=None)

vertex_pack = _bind("bgfx_vertex_pack",
    args=[POINTER(c_float), c_bool, bgfx_attrib, POINTER(vertex_decl), c_void_p, c_uint32],
    returns=None)

vertex_unpack = _bind("bgfx_vertex_unpack",
    args=[POINTER(c_float), bgfx_attrib, POINTER(vertex_decl), c_void_p, c_uint32],
    returns=None)

vertex_convert = _bind("bgfx_vertex_convert",
    args=[POINTER(vertex_decl), c_void_p, POINTER(vertex_decl), c_void_p, c_uint32],
    returns=None)

weld_vertices = _bind("bgfx_weld_vertices",
    args=[POINTER(c_uint16), POINTER(vertex_decl), c_void_p, c_uint16, c_float],
    returns=c_uint16)

topology_convert = _bind("bgfx_topology_convert",
    args=[topology_convert, c_void_p, c_uint32, c_void_p, c_uint32, c_bool],
    returns=None)

topology_sort_tri_list = _bind("bgfx_topology_sort_tri_list",
    args=[topology_sort, c_void_p, c_uint32, POINTER(c_float), POINTER(c_float), c_void_p, c_uint32, c_void_p, c_uint32, c_bool],
    returns=None)

get_supported_renderers = _bind("bgfx_get_supported_renderers",
    args=[c_uint8, POINTER(bgfx_renderer_type)],
    returns=c_uint8)

get_renderer_name = _bind("bgfx_get_renderer_name",
    args=[bgfx_renderer_type],
    returns=c_char_p)

init_ctor = _bind("bgfx_init_ctor",
             args=[POINTER(bgfx_init_t)],
             returns=None)

# bgfx_init
# https://bkaradzic.github.io/bgfx/bgfx.html#_CPPv2N4bgfx4initERK4Init
init = _bind("bgfx_init",
             args=[POINTER(bgfx_init_t)],
             returns=c_bool)

shutdown = _bind("bgfx_shutdown")

reset = _bind("bgfx_reset",
              args=[c_uint32, c_uint32, c_uint32, bgfx_texture_format])

class bgfx_encoder(Structure):
    _fields_ = []

#begin = _bind("bgfx_begin",
#    args=[],
#    returns=POINTER(bgfx_encoder))

#end = _bind("bgfx_end",
#    args=[POINTER(bgfx_encoder)],
#    returns=None)  

frame = _bind("bgfx_frame",
              args=[c_bool],
              returns=c_uint32)

get_renderer_type = _bind("bgfx_get_renderer_type", 
    args=[],
    returns=bgfx_renderer_type)

get_caps = _bind("bgfx_get_caps",
    args=[],
    returns=POINTER(caps))

get_stats = _bind("bgfx_get_stats",
    args=[],
    returns=POINTER(bgfx_stats))

alloc = _bind("bgfx_alloc",
    args=[c_uint32],
    returns=POINTER(bgfx_memory))

copy = _bind("bgfx_copy",
    args=[c_void_p, c_uint32],
    returns=POINTER(bgfx_memory))

make_ref = _bind("bgfx_make_ref",
    args=[c_void_p, c_uint32],
    returns=POINTER(bgfx_memory))

make_ref_release = _bind("bgfx_make_ref_release",
    args=[c_void_p, c_uint32, RELEASEFUNC, c_void_p],
    returns=POINTER(bgfx_memory))

set_debug = _bind("bgfx_set_debug",
    args=[c_uint32],
    returns=None)

dbg_text_clear = _bind("bgfx_dbg_text_clear",
    args=[c_uint8, c_bool])

dbg_text_printf = _bind("bgfx_dbg_text_printf",
    args=[c_uint16, c_uint16, c_uint8, c_char_p])

dbg_text_image = _bind("bgfx_dbg_text_image", 
    args=[c_uint16, c_uint16, c_uint16, c_uint16, c_void_p, c_uint16])

dbg_text_vprintf = _bind("bgfx_dbg_text_vprintf",
    args=[c_uint16, c_uint16, c_uint8, c_char_p],
    returns=None)

dbg_text_image = _bind("bgfx_dbg_text_image",
    args=[c_uint16, c_uint16, c_uint16, c_uint16, c_void_p, c_uint16],
    returns=None)

create_index_buffer = _bind("bgfx_create_index_buffer", 
    args=[POINTER(bgfx_memory), c_uint16], 
    returns=bgfx_index_buffer_handle)

set_index_buffer_name = _bind("bgfx_set_index_buffer_name",
    args=[bgfx_index_buffer_handle, c_char_p, c_int32],
    returns=None)

destroy_index_buffer = _bind("bgfx_destroy_index_buffer",
    args=[bgfx_index_buffer_handle])

create_vertex_buffer = _bind("bgfx_create_vertex_buffer", 
    args=[POINTER(bgfx_memory), POINTER(vertex_decl), c_uint16], 
    returns=bgfx_vertex_buffer_handle)

set_vertex_buffer_name = _bind("bgfx_set_vertex_buffer_name",
    args=[bgfx_vertex_buffer_handle, c_char_p, c_int32],
    returns=None)

destroy_vertex_buffer = _bind("bgfx_destroy_vertex_buffer",
    args=[bgfx_vertex_buffer_handle])

create_dynamic_index_buffer = _bind("bgfx_create_dynamic_index_buffer",
    args=[c_uint32, c_uint16],
    returns=bgfx_dynamic_index_buffer_handle)

create_dynamic_index_buffer_mem = _bind("bgfx_create_dynamic_index_buffer_mem",
    args=[POINTER(bgfx_memory), c_uint16],
    returns=bgfx_dynamic_index_buffer_handle)

update_dynamic_index_buffer = _bind("bgfx_update_dynamic_index_buffer",
    args=[bgfx_dynamic_index_buffer_handle, c_uint32, POINTER(bgfx_memory)],
    returns=None)

destroy_dynamic_index_buffer = _bind("bgfx_destroy_dynamic_index_buffer",
    args=[bgfx_dynamic_index_buffer_handle],
    returns=None)

create_dynamic_vertex_buffer = _bind("bgfx_create_dynamic_vertex_buffer",
    args=[c_uint32, POINTER(vertex_decl), c_uint16],
    returns=bgfx_dynamic_vertex_buffer_handle)

create_dynamic_vertex_buffer_mem = _bind("bgfx_create_dynamic_vertex_buffer_mem",
    args=[POINTER(bgfx_memory), POINTER(vertex_decl), c_uint16],
    returns=bgfx_dynamic_vertex_buffer_handle)

update_dynamic_vertex_buffer = _bind("bgfx_update_dynamic_vertex_buffer",
    args=[bgfx_dynamic_vertex_buffer_handle, c_uint32, POINTER(bgfx_memory)],
    returns=None)

destroy_dynamic_vertex_buffer = _bind("bgfx_destroy_dynamic_vertex_buffer",
    args=[bgfx_dynamic_vertex_buffer_handle],
    returns=None)

get_avail_transient_index_buffer = _bind("bgfx_get_avail_transient_index_buffer",
    args=[c_uint32],
    returns=c_uint32)

get_avail_transient_vertex_buffer = _bind("bgfx_get_avail_transient_vertex_buffer",
    args=[c_uint32, POINTER(vertex_decl)],
    returns=c_uint32)

get_avail_instance_data_buffer = _bind("bgfx_get_avail_instance_data_buffer",
    args=[c_uint32, c_uint16],
    returns=c_uint32)

alloc_transient_index_buffer = _bind("bgfx_alloc_transient_index_buffer",
    args=[POINTER(bgfx_transient_index_buffer), c_uint32],
    returns=None)

alloc_transient_vertex_buffer = _bind("bgfx_alloc_transient_vertex_buffer",
    args=[POINTER(transient_vertex_buffer), c_uint32, POINTER(vertex_decl)],
    returns=None)

alloc_transient_buffers = _bind("bgfx_alloc_transient_buffers", 
    args=[POINTER(transient_vertex_buffer), POINTER(vertex_decl), c_uint32, POINTER(bgfx_transient_index_buffer), c_uint32], 
    returns=c_bool)

alloc_instance_data_buffer = _bind("bgfx_alloc_instance_data_buffer",
    args=[POINTER(bgfx_instance_data_buffer), c_uint32, c_uint16],
    returns=None)

create_indirect_buffer = _bind("bgfx_create_indirect_buffer",
    args=[c_uint32],
    returns=bgfx_indirect_buffer_handle)

destroy_indirect_buffer = _bind("bgfx_destroy_indirect_buffer",
    args=[bgfx_indirect_buffer_handle],
    returns=None)

create_shader = _bind("bgfx_create_shader",
    args=[POINTER(bgfx_memory)], 
    returns=bgfx_shader_handle)

get_shader_uniforms = _bind("bgfx_get_shader_uniforms",
    args=[bgfx_shader_handle, POINTER(bgfx_uniform_handle), c_uint16],
    returns=c_uint16)

get_uniform_info = _bind("bgfx_get_uniform_info",
    args=[bgfx_uniform_handle, POINTER(uniform_info)],
    returns=None)

set_shader_name = _bind("bgfx_set_shader_name",
    args=[bgfx_shader_handle, c_char_p, c_int32],
    returns=None)

destroy_shader = _bind("bgfx_destroy_shader",
    args=[bgfx_shader_handle],
    returns=None)

create_program = _bind("bgfx_create_program", 
    args=[bgfx_shader_handle, bgfx_shader_handle, c_bool], 
    returns=bgfx_program_handle)

create_compute_program = _bind("bgfx_create_compute_program",
    args=[bgfx_shader_handle, c_bool],
    returns=bgfx_program_handle)

destroy_program = _bind("bgfx_destroy_program", 
    args=[bgfx_program_handle],
    returns=None)

is_texture_valid = _bind("bgfx_is_texture_valid",
    args=[c_uint16, c_bool, c_uint16, bgfx_texture_format, c_uint64],
    returns=c_bool)

calc_texture_size = _bind("bgfx_calc_texture_size",
    args=[POINTER(texture_info), c_uint16, c_uint16, c_uint16, c_bool, c_bool, c_uint16, bgfx_texture_format],
    returns=None)

create_texture = _bind("bgfx_create_texture",
    args=[POINTER(bgfx_memory), c_uint64, c_uint8, POINTER(texture_info)],
    returns=bgfx_texture_handle)

create_texture_2d = _bind("bgfx_create_texture_2d",
    args=[c_uint16, c_uint16, c_bool, c_uint16, bgfx_texture_format, c_uint64, POINTER(bgfx_memory)],
    returns=bgfx_texture_handle)

create_texture_2d_scaled = _bind("bgfx_create_texture_2d_scaled",
    args=[backbuffer_ratio, c_bool, c_uint16, bgfx_texture_format, c_uint64],
    returns=bgfx_texture_handle)

create_texture_3d = _bind("bgfx_create_texture_3d",
    args=[c_uint16, c_uint16, c_uint16, c_bool, bgfx_texture_format, c_uint64, POINTER(bgfx_memory)],
    returns=bgfx_texture_handle)

create_texture_cube = _bind("bgfx_create_texture_cube",
    args=[c_uint16, c_bool, c_uint16, bgfx_texture_format, c_uint64, POINTER(bgfx_memory)],
    returns=bgfx_texture_handle)

update_texture_2d = _bind("bgfx_update_texture_2d",
    args=[bgfx_texture_handle, c_uint16, c_uint8, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(bgfx_memory), c_uint16],
    returns=None)

update_texture_3d = _bind("bgfx_update_texture_3d",
    args=[bgfx_texture_handle, c_uint8, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(bgfx_memory)],
    returns=None)

update_texture_cube = _bind("bgfx_update_texture_cube",
    args=[bgfx_texture_handle, c_uint16, c_uint8, c_uint8, c_uint16, c_uint16, c_uint16, c_uint16, POINTER(bgfx_memory), c_uint16],
    returns=None)

read_texture = _bind("bgfx_read_texture",
    args=[bgfx_texture_handle, c_void_p, c_uint8],
    returns=c_uint32)

set_texture_name = _bind("bgfx_set_texture_name",
    args=[bgfx_texture_handle],
    returns=None)

destroy_texture = _bind("bgfx_destroy_texture",
    args=[bgfx_texture_handle],
    returns=None)

create_frame_buffer = _bind("bgfx_create_frame_buffer",
    args=[c_uint16, c_uint16, bgfx_texture_format, c_uint64],
    returns=bgfx_frame_buffer_handle)

set_frame_buffer_name = _bind("bgfx_set_frame_buffer_name",
    args=[bgfx_frame_buffer_handle, c_char_p, c_int32],
    returns=None)

create_frame_buffer_scaled = _bind("bgfx_create_frame_buffer_scaled",
    args=[backbuffer_ratio, bgfx_texture_format, c_uint64],
    returns=bgfx_frame_buffer_handle)

create_frame_buffer_from_handles = _bind("bgfx_create_frame_buffer_from_handles",
    args=[c_uint8, POINTER(bgfx_texture_handle), c_bool],
    returns=bgfx_frame_buffer_handle)

create_frame_buffer_from_attachment = _bind("bgfx_create_frame_buffer_from_attachment",
    args=[c_uint8, POINTER(attachment), c_bool],
    returns=bgfx_frame_buffer_handle)

create_frame_buffer_from_nwh = _bind("bgfx_create_frame_buffer_from_nwh",
    args=[c_void_p, c_uint16, c_uint16, bgfx_texture_format, bgfx_texture_format],
    returns=bgfx_frame_buffer_handle)

get_texture = _bind("bgfx_get_texture",
    args=[bgfx_frame_buffer_handle, c_uint8],
    returns=bgfx_texture_handle)

destroy_frame_buffer = _bind("bgfx_destroy_frame_buffer",
    args=[bgfx_frame_buffer_handle],
    returns=None)

create_uniform = _bind("bgfx_create_uniform", 
    args=[c_char_p, bgfx_uniform_type, c_uint16], 
    returns=bgfx_uniform_handle)

destroy_uniform = _bind("bgfx_destroy_uniform", 
    args=[bgfx_uniform_handle],
    returns=None)

create_occlusion_query = _bind("bgfx_create_occlusion_query",
    args=[],
    returns=bgfx_occlusion_query_handle)

get_result = _bind("bgfx_get_result",
    args=[bgfx_occlusion_query_handle, POINTER(c_int32)],
    returns=occlusion_query_result)

destroy_occlusion_query = _bind("bgfx_destroy_occlusion_query",
    args=[bgfx_occlusion_query_handle],
    returns=None)

set_palette_color = _bind("bgfx_set_palette_color",
    args=[c_uint8, POINTER(c_float)],
    returns=None)

set_view_name = _bind("bgfx_set_view_name",
    args=[bgfx_view_id, c_char_p],
    returns=None)

set_view_rect = _bind("bgfx_set_view_rect",
    args=[bgfx_view_id, c_uint16, c_uint16, c_uint16, c_uint16],
    returns=None)

set_view_rect_auto = _bind("bgfx_set_view_rect_auto",
    args=[bgfx_view_id, c_uint16, c_uint16, backbuffer_ratio],
    returns=None)

set_view_scissor = _bind("bgfx_set_view_scissor",
    args=[bgfx_view_id, c_uint16, c_uint32, c_float, c_uint8],
    returns=None)

set_view_clear = _bind("bgfx_set_view_clear",
    args=[bgfx_view_id, c_uint16, c_uint32, c_float, c_uint8],
    returns=None)

set_view_clear_mrt = _bind("bgfx_set_view_clear_mrt",
    args=[bgfx_view_id, c_uint16, c_float, c_uint8, c_uint8, c_uint8, c_uint8, c_uint8, c_uint8, c_uint8, c_uint8, c_uint8],
    returns=None)

set_view_mode = _bind("bgfx_set_view_mode",
    args=[bgfx_view_id, view_mode],
    returns=None)

set_view_frame_buffer = _bind("bgfx_set_view_frame_buffer",
    args=[bgfx_view_id, bgfx_frame_buffer_handle],
    returns=None)

set_view_transform = _bind("bgfx_set_view_transform",
    args=[bgfx_view_id, c_void_p, c_void_p],
    returns=None)

set_view_order = _bind("bgfx_set_view_order",
    args=[bgfx_view_id, c_uint16, POINTER(bgfx_view_id)],
    returns=None)

reset_view = _bind("bgfx_reset_view",
    args=[bgfx_view_id],
    returns=None)

set_marker = _bind("bgfx_set_marker",
    args=[c_char_p],
    returns=None)

set_state = _bind("bgfx_set_state",
    args=[c_uint64, c_uint32],
    returns=None)

set_condition = _bind("bgfx_set_condition",
    args=[c_uint64, c_uint32],
    returns=None)

set_stencil = _bind("bgfx_set_stencil",
    args=[c_uint32, c_uint32],
    returns=None)

set_scissor = _bind("bgfx_set_scissor",
    args=[c_uint16, c_uint16, c_uint16, c_uint16],
    returns=c_uint16)

set_scissor_cache = _bind("bgfx_set_scissor_cached",
    args=[c_uint16],
    returns=None)

set_transform = _bind("bgfx_set_transform",
    args=[c_void_p, c_uint16],
    returns=c_uint32)

alloc_transform = _bind("bgfx_alloc_transform",
    args=[POINTER(bgfx_transform), c_uint16],
    returns=c_uint32)

set_transform_cached = _bind("bgfx_set_transform_cached",
    args=[c_uint32, c_uint16],
    returns=None)

set_uniform = _bind("bgfx_set_uniform",
    args=[bgfx_uniform_handle, c_void_p, c_uint16],
    returns=None)

set_index_buffer = _bind("bgfx_set_index_buffer", 
    args=[bgfx_index_buffer_handle, c_uint32, c_uint32],
    returns=None)

set_dynamic_index_buffer = _bind("bgfx_set_dynamic_index_buffer",
    args=[bgfx_dynamic_index_buffer_handle, c_uint32, c_uint32],
    returns=None)

set_transient_index_buffer = _bind("bgfx_set_transient_index_buffer", 
    args=[POINTER(bgfx_transient_index_buffer), c_uint32, c_uint32],
    returns=None)

set_vertex_buffer = _bind("bgfx_set_vertex_buffer", 
    args=[c_uint8, bgfx_vertex_buffer_handle, c_uint32, c_uint32],
    returns=None)

set_dynamic_vertex_buffer = _bind("bgfx_set_dynamic_vertex_buffer",
    args=[c_uint8, POINTER(bgfx_dynamic_vertex_buffer_handle), c_uint32, c_uint32],
    returns=None)

set_transient_vertex_buffer = _bind("bgfx_set_transient_vertex_buffer", 
    args=[c_uint8, POINTER(transient_vertex_buffer), c_uint32, c_uint32],
    returns=None)

set_vertex_count = _bind("bgfx_set_vertex_count",
    args=[c_uint32],
    returns=None)

set_instance_data_buffer = _bind("bgfx_set_instance_data_buffer",
    args=[POINTER(bgfx_instance_data_buffer), c_uint32, c_uint32],
    returns=None)

set_instance_data_from_vertex_buffer = _bind("bgfx_set_instance_data_from_vertex_buffer",
    args=[bgfx_vertex_buffer_handle, c_uint32, c_uint32],
    returns=None)

set_instance_data_from_dynamic_vertex_buffer = _bind("bgfx_set_instance_data_from_dynamic_vertex_buffer",
	args=[bgfx_dynamic_vertex_buffer_handle, c_uint32, c_uint32],
	returns=None)

set_instance_count = _bind("bgfx_set_instance_count",
	args=[c_uint32],
	returns=None)

set_texture = _bind("bgfx_set_texture",
	args=[c_uint8, bgfx_uniform_handle, bgfx_texture_handle, c_uint32],
	returns=None)

touch = _bind("bgfx_touch",
	args=[bgfx_view_id],
	returns=None)

submit = _bind("bgfx_submit",
	args=[bgfx_view_id, bgfx_program_handle, c_uint32, c_bool],
	returns=None)

submit_occlusion_query = _bind("bgfx_submit_occlusion_query",
	args=[bgfx_view_id, bgfx_program_handle, bgfx_occlusion_query_handle, c_uint32, c_bool],
	returns=None)

submit_indirect = _bind("bgfx_submit_indirect",
	args=[bgfx_view_id, bgfx_program_handle, bgfx_indirect_buffer_handle, c_uint16, c_uint16, c_uint32, c_bool],
	returns=None)

set_image = _bind("bgfx_set_image",
	args=[c_uint8, bgfx_texture_handle, c_uint8, bgfx_access, bgfx_texture_format],
	returns=None)

set_compute_index_buffer = _bind("bgfx_set_compute_index_buffer",
	args=[c_uint8, bgfx_index_buffer_handle, bgfx_access],
	returns=None)

set_compute_vertex_buffer = _bind("bgfx_set_compute_vertex_buffer",
	args=[c_uint8, bgfx_vertex_buffer_handle, bgfx_access],
	returns=None)

set_compute_dynamic_index_buffer = _bind("bgfx_set_compute_dynamic_index_buffer",
	args=[c_uint8, bgfx_dynamic_index_buffer_handle, bgfx_access],
	returns=None)

set_compute_dynamic_vertex_buffer = _bind("bgfx_set_compute_dynamic_vertex_buffer",
	args=[c_uint8, bgfx_dynamic_vertex_buffer_handle, bgfx_access],
	returns=None)

set_compute_indirect_buffer = _bind("bgfx_set_compute_indirect_buffer",
	args=[c_uint8, bgfx_indirect_buffer_handle, bgfx_access],
	returns=None)

dispatch = _bind("bgfx_dispatch",
	args=[bgfx_view_id, bgfx_program_handle, c_uint32, c_uint32, c_uint32],
	returns=None)

dispatch_indirect = _bind("bgfx_dispatch_indirect",
	args=[bgfx_view_id, bgfx_program_handle, bgfx_indirect_buffer_handle, c_uint16, c_uint16],
	returns=None)

discard = _bind("bgfx_discard",
	args=[c_void_p],
	returns=None)

blit = _bind("bgfx_blit",
	args=[bgfx_view_id, bgfx_texture_handle, c_uint8, c_uint16, c_uint16, c_uint16, bgfx_texture_handle, c_uint8, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16],
	returns=None)

encoder_set_marker = _bind("bgfx_encoder_set_marker",
	args=[POINTER(bgfx_encoder), POINTER(c_char)],
	returns=None)

encoder_set_state = _bind("bgfx_encoder_set_state",
	args=[POINTER(bgfx_encoder), c_uint64, c_uint32],
	returns=None)

encoder_set_condition = _bind("bgfx_encoder_set_condition",
	args=[POINTER(bgfx_encoder), bgfx_occlusion_query_handle, c_bool],
	returns=None)

encoder_set_stencil = _bind("bgfx_encoder_set_stencil",
	args=[POINTER(bgfx_encoder), c_uint32, c_uint32],
	returns=None)

encoder_set_scissor = _bind("bgfx_encoder_set_scissor",
	args=[POINTER(bgfx_encoder), c_uint16, c_uint16, c_uint16, c_uint16],
	returns=c_uint16)

encoder_set_scissor_cached = _bind("bgfx_encoder_set_scissor_cached",
	args=[POINTER(bgfx_encoder), c_uint16],
	returns=None)

encoder_set_transform = _bind("bgfx_encoder_set_transform",
	args=[POINTER(bgfx_encoder), POINTER(c_void_p), c_uint16],
	returns=c_uint32)

encoder_alloc_transform = _bind("bgfx_encoder_alloc_transform",
	args=[POINTER(bgfx_encoder), POINTER(bgfx_transform), c_uint16],
	returns=c_uint32)

encoder_set_transform_cached = _bind("bgfx_encoder_set_transform_cached",
	args=[POINTER(bgfx_encoder), c_uint32, c_uint16],
	returns=None)

encoder_set_uniform = _bind("bgfx_encoder_set_uniform",
	args=[POINTER(bgfx_encoder), bgfx_uniform_handle, POINTER(c_void_p), c_uint16],
	returns=None)

encoder_set_index_buffer = _bind("bgfx_encoder_set_index_buffer",
	args=[POINTER(bgfx_encoder), bgfx_index_buffer_handle, c_uint32, c_uint32],
	returns=None)

encoder_set_dynamic_index_buffer = _bind("bgfx_encoder_set_dynamic_index_buffer",
	args=[POINTER(bgfx_encoder), bgfx_dynamic_index_buffer_handle, c_uint32, c_uint32],
	returns=None)

encoder_set_transient_index_buffer = _bind("bgfx_encoder_set_transient_index_buffer",
	args=[POINTER(bgfx_encoder), POINTER(bgfx_transient_index_buffer), c_uint32, c_uint32],
	returns=None)

encoder_set_vertex_buffer = _bind("bgfx_encoder_set_vertex_buffer",
	args=[POINTER(bgfx_encoder), c_uint8, bgfx_vertex_buffer_handle, c_uint32, c_uint32],
	returns=None)

encoder_set_dynamic_vertex_buffer = _bind("bgfx_encoder_set_dynamic_vertex_buffer",
	args=[POINTER(bgfx_encoder), c_uint8, bgfx_dynamic_vertex_buffer_handle, c_uint32, c_uint32],
	returns=None)

encoder_set_transient_vertex_buffer = _bind("bgfx_encoder_set_transient_vertex_buffer",
	args=[POINTER(bgfx_encoder), c_uint8, POINTER(bgfx_transient_index_buffer), c_uint32, c_uint32],
	returns=None)

encoder_set_vertex_count = _bind("bgfx_encoder_set_vertex_count",
	args=[POINTER(bgfx_encoder), c_uint32],
	returns=None)

encoder_set_instance_data_buffer = _bind("bgfx_encoder_set_instance_data_buffer",
	args=[POINTER(bgfx_encoder), POINTER(bgfx_instance_data_buffer), c_uint32, c_uint32],
	returns=None)

encoder_set_instance_data_from_vertex_buffer = _bind("bgfx_encoder_set_instance_data_from_vertex_buffer",
	args=[POINTER(bgfx_encoder), bgfx_vertex_buffer_handle, c_uint32, c_uint32],
	returns=None)

encoder_set_instance_data_from_dynamic_vertex_buffer = _bind("bgfx_encoder_set_instance_data_from_dynamic_vertex_buffer",
	args=[POINTER(bgfx_encoder), bgfx_dynamic_vertex_buffer_handle, c_uint32, c_uint32],
	returns=None)

encoder_set_texture = _bind("bgfx_encoder_set_texture",
	args=[POINTER(bgfx_encoder), c_uint8, bgfx_uniform_handle, bgfx_texture_handle, c_uint32],
	returns=None)

encoder_touch = _bind("bgfx_encoder_touch",
	args=[POINTER(bgfx_encoder), bgfx_view_id],
	returns=None)

encoder_submit = _bind("bgfx_encoder_submit",
	args=[POINTER(bgfx_encoder), bgfx_view_id, bgfx_program_handle, c_uint32, c_bool],
	returns=None)

encoder_submit_occlusion_query = _bind("bgfx_encoder_submit_occlusion_query",
	args=[POINTER(bgfx_encoder), bgfx_view_id, bgfx_program_handle, bgfx_occlusion_query_handle, c_uint32, c_bool],
	returns=None)

encoder_submit_indirect = _bind("bgfx_encoder_submit_indirect",
	args=[POINTER(bgfx_encoder), bgfx_view_id, bgfx_program_handle, bgfx_indirect_buffer_handle, c_uint16, c_uint16, c_uint32, c_bool],
	returns=None)

encoder_set_image = _bind("bgfx_encoder_set_image",
	args=[POINTER(bgfx_encoder), c_uint8, bgfx_texture_handle, c_uint8, bgfx_access, bgfx_texture_format],
	returns=None)

encoder_set_compute_index_buffer = _bind("bgfx_encoder_set_compute_index_buffer",
	args=[POINTER(bgfx_encoder), c_uint8, bgfx_index_buffer_handle, bgfx_access],
	returns=None)

encoder_set_compute_vertex_buffer = _bind("bgfx_encoder_set_compute_vertex_buffer",
	args=[POINTER(bgfx_encoder), c_uint8, bgfx_vertex_buffer_handle, bgfx_access],
	returns=None)

encoder_set_compute_dynamic_index_buffer = _bind("bgfx_encoder_set_compute_dynamic_index_buffer",
	args=[POINTER(bgfx_encoder), c_uint8, bgfx_dynamic_index_buffer_handle, bgfx_access],
	returns=None)

encoder_set_compute_dynamic_vertex_buffer = _bind("bgfx_encoder_set_compute_dynamic_vertex_buffer",
	args=[POINTER(bgfx_encoder), c_uint8, bgfx_dynamic_vertex_buffer_handle, bgfx_access],
	returns=None)

encoder_set_compute_indirect_buffer = _bind("bgfx_encoder_set_compute_indirect_buffer",
	args=[POINTER(bgfx_encoder), c_uint8, bgfx_indirect_buffer_handle, bgfx_access],
	returns=None)

encoder_dispatch = _bind("bgfx_encoder_dispatch",
	args=[POINTER(bgfx_encoder), bgfx_view_id, bgfx_program_handle, c_uint32, c_uint32, c_uint32],
	returns=None)

encoder_dispatch_indirect = _bind("bgfx_encoder_dispatch_indirect",
	args=[POINTER(bgfx_encoder), bgfx_view_id, bgfx_program_handle, bgfx_indirect_buffer_handle, c_uint16, c_uint16],
	returns=None)

encoder_discard = _bind("bgfx_encoder_discard",
	args=[POINTER(bgfx_encoder)],
	returns=None)

encoder_blit = _bind("bgfx_encoder_blit",
	args=[POINTER(bgfx_encoder), bgfx_view_id, bgfx_texture_handle, c_uint8, c_uint16, c_uint16, c_uint16, bgfx_texture_handle, c_uint8, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16, c_uint16],
	returns=None)

request_screen_shot = _bind("bgfx_request_screen_shot",
	args=[bgfx_frame_buffer_handle, POINTER(c_char)],
	returns=None)

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
