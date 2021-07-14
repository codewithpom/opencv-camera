import cv2
# I used this line because I have external camera.
# You do not need to use cv2.CAP_DSHOW if you do not use external camera
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
   ret, frame = cam.read()
   cv2.imshow("My Webcam", frame)
   key = cv2.waitKey(25)
   if key == ord('q'):
        break
        
