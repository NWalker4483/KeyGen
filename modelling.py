import cv2
import matplotlib.pyplot as plt
import numpy
import imutils
def top_edge(A):
    y=[]
    # Range of all Possible Rows
    for i in range(len(A[0])):
        try:
            #Search column at all row indexes until a value is found
            O=next(filter(lambda x: A[x][i]>0,range(int(len(A)/2))))
            #Add to list of edges
            y.append(O)
        except:
            if len(y)>0:
                break
            continue
    zero=max(y)
    y=[(zero/   i)/2 for i in y]
    print(*y,sep='\n')
    return (y)