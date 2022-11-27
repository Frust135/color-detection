import cv2
import numpy as np

class twoCameras():
    def __init__(self, camID1, camID2, width, height, lower_color, upper_color):
        self.camID1 = int(camID1)
        self.camID2 = int(camID2)
        self.width = int(width)
        self.height = int(height)
        self.lower_color = lower_color
        self.upper_color = upper_color
        self.cap1 = self.initialize_camera(self.camID1)
        self.cap2 = self.initialize_camera(self.camID2)
        self.open_camera_with_mask()
        self.open_camera_with_mask()
        

    def initialize_camera(self, cam_id):
        '''
        Función para inicializar cámara
        '''
        cap = cv2.VideoCapture(cam_id)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        return cap

    def get_img_point(self, cap, img, mask):
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

    def get_centimeter_position(self, cap, position):
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

    def create_new_canvas(self, position1, position2):
        blank_image = np.zeros((self.height,self.width,3), np.uint8)
        cv2.circle(blank_image, (int(position1[0]), int(position1[1])), radius=10, color=(0, 0, 255), thickness=2)
        cv2.circle(blank_image, (int(position2[0]), int(position2[1])), radius=10, color=(0, 0, 255), thickness=2)
        return blank_image

    def open_camera_with_mask(self):
        '''
        Abrir la camara aplicando una máscara
        '''
        print('#################')
        print('Opening camera...')
        
        camera_name_1 = 'Camara ' + str(self.camID1)
        camera_name_2 = 'Camara ' + str(self.camID2)
        while(self.cap1.isOpened() and self.cap2.isOpened()):
            ret1, frame1 = self.cap1.read()
            rgb_video1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)

            ret2, frame2 = self.cap2.read()
            rgb_video2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

            lower_mask = np.array(self.lower_color)
            upper_mask = np.array(self.upper_color)   
            position1 = position2 = (999,999)
            mask1 = cv2.inRange(rgb_video1, lower_mask, upper_mask)
            mask2 = cv2.inRange(rgb_video2, lower_mask, upper_mask)            
            print('###############')
            if np.mean(mask1) > 0:
                img_point1, position1 = self.get_img_point(self.cap1, frame1, mask1)
                actual_position1 = self.get_centimeter_position(self.cap1, position1)
                print(camera_name_1+': X (cm):', actual_position1[0], '- Y (cm):', actual_position1[1])
                cv2.imshow(camera_name_1, img_point1)
                flag_camera1 = True
            else:
                cv2.imshow(camera_name_1, frame1)
                print(camera_name_1+': Sin señal...')
            
            if np.mean(mask2) > 0:
                img_point2, position2 = self.get_img_point(self.cap2, frame2, mask2)
                actual_position2 = self.get_centimeter_position(self.cap2, position2)
                print(camera_name_2+': X (cm):', actual_position2[0], '- Y (cm):', actual_position2[1])
                cv2.imshow(camera_name_2, img_point2)
                flag_camera2 = True
            else:
                cv2.imshow(camera_name_2, frame2)
                print(camera_name_2+': Sin señal...')
            
            canvas = self.create_new_canvas(position1, position2)
            cv2.imshow('Canvas', canvas)

            if cv2.waitKey(1) & 0xFF == ord('q'): break

        print('Closing camera...')
        self.cap.release()
        cv2.destroyAllWindows()