import cv2
import time
import datetime
from imutils.video import VideoStream
def Create_Views(windows,pos=(0,0)):#list of window names
    for i in windows:
        #Create Windows to view images
        cv2.namedWindow(i, cv2.WINDOW_AUTOSIZE)  
        cv2.moveWindow(i,0,0)  
    #Start the window thread for the two windows we are using
    cv2.startWindowThread()
#Position the windows next to eachother
def Update_Views(names,images,trigger=(None,None)):
    for i in zip(names,images):
        cv2.imshow(i[0],i[1])#name,image
    return cv2.waitKey(1)
def ConnectCam(pi=False):
    cam=VideoStream(usePiCamera=pi).start()
    #Let Camera Warmup
    time.sleep(1)
    # initialize the video stream and allow the cammera sensor to warmup
    return cam
    
def Log_Image(name,image):
    cv2.imwrite("{0}{1}.png".format(name,datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d-%H:%M:%S')),image)
if __name__=="__main__":
    camera=ConnectCam()
    views=["Test"]
    Create_Views(views)
    while True:
        key = cv2.waitKey(1) & 0xFF
        _,img=camera.read()
        if key=='q':
            Log_Image("Test",img)
        Update_Views(views,[img])
    camera.release()
    cv2.destroyAllWindows()



#Start the window thread for the two windows we are using

