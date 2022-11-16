from camera_functions import initialize_camera, open_camera_with_mask
cap = initialize_camera(640, 480)
open_camera_with_mask(cap, [50,50,100], [80,80,255])