#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Yeahia Sarker

"""

import cv2
from imutils.video import VideoStream
import os
import numpy as np

class object_detection_yolo:
    def __init__(self):
        self.labels_path = os.getcwd() + "/yolo/coco.names"
        self.labels = os.getcwd() + "yolo/labels"
        self.weights_path = os.getcwd() + "/yolo/yolov3.weights"
        self.config_path = os.getcwd() + "/yolo/yolov3.cfg"
        self.label_names = open(self.labels_path).read().strip().split("\n")
        self.scale = 0.00428
        self.confidence_threshold = 0.6
        self.nms_threshold = 0.004  # Non Maxima Supression Threshold Vlue
        self.net = cv2.dnn.readNetFromDarknet(self.config_path, self.weights_path)

    def yolo_object_detection(self):
        
        """This function uses non maxima supression and has time complexity.
            If your project needs more accuracy and you don't care about execution time and fps,
            you can use this function without any worries."""
            
        cap = VideoStream(src=0).start()
        layers_name = self.net.getLayerNames()
        output_layer = [layers_name[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        while True:
            frame = cap.read()
            (h, w) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
            self.net.setInput(blob)
            outputs = self.net.forward(output_layer)
            confidences = []
            boxes = []
            class_ids = []
            for output in outputs:
                for detection in output:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5 :
                        box = detection[0:4] * np.array([w, h, w, h])
                        (center_x, center_y, width, height) = box.astype("int")
                        x = int(center_x - (width / 2))
                        y = int(center_y - (height / 2))
                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)
            ind = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, self.nms_threshold)
            for i in ind:
                i = i[0]
                (x, y, w, h) = (boxes[i][0], boxes[i][1],boxes[i][2], boxes[i][3])
                cv2.rectangle(frame,(x, y), (x + w, y + h), (0, 255, 255), 2)
                label = "{}: {:.4f}".format(self.label_names[class_ids[i]], confidences[i])
                cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,255), 2)
            cv2.imshow("Object Detection Yolo", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cv2.destroyAllWindows()
        cap.stop()
if __name__ == "__main__":    
    object_detection_yolo().yolo_object_detection()