import cv2
def get_edge(img,mode="cropped"):
    A=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    A=cv2.threshold(A, 50, 255, cv2.THRESH_BINARY)[1]
    im2,contours,hierarchy =cv2.findContours(A, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        #find the biggest area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        #
        if mode=="cropped":
            return [i[y: y + h, x: x + w] for i in [A,img]]
        cv2.drawContours(img, contours, -1, 255, 3)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return [A,img]
if __name__=="__main__":
    img=cv2.imread("Logs/Test2017_11_26-20:09:10.png",0)
    ima=get_edge(img,img)
    # show the images
    cv2.imshow("",ima)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
