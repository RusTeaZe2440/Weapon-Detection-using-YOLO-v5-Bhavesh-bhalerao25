
import cv2

cap = cv2.VideoCapture('http://192.168.0.109:8080/video')

while True:
    ret, frame = cap.read()
    resized = cv2.resize(frame,(600,400))
    cv2.imshow("Frame", resized)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


# p3.pt exp7
# python detect.py --weights p3.pt  --img 640 --conf 0.25 --source ("http://192.168.0.105:8080/video")