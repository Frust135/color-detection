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

def get_img_point(cap, img, mask):
    '''
    Función para dibujar el punto en el video, retorna el dibujo y la posición
    '''
    points = cv2.findNonZero(mask)
    position = np.mean(points, axis=0)[0]
    img_point = cv2.circle(img, (int(position[0]), int(position[1])), radius=10, color=(0, 0, 255), thickness=2)
    width_camera = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height_camera = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    cv2.circle(img, (int(width_camera/2), int(height_camera/2)), radius=1, color=(0, 0, 255), thickness=2)
    return img_point, position

def get_centimeter_position(cap, position):
    '''
    Función para calcular la posición del objeto en centimetros (asumiendo un dpi de 96px/in )
    '''
    width_camera = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height_camera = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    px_width = int(width_camera/2 - position[0])
    px_height = int(height_camera/2 - position[1])

    width_centimeters = px_width*2.54/96
    height_centimeters = px_height*2.54/96
    return [round(width_centimeters, 2), round(height_centimeters, 2)]

def open_camera_with_mask(cap, lower_color, upper_color):
    '''
    Abrir la camara aplicando una máscara
    '''
    print('#################')
    print('Opening camera...')
    while(cap.isOpened()):    
        ret, frame = cap.read()
        rgb_video = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)        

        lower_mask = np.array(lower_color)
        upper_mask = np.array(upper_color)   
        mask = cv2.inRange(rgb_video, lower_mask, upper_mask)
        res = cv2.bitwise_and(frame, frame, mask=mask)        
        # cv2.imshow('frame', frame)
        # cv2.imshow('res', res)
        if np.mean(mask) > 0:
            img_point, position = get_img_point(cap, frame, mask)
            actual_position = get_centimeter_position(cap, position)
            print('X (cm):', actual_position[0], '- Y (cm):', actual_position[1])
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