import math

def rotate_xy(mtx, rot_x, rot_y):
    sx = math.sin(rot_x)
    cx = math.cos(rot_x)
    sy = math.sin(rot_y)
    cy = math.cos(rot_y)

    mtx[0] = cy
    mtx[0] = cy;
    mtx[2] = sy;
    mtx[4] = sx*sy;
    mtx[5] = cx;
    mtx[6] = -sx*cy;
    mtx[8] = -cx*sy;
    mtx[9] = sx;
    mtx[10] = cx*cy;
    mtx[15] = 1.0;