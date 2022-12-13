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

    def create_new_canvas(self, points1, points2, actual_position1, actual_position2):
        blank_image = np.zeros((self.height,self.width,3), np.uint8)
        tuple_points1 = (int(points1[0]), int(points1[1]))
        tuple_points2 = (int(points2[0]), int(points2[1]))
        cv2.circle(blank_image, (int(self.width/2), int(self.height/2)), radius=1, color=(0, 0, 255), thickness=2)
        if actual_position1:
            if tuple_points1[1] < (self.height/2): camera_position1 = 'B'
            else: camera_position1 = 'A'
            cv2.circle(blank_image, tuple_points1, radius=10, color=(0, 0, 255), thickness=2)
            cv2.putText(blank_image, '{0} - X (cm): {1} - Y (cm): {2}'.format(camera_position1 ,actual_position1[0], actual_position1[1]),
                (int(points1[0])+20, int(points1[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color=(0, 0, 255), thickness=1
            )
        if actual_position2:
            if tuple_points2[1] < (self.height/2): camera_position2 = 'B'
            else: camera_position2 = 'A'
            cv2.circle(blank_image, tuple_points2, radius=10, color=(0, 0, 255), thickness=2)
            cv2.putText(blank_image, '{0} - X (cm): {0} - Y (cm): {1}'.format(camera_position2, actual_position2[0], actual_position2[1]),
                (int(points2[0])+20, int(points2[1])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color=(0, 0, 255), thickness=1
            )
        if actual_position1 and actual_position2:
            cv2.line(blank_image, tuple_points1, tuple_points2, color=(0, 0, 255), thickness=5)
        return blank_image

    def open_camera_with_mask(self):
        import time
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
            actual_position1 = None
            actual_position2 = None
            print('###############')
            if np.mean(mask1) > 0:
                img_point1, position1 = self.get_img_point(self.cap1, frame1, mask1)
                actual_position1 = self.get_centimeter_position(self.cap1, position1)
                #print(camera_name_1+': X (cm):', actual_position1[0], '- Y (cm):', actual_position1[1])
                cv2.imshow(camera_name_1, img_point1)
            else:
                print(camera_name_1+': Sin señal...')
                cv2.imshow(camera_name_1, frame1)                
            
            if np.mean(mask2) > 0:
                img_point2, position2 = self.get_img_point(self.cap2, frame2, mask2)
                actual_position2 = self.get_centimeter_position(self.cap2, position2)
                #print(camera_name_2+': X (cm):', actual_position2[0], '- Y (cm):', actual_position2[1])
                cv2.imshow(camera_name_2, img_point2)
            else:
                print(camera_name_2+': Sin señal...')
                cv2.imshow(camera_name_2, frame2)                
            
            canvas = self.create_new_canvas(position1, position2, actual_position1, actual_position2)
            cv2.imshow('Canvas', canvas)

            if cv2.waitKey(1) & 0xFF == ord('q'): break

        print('Closing camera...')
        self.cap.release()
        cv2.destroyAllWindows()