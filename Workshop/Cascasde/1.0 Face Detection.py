import cv2

face_clsfr=cv2.CascadeClassifier('Cascades\Face & Eyes\haarcascade_frontalface_default.xml')
eye_clsfr=cv2.CascadeClassifier('Cascades\Face & Eyes\haarcascade_eye_tree_eyeglasses.xml')

camera=cv2.VideoCapture('Faces from around the world.mp4')

while(True):

    ret,img=camera.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_clsfr.detectMultiScale(gray)     #results=clsfr.predict(features)

    for (x,y,w,h) in faces:

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img,'FACE',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

        face_img=gray[y:y+w,x:x+w]
        #cv2.imshow('Face',face_img)
        eyes=eye_clsfr.detectMultiScale(face_img)

        for(ex,ey,ew,eh) in eyes:

            cv2.rectangle(img,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(255,0,0),2)
            cv2.putText(img,'EYES',(x+ex,y+ey-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)

            
            
    cv2.imshow('LIVE',img)
    cv2.waitKey(1)


