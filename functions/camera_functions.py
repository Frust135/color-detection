import cv2
import numpy as np
from matplotlib import pyplot as plt

def initialize_camera(width, height, number):
    '''
    Función para inicializar cámara
    '''
    # 640.0 x 480.0
    # 1280.0 x 720.0
    cap = cv2.VideoCapture(number)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  
    print('Camera Size')
    print('Height: {0} - Width: {1}'.format(height, width))
    return cap

def get_img_point(img, mask):
    '''
    Función para dibujar el punto en el video, retorna el dibujo y la posición
    '''
    points = cv2.findNonZero(mask)
    position = np.mean(points, axis=0)[0]
    img_point = cv2.circle(img, (int(position[0]), int(position[1])), radius=20, color=(0, 0, 255), thickness=2)
    return img_point, position

def open_camera_with_mask(cap, lower_color, upper_color):
    '''
    Abrir la camara aplicando una máscara
    '''
    print('#################')
    print('Opening camera...')
    while(cap.isOpened()):    
        ret, frame = cap.read()
        rgb_video = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_mask = np.array(lower_color)
        upper_mask = np.array(upper_color)   
        mask = cv2.inRange(rgb_video, lower_mask, upper_mask)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        
        # cv2.imshow('frame', frame)
        # cv2.imshow('res', res)
        if np.mean(mask) > 0:
            img_point, position = get_img_point(frame, mask)
            cv2.imshow('img_point', img_point)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    print('Closing camera...')
    cap.release()
    cv2.destroyAllWindows()

def open_camera_tkinter(number, width, height, lower_color, upper_color):
    try:
        width = int(width)
        height = int(height)
        lower_color = list(map(int, lower_color.split()))
        upper_color = list(map(int, upper_color.split()))
    except:
        return False
    cap = initialize_camera(width, height, number)
    open_camera_with_mask(cap, lower_color, upper_color)
    return True