from stl_tools import numpy2stl
import cv2
import matplotlib.pyplot as plt
import numpy
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
            O=next(filter(lambda x: A[x][i]==255,range(len(A))))
            y.append(O)
            pix+=1
        except:
            if pix>0:
                break
            y.append(0)
    return (y)
def get_mod(A):
    numpy2stl(A[:int(len(A)/2)], "test1.stl", scale=.1, mask_val= .05, solid=True)