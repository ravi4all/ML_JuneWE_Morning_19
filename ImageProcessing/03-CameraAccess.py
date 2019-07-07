import cv2

dataset = cv2.CascadeClassifier('data.xml')
capture = cv2.VideoCapture(0)

while True:
    ret,frame = capture.read()
    if ret:
        faces = dataset.detectMultiScale(frame, 1.28)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

        cv2.imshow('result', frame)
        if cv2.waitKey(10) == 27:
            break
    else:
        print("Camera is not working")

cv2.destroyAllWindows()
capture.release()
