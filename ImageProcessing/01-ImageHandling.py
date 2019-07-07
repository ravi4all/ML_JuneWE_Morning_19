# img = open('img_1.jpg','rb')
#
# data = img.read()
# print(data)
#
# img.close()

import cv2

img = cv2.imread('img_1.jpg')
# print(img.shape)
font = cv2.FONT_HERSHEY_COMPLEX
while True:
    #cv2.imshow('result', img)
    GRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img, (x,y), (w,h),(b,g,r),border_thickness
    cv2.imshow('result', GRAY)
    cv2.rectangle(img,(300,100),(450,300),(255,0,0),5)
    cv2.putText(img,'MS Dhoni',(300,100),font,2,(0,255,255),2)
    if cv2.waitKey(10) == 27:
        break
