# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:53:29 2024

@author: ghita
"""
import cv2
import numpy as np

def detectCircle():
    
    cam = cv2.VideoCapture(0)
    if cam.isOpened():
        print("Connected to camera")
        #cam.release()
        while True :
            capture, frame = cam.read()
            if capture :
                print("frame was captured")
                #cv2.imwrite('frame.jpg', frame)
                gFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                gFrame = cv2.medianBlur(gFrame,3)
                cv2.imwrite("grey.jpg",gFrame)
                rows = gFrame.shape[0]
                circles = cv2.HoughCircles(gFrame, cv2.HOUGH_GRADIENT, 1,rows/8, param1=160,param2=40,minRadius=50,maxRadius=100)
                if circles is not None:
                    circles = np.uint16(np.around(circles))
                    for i in circles[0, :]:
                        center = (i[0], i[1])
                        cv2.circle(frame,center,1,(0,100,100),3)
                        radius = i[2]
                        cv2.circle(frame,center,radius,(255,0,255),3)
                    cv2.imwrite("framee.jpg",frame)
                else :
                    print("no circle ")
                break
                
                
            else :
                print("frame capture failed")
                #cam.release()
                #break
            
            
        
    else :
        print("Connection to camera failed")