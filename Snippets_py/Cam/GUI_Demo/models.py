import cv2


class Camera:

    def __init__(self, cam_num):

        self.cap = cv2.VideoCapture(cam_num)
        self.cam_num = cam_num

    def open(self, width=640, height=480, fps=30):
        self.cap.set(5, fps)  #set FPS
        self.cap.set(3, width)
        self.cap.set(4, height)
        return self.cap.isOpened()

    def read(self):
        rval, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame

    def get_brightness(self):
        return self.cap.get(cv2.CAP_PROP_BRIGHTNESS)

    def set_brightness(self, value):
        self.cap.set(cv2.CAP_PROP_BRIGHTNESS, value)