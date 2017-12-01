import cv2
edge=cv2.imread('Logs/BestCase.png')
edge=cv2.cvtColor(edge,cv2.COLOR_BGR2GRAY)
#edge=cv2.threshold(edge, 50, 255, cv2.THRESH_BINARY)[1]
def top_edge(A):
    out=cv2.imread('Logs/BestCase.png')
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
            out[O][i]=[0,255,0]
            pix+=1
        except:
            if pix>0:
                break
            y.append(0)
    return (y,out)

y,out=top_edge(edge)
y=[i-8.521902 for i in y]
cv2.imshow("",out)
cv2.waitKey(0)
#8.521902mm