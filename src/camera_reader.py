import cv2


class CameraNotInitializedException(Exception):
    pass


class Reader:
    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        if self.cam is None:
            raise CameraNotInitializedException()

    def read(self):
        s, r = self.cam.read()
        return r
