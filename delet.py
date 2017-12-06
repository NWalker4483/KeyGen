import cv2
import numpy as np
def getme():
    img_file = 'test.png'
    img = cv2.imread(img_file, cv2.IMREAD_COLOR)

    imgDim = img.shape
    dimA = imgDim[0]
    dimB = imgDim[1]

    # RGB to Gray scale conversion
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    # Noise removal with iterative bilateral filter(removes noise while preserving edges)
    noise_removal = cv2.bilateralFilter(img_gray,9,75,75)
    # Thresholding the image
    ret,thresh_image = cv2.threshold(noise_removal,220,255,cv2.THRESH_OTSU)
    th = cv2.adaptiveThreshold(noise_removal, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # Applying Canny Edge detection
    canny_image = cv2.Canny(th,50,255)
    canny_image = cv2.convertScaleAbs(canny_image)
    # dilation to strengthen the edges
    kernel = np.ones((5,5), np.uint8)
    # Creating the kernel for dilation
    dilated_image = cv2.dilate(canny_image,kernel,iterations=1)
    dilated_image=cv2.bilateralFilter(dilated_image,22,75,75)

    for i in range(2):
        continue
        dilated_image=cv2.erode(dilated_image,(7,7))
        dilated_image=cv2.dilate(dilated_image,(9,9))
    #dilated_image=remove_isolated_pixels(dilated_image)
    #
    _, contours, h = cv2.findContours(dilated_image, 1, 2)
    #dilated_image=cv2.cvtColor(dilated_image,cv2.COLOR_GRAY2BGR)
    #cv2.drawContours(dilated_image, contours, -1, (0,255,0), 2)
    image=dilated_image
    mask = np.ones(image.shape[:2], dtype="uint8") * 255
    # loop over the contours
    for c in contours:
        # if the contour is bad, draw it on the mask
        if cv2.contourArea(c)<600:
            cv2.drawContours(mask, [c], -1, 0, -1)
    
    # remove the contours from the image and show the resulting images
    image = cv2.bitwise_and(image, image, mask=mask)
    #contours= sorted(contours, key = cv2.contourArea, reverse = True)


    #corners    = cv2.goodFeaturesToTrack(thresh_image,6,0.06,25)
    #corners    = np.float32(corners)
    image=cv2.medianBlur(image,13)
    #cv2.imshow("Corners",image)
    #cv2.waitKey()
    cv2.imwrite("edge.png",image)
    return image
#cv2.namedWindow("Corners", cv2.WINDOW_NORMAL)

#cv2.destroyAllWindows()