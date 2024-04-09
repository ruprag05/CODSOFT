import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_and_recognize_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
    
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
       
    
    return image

cap = cv2.VideoCapture(0) 
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
   
    frame_with_faces = detect_and_recognize_faces(frame)
   
    cv2.imshow('Face Detection and Recognition', frame_with_faces)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

