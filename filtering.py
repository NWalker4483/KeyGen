import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

def HomomorphicFilter(img, rh = 2.5, rl = 0.5, cutoff =32):
    img = np.float32(img)
    img = img/255

    rows,cols,dim=img.shape

    imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    y,cr,cb = cv2.split(imgYCrCb)

    y_log = np.log(y+0.01)

    y_fft = np.fft.fft2(y_log)

    y_fft_shift = np.fft.fftshift(y_fft)

    DX = cols/cutoff
    G = np.ones((rows,cols))
    for i in range(rows):
        for j in range(cols):
            G[i][j]=((rh-rl)*(1-np.exp(-((i-rows/2)**2+(j-cols/2)**2)/(2*DX**2))))+rl

    result_filter = G * y_fft_shift
    result_interm = np.real(np.fft.ifft2(np.fft.ifftshift(result_filter)))
    result = np.exp(result_interm)
    result = cv2.normalize(result, None, alpha=255, beta=0, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC3)
    return result
if __name__ == "__main__":
    img = cv2.imread('Logs/test.png')
    img = imutils.resize(img, height = 600)
    result = HomomorphicFilter(img)
    #result = result/(result.max()/255.0)
    #result = np.array(result,  dtype = np.uint8)
    print(result)
    #cv2.normalize(result, result, 0, 255, cv2.NORM_MINMAX)
    #print(np.array([i * 36.5 for i in result ]).astype(int))
    
    #result = cv2.Canny(result.astype(int),50,255)
    cv2.imshow('résultat',result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()