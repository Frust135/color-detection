import sys
from objects.camera_object import twoCameras


if __name__ == "__main__":        
    twoCameras(
        camID1=sys.argv[1],
        camID2=sys.argv[2],
        width=sys.argv[3],
        height=sys.argv[4],
        lower_color=[1, 220, 150],
        upper_color=[10, 240, 190]
    )