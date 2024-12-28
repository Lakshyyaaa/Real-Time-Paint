import HandTrackingFunctionalP as htm
import cv2 as cv
import numpy as np
import time
import os

cap = cv.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)

drawColor=(0,255,0)
brushThickness=10
eraserT=40


detector=htm.HandDetector()

xp,yp=0,0

folderPath = "Menu bar"
overlay = []
myList = os.listdir(folderPath)

for imPath in myList:
    img = cv.imread(f'{folderPath}/{imPath}')
    if img is not None:
        overlay.append(img)

header = overlay[0]
header = cv.resize(header, (1920, 336))

imgcan=np.zeros((1920,1080,3),np.uint8)

while True:
    isTrue, img = cap.read()
    img=cv.flip(img,1)
    fingers=[]
    tipIds = [4, 8, 12, 16, 20]

    img=detector.showPoints(img)
    lm=detector.returnPoints(img)

    if len(lm)!=0:
        x1,y1=lm[8][1:] #Index Finger
        x2,y2=lm[12][1:] #Middle Finger

        if (lm[tipIds[0]][1] < lm[tipIds[0] - 1][1]):
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
        # Fingers
            if (lm[tipIds[id]][2] < lm[tipIds[id] - 2][2]):
                fingers.append(1)
            else:
                fingers.append(0)

        if fingers[1] and fingers[2]:
            cv.circle(img, (x1, y1), 15, drawColor, -1)
            cv.circle(img, (x2, y2), 15, drawColor, -1)

            if y1<330:
                if 410<x1<722:
                    header=overlay[3]
                    drawColor=(150, 120, 200)

                elif 770<x1<1053:
                    header=overlay[1]
                    drawColor=(235, 206, 135)

                elif 1062<x1<1440:
                    header=overlay[2]
                    drawColor=(0, 255, 255)

                if 1471<x1<1868:
                    header=overlay[0]
                    drawColor=(0,0,0)

        if fingers[1] and fingers[2]==False:
            cv.circle(img, (x1, y1), 15, drawColor, -1)

            if xp==0 and yp==0:
                xp,yp=x1,y1

            if drawColor==(0,0,0):
                cv.line(img, (xp, yp), (x1, y1), drawColor, eraserT)
                cv.line(imgcan, (xp, yp), (x1, y1), drawColor, eraserT)

            else:
                cv.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                cv.line(imgcan, (xp, yp), (x1, y1), drawColor, brushThickness)

            xp,yp=x1,y1

    imgGray=cv.cvtColor(imgcan,cv.COLOR_BGR2GRAY)
    _,imginv=cv.threshold(imgGray,50,255,cv.THRESH_BINARY_INV)
    imginv=cv.cvtColor(imginv,cv.COLOR_GRAY2BGR)

    if img.shape != imginv.shape:
        imginv = cv.resize(imginv, (img.shape[1], img.shape[0]))
    img = cv.bitwise_and(img, imginv)

    if img.shape != imgcan.shape:
        imgcan = cv.resize(imgcan, (img.shape[1], img.shape[0]))
    img = cv.bitwise_or(img, imgcan)

    header = cv.resize(header, (1920, 336))
    img[0:336, 0:1920] = header

    imgcan = cv.resize(imgcan, (img.shape[1], img.shape[0]))
    img=cv.addWeighted(img,0.5,imgcan,0.5,2)

    cv.imshow("Image", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
