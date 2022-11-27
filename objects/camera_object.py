import cv2
import numpy as np
from threading import Thread

class cameraObject():
    def __init__(self, camID, width, height, lower_color, upper_color):
        self.camID = int(camID)
        self.width = int(width)
        self.height = int(height)
        self.lower_color = lower_color
        self.upper_color = upper_color        
        #self.open_camera_with_mask()

    def initialize_camera(self):
        '''
        Función para inicializar cámara
        '''
        # 640.0 x 480.0
        # 1280.0 x 720.0
        cap = cv2.VideoCapture(self.camID)
        camera_name = 'Camara ' + str(self.camID)
        cv2.namedWindow(camera_name)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        size_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        size_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Camera Size')
        print('Height: {0} - Width: {1}'.format(size_height, size_width))
        return cap

    def get_img_point(self, img, mask):
        '''
        Función para dibujar el punto en el video, retorna el dibujo y la posición
        '''
        points = cv2.findNonZero(mask)
        position = np.mean(points, axis=0)[0]
        img_point = cv2.circle(img, (int(position[0]), int(position[1])), radius=10, color=(0, 0, 255), thickness=2)
        width_camera = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height_camera = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        cv2.circle(img, (int(width_camera/2), int(height_camera/2)), radius=1, color=(0, 0, 255), thickness=2)
        return img_point, position

    def get_centimeter_position(self, position):
        '''
        Función para calcular la posición del objeto en centimetros (asumiendo un dpi de 96px/in )
        '''
        width_camera = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height_camera = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        px_width = int(width_camera/2 - position[0])
        px_height = int(height_camera/2 - position[1])

        width_centimeters = px_width*2.54/96
        height_centimeters = px_height*2.54/96
        return [round(width_centimeters, 2), round(height_centimeters, 2)]

    def open_camera_with_mask(self):
        '''
        Abrir la camara aplicando una máscara
        '''
        print('#################')
        print('Opening camera...')
        self.cap = self.initialize_camera()
        camera_name = 'Camara ' + str(self.camID)
        while(self.cap.isOpened()):            
            ret, frame = self.cap.read()
            rgb_video = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)        

            lower_mask = np.array(self.lower_color)
            upper_mask = np.array(self.upper_color)   
            mask = cv2.inRange(rgb_video, lower_mask, upper_mask)
            res = cv2.bitwise_and(frame, frame, mask=mask)        
            # cv2.imshow('frame', frame)
            # cv2.imshow('res', res)
            if np.mean(mask) > 0:
                img_point, position = self.get_img_point(frame, mask)
                actual_position = self.get_centimeter_position(position)
                print(camera_name+': X (cm):', actual_position[0], '- Y (cm):', actual_position[1])
                cv2.imshow(camera_name, img_point)
            else:
                cv2.imshow(camera_name, frame)
                print(camera_name+': Sin señal...')
            if cv2.waitKey(1) & 0xFF == ord('q'): break

        print('Closing camera...')
        self.cap.release()
        cv2.destroyAllWindows(camera_name)