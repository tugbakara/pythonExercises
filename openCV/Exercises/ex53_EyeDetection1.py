from cv2 import cv2

trainedClassifierFace = cv2.CascadeClassifier(r'E:\ImageProcessingdenemeleri\Trained Classifiers\haarcascade_frontalface_default.xml')
trainedClassifierEye =  cv2.CascadeClassifier(r'E:\ImageProcessingdenemeleri\Trained Classifiers\haarcascade_eye_tree_eyeglasses.xml')
myVid = cv2.VideoCapture(0)

while myVid.isOpened():
    _, frame = myVid.read()
    frameG = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = trainedClassifierFace.detectMultiScale(frameG,1.3,4)
    for (x,y,w,h) in faces:
        roiFaceG = frameG[y:y+h , x:x+w]
        roiFace = frame[y:y+h , x:x+w]
        eyes = trainedClassifierEye.detectMultiScale(roiFaceG,1.3,4)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roiFace,(ex,ey),(ex+ew,ey+eh),(0,255,255),1)
    cv2.imshow('Eye Detection',frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
myVid.release()
cv2.destroyAllWindows()

