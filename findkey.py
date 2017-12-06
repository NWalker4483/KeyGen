import cv2
def get_edge(img,mode="cropped"):
    A=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #A=cv2.threshold(A, 100, 255, cv2.THRESH_BINARY)[1]
    _,contours,_ =cv2.findContours(A, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        #find the biggest area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        if mode=="cropped":
            return A[y: y + h, x: x + w]
    cv2.drawContours(A, contours, -1, (0,255,0), 8)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return A
if __name__=="__main__":
    import imutils
    img=cv2.imread("test.png")
    img=get_edge(img,"")
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img=cv2.bilateralFilter(img,22,75,75)
    #img=cv2.Canny(img,170,255,apertureSize=7)
    #img=cv2.GaussianBlur(img,(5,5),0)
    
    #img=cv2.Laplacian(img,cv2.CV_64F)
    #img = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=29) 
    ima=imutils.resize(img,height=600)
    # show the images
    cv2.imshow("",ima)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
