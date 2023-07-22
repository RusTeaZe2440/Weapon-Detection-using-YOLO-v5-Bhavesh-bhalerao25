
import cv2

cap = cv2.VideoCapture('weapon detector')

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
# p4.pt (guns,shikha) exp31
# p5.pt (pistol, saif, web/pistolweb) exp12 ##(best one)##
# p6.pt (pistol, saif, robo{shama}, 17580) exp2
# p7.pt (piarol, pistol and final[data], with p5.pt) exp16

# python detect.py --weights p5.pt  --img 640 --conf 0.25 --source ("http://192.168.0.100:8080/video")


# k1.pt (knife roboflow ,shikha pgl) exp 2
# k2.pt (knife , bhavesh)
# k3.pt (knife roboflow, weight-k1) exp4, 30 epoch
# k4.pt (k3.pt) exp5, 60 epoch





