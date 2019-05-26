#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 13:34:15 2019

@author: Yeahia Sarker

"""

import cv2
import os
import numpy as np

class object_detection_yolo:
    def __init__(self):
        self.labels_path = os.getcwd() + "/yolo/coco.names"
        self.labels = os.getcwd() + "yolo/labels"
        self.weights_path = os.getcwd() + "/yolo/yolov3.weights"
        self.config_path = os.getcwd() + "/yolo/yolov3.cfg"
        self.scale = 0.00428
        self.confidence_threshold = 0.6
        self.nms_threshold = 0.004 # Non Maxima Supression Threshold Vlue
        self.net = cv2.dnn.readNetFromDarknet(self.config_path, self.weights_path)

    def object_detection(self):
        layers_name = self.net.getLayerNames()
        output_layer = [layers_name[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        while True:
            blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
            self.net.setInput(blob)
            outputs = self.net.forward(output_layer)
            confidence = []
            boxes = []
            class_ids = []
            for output in outputs:
                for detection in output:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5 :
                        box = detection[0:4] * np.array([W, H, W, H])
                        (centerX, centerY, width, height) = box.astype("int")
                        x = int(centerX - (width / 2))
                        y = int(centerY - (height / 2))
                        boxes.append([x, y, int(width), int(height)])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)
            ind = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, self.nms_threshold)
            for i in ind:
                (x, y, w, h) = (boxes[i][0], boxes[i][1],boxes[i][2], boxes[i][3])
                cv2.rectangle(frame,(x, y), (x + w, y + h), (0, 255, 255), 2)
                label = str(classes(class_id))
                cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, color, 2)
