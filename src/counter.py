import cv2
import imutils
import numpy as np
from pyimagesearch.centroidtracker import CentroidTracker


class Counter:
    CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
               "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
               "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
               "sofa", "train", "tvmonitor"]

    def __init__(self, confidence=0.3):

        self.confidence = confidence

        self.net = cv2.dnn.readNetFromCaffe('mobilenet_ssd/MobileNetSSD_deploy.prototxt',
                                            'mobilenet_ssd/MobileNetSSD_deploy.caffemodel')
        self.W = -1
        self.H = -1
        self.ct = CentroidTracker(maxDisappeared=40, maxDistance=50)

    def count(self, image):
        image = imutils.resize(image, width=500)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if self.W < 0:
            (self.H, self.W) = image.shape[:2]

        blob = cv2.dnn.blobFromImage(image, 0.007843, (self.W, self.H), 127.5)
        self.net.setInput(blob)
        detections = self.net.forward()
        cnt = 0
        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > self.confidence:
                class_idx = int(detections[0, 0, i, 1])
                if self.CLASSES[class_idx] == "person":
                    cnt += 1
        return cnt
