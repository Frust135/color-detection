import sys
from objects.camera_object import cameraObject


if __name__ == "__main__":
    if (len(sys.argv) == 4):
        cameraObject(
            camID=sys.argv[1], #0 o 1
            width=sys.argv[2], # 640 o 1280
            height=sys.argv[3], # 480 o 720
            lower_color=[50, 50, 100],
            upper_color=[80, 80, 255]
        )