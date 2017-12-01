from stl_tools import numpy2stl
import cv2
import matplotlib.pyplot as plt
import numpy
import imutils
def top_edge(A):
    #A = imread("Logs/Test2.png",0)
    #A=cv2.cvtColor(A,cv2.COLOR_RGB2GRAY)
    #A = A[:, :, 2] + 1.0*A[:,:, 0] # Compose R
    #A=A[:int(len(A)/2)]
    y=[]
    pix=0
    for i in range(len(A[0])):
        found=False
        try:
            O=next(filter(lambda x: A[x][i]>0,range(int(len(A)/2))))
            y.append(O)
            pix+=1
        except:
            if pix>0:
                break

    '''
    if len(y)>35:
        print(len(y),len(A[0]))
        return top_edge(imutils.resize(A,width=int((35/len(y))*len(A[0]))))
    '''
    zero=max(y)
    y=[(zero/i) for i in y]
    print(y)
    return (y)
def get_mod(A):
    numpy2stl(A[:int(len(A)/2)], "test1.stl", scale=.1, mask_val= .05, solid=True)