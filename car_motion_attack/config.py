import numpy as np

CAMERA_IMG_HEIGHT = 484
CAMERA_IMG_WIDTH = 1164

# BEV_BASE_HEIGHT = int(CAMERA_IMG_HEIGHT * 1.1)
# BEV_BASE_WIDTH = CAMERA_IMG_WIDTH

BEV_BASE_HEIGHT = 968
BEV_BASE_WIDTH = 1000  # 1408

MODEL_IMG_HEIGHT = 128
MODEL_IMG_WIDTH = 256
MODEL_IMG_CH = 6

IMG_CROP_HEIGHT = 256
IMG_CROP_WIDTH = 512


PIXELS_PER_METER = 29 / 3.6576  # bev pixels / lane width
SKY_HEIGHT = 390

IMG_INPUT_SHAPE = (1, 6, MODEL_IMG_HEIGHT, MODEL_IMG_WIDTH)
IMG_INPUT_MASK_SHAPE = (1, 1, MODEL_IMG_HEIGHT, MODEL_IMG_WIDTH)
RNN_INPUT_SHAPE = (1, 512)
MODEL_DESIRE_INPUT_SHAPE = (1, 8)
MODEL_OUTPUT_SHAPE = (1, 1760)
#MODEL_OUTPUT_SHAPE = (1, 1724)

YUV_MIN = -8.68289960e-01
YUV_MAX = 4.87138199e-01

DTYPE = np.float32


"""
ROI_MAT = np.array([
        [1.25, 0., 412.0],
        [0., 1.25, 377.75],
        [0., 0., 1.]
    ]) # deagon
"""
"""
ROI_MAT = np.array(
    [[1.25, 0.0, 393.0], 
    [0.0, 1.25, 354.75],
     [0.0, 0.0, 1.0]]
)  # RAV4
"""
"""
ROI_MAT = np.array([
    [1.25, 0., 416.0],
    [0., 1.25, 377.75],
    [0., 0., 1.]
])  # deagon

ROI_MAT = np.array(
    [
        [0.990908, 0.0, 339.854187],
        [-0.006753, 1.0, 332.119049],
        [-0.000015, 0.0, 1.018190],
    ]
)  # RAV4 v0.6.6

ROI_MAT_INV = np.linalg.inv(ROI_MAT)
"""
# IMG_CENTER_WIDTH = int(160 * 1.25 + 382)
# IMG_CENTER_HEIGHT = int(80 * 1.25 + 410.75)


PLAN_PER_PREDICT = 5

LATERAL_SHIFT_OFFSET = -45
