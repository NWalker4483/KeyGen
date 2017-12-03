import stream as im
import cv2
import time
from modelling import test_terra
from modelling import top_edge
from findkey import get_edge
import imutils
import numpy as np
camera=im.ConnectCam()
views=["Scanning"]
im.Create_Views(views)
while True:
    key = cv2.waitKey(1) & 0xFF
    edge,plain=get_edge(camera.read())
    im.Update_Views(views,[edge])
    if key==ord('y'):
        time.sleep(.03)
        # No need to read just resizes and combines the edge image and the plain image
        cv2.imshow("Press y if this is your key", np.concatenate((imutils.resize(cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR),width=300),imutils.resize(plain,width=300)),axis=1))
        if chr(cv2.waitKey(0)) =="y":
            test_terra(top_edge(edge))
            print("Model Complete")
            break
        else:
            cv2.destroyAllWindows()
        #im.Log_Image("Logs/Test",edge)
    if key==ord('r'):
        break
camera.stop()
cv2.destroyAllWindows()