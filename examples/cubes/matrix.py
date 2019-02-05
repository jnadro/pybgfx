import ctypes
import math
import numpy as np

def sub(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

def cross(v1, v2):
    v1x = v1[0] 
    v1y = v1[1]
    v1z = v1[2]
    v2x = v2[0]
    v2y = v2[1]
    v2z = v2[2]
    return [
        (v1y * v2z) - (v1z * v2y),
        (v1z * v2x) - (v1x * v2z),
        (v1x * v2y) - (v1y * v2x)
    ]

def length(vec3):
    return math.sqrt(vec3[0] * vec3[0] + vec3[1] * vec3[1] + vec3[2] * vec3[2])

def normalize(vec3):
    l = length(vec3)
    return [vec3[0] / l, vec3[1] / l, vec3[2] / l]

def look_at(eye, at, up):
    """Constructs look-at matrix for right handed coordinate system."""
    view = normalize(sub(at, eye))
    right = normalize(np.cross(up, view))

    up = np.cross(view, right)

    view = (ctypes.c_float * 16)(*[right[0], up[0], view[0], 0.0,
                                   right[1], up[1], view[1], 0.0,
                                   right[2], up[2], view[2], 0.0,
                                   -np.dot(right, eye), -np.dot(up, eye), -np.dot(view, eye), 1.0])

    return view

def proj(mtx, fov_y, aspect, near, far):
    pass

def ortho(mtx, left, right, bottom, top, near, far):
    pass

def rotate_xy(mtx, rot_x, rot_y):
    sx = math.sin(rot_x)
    cx = math.cos(rot_x)
    sy = math.sin(rot_y)
    cy = math.cos(rot_y)

    mtx[0] = cy
    mtx[0] = cy
    mtx[2] = sy
    mtx[4] = sx*sy
    mtx[5] = cx
    mtx[6] = -sx*cy
    mtx[8] = -cx*sy;
    mtx[9] = sx
    mtx[10] = cx*cy
    mtx[15] = 1.0