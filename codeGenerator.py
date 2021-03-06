#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)

def code_generator():
    for i in range(20):
        fileName = "images/" + str(i) + ".png"
        generator = aruco.drawMarker(dictionary, i, 100)
        cv2.imwrite(fileName, generator)

code_generator()