import cv2
import numpy as np
import imutils
from filtering import HomomorphicFilter

def DrawEdges(img,mode = "cropped"):
    image = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    image = cv2.threshold(image, 100, 255, cv2.THRESH_BINARY)[1]
    _,contours,_ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        #find the biggest area
        c = max(contours, key = cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        if mode == "cropped":
            return img[y: y + h, x: x + w]
    cv2.drawContours(img, contours, -1, (0,0,255), 8)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    return img

def ExtractKeyEdges(color_img):
    # RGB to Gray scale conversion
    img_gray = cv2.cvtColor(color_img,cv2.COLOR_RGB2GRAY)
    # Noise removal with iterative bilateral filter(removes noise while preserving edges)
    noise_removal = cv2.bilateralFilter(img_gray,9,75,75)
    # Thresholding the image
    _,thresh_image  =  cv2.threshold(noise_removal,220,255,cv2.THRESH_OTSU)
    th = cv2.adaptiveThreshold(thresh_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 2)
    # Applying Canny Edge detection
    canny_image = cv2.Canny(th,50,255)
    canny_image = cv2.convertScaleAbs(canny_image)
    
    # dilation to strengthen the edges
    kernel = np.ones((5,5), np.uint8)
    # Creating the kernel for dilation
    dilated_image = cv2.dilate(canny_image,kernel,iterations = 1)
    dilated_image = cv2.bilateralFilter(dilated_image,22,75,75)

    for _ in range(2):
        dilated_image = cv2.erode(dilated_image,(7,7))
        dilated_image = cv2.dilate(dilated_image,(9,9))
    #dilated_image = remove_isolated_pixels(dilated_image)
    _, contours, _ = cv2.findContours(dilated_image, 1, 2)
    #dilated_image = cv2.cvtColor(dilated_image,cv2.COLOR_GRAY2BGR)
    #cv2.drawContours(dilated_image, contours, -1, (0,255,0), 2)
    image = dilated_image
    mask = np.ones(image.shape[:2], dtype = "uint8") * 255
    # loop over the contours
    for c in contours:
        # if the contour is bad, draw it on the mask
        if cv2.contourArea(c)<600:
            cv2.drawContours(mask, [c], -1, 0, -1)
    # remove the contours from the image and show the resulting images
    image = cv2.bitwise_and(image, image, mask = mask)
    # contours =  sorted(contours, key  =  cv2.contourArea, reverse  =  True)
    # corners = cv2.goodFeaturesToTrack(thresh_image,6,0.06,25)
    # corners = np.float32(corners)
    image = cv2.medianBlur(image,13)
    return image

if __name__ == "__main__":
    img = cv2.imread("Logs/test.png")
    img = imutils.resize(img,height = 600)
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img = cv2.bilateralFilter(img,22,75,75)
    #img = cv2.Canny(img,170,255,apertureSize = 7)
    #img = cv2.GaussianBlur(img,(5,5),0)
    
    #img = cv2.Laplacian(img,cv2.CV_64F)
    #img  =  cv2.Sobel(img,cv2.CV_64F,0,1,ksize = 29) 
    
    # show the images
    cv2.imshow("",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()