import sys
from objects.camera_object import twoCameras


if __name__ == "__main__":        
    twoCameras(
        camID1=sys.argv[1],
        camID2=sys.argv[2],
        width=sys.argv[3],
        height=sys.argv[4],
        lower_color=[50, 50, 100],
        upper_color=[80, 80, 255]
    )