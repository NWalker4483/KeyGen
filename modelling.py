from stl import mesh
import numpy as np
from matplotlib import pyplot
from mpl_toolkits import mplot3d
def top_edge(A,Key):
    y=[]
    a=len(A)
    # Range of all Possible Rows
    for i in range(len(A[0])):
        try:
            #Search column at all row indexes until a value is found
            O=next(filter(lambda x: A[x][i]>0,range(len(A))))
            #Add to list of edges
            y.append(a-O)
        except:
            y.append(y[-1])
            #You have reached the end of the key 
            #if len(y)>0:
                #break
    zero=1/max(y)
    y=[((i*zero)*Key.ridgemax) for i in y]
    #print(*y,sep='\n')
    return y
def test_terra(y,Key,index=0):
    zero=Key.ridgemin
    step=Key.length/len(y)
    if step>1:
        step=1
    # Create 3 faces of a cube
    data = np.zeros(len(y)*6, dtype=mesh.Mesh.dtype)
   #red,green,blue
   # y.append(0)
    y=list(y)+[zero]
    x=1
    for i in range(0,len(data['vectors']),6):

        data['vectors'][i] = np.array([[index, y[x-1],1],
                                    [index, y[x-1], 0],
                                    [index+step, y[x], 0]])
        data['vectors'][i+1] = np.array([[index+step, y[x], 1],
                                    [index+step, y[x], 0],
                                    [index, y[x-1],1]])
        #The Walls
        data['vectors'][i+2] = np.array([[index, y[x-1], 1],
                                    [index, zero, 1],
                                    [index+step, zero,1]])
        data['vectors'][i+3] = np.array([[index, y[x-1], 1],
                                    [index+step, y[x], 1],
                                    [index+step, zero,1]])
        data['vectors'][i+4] = np.array([[index, y[x-1], 0],
                                    [index, zero, 0],
                                    [index+step, zero,0]])
        data['vectors'][i+5] = np.array([[index, y[x-1], 0],
                                    [index+step, y[x], 0],
                                    [index+step, zero,0]])
        x+=1
        index+=step
    return mesh.Mesh(data)
def Add_Temp(ridges,Key):
    #Read in Keyway File 
    temp=mesh.Mesh.from_file('KeyWays/{0}_Way.stl'.format(Key.type))
    #Read in handle file 
    handle=mesh.Mesh.from_file('KeyWays/Handle.stl')
    #Store Ridge Length in mm 
    #Filter through KeyWay template and set length equal to the length of the keytype
    for i in range(len(temp.vectors)):
        for j in range(3): 
            if temp.vectors[i][j][0]==1:
                temp.vectors[i][j][0]=Key.length 
    # Return Combined Meshes
    return mesh.Mesh(np.concatenate([handle.data,
    temp.data,ridges.data   
]))

def plot_stl(img):
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(img.vectors))
    # Auto scale to the mesh size
    scale = img.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()
class KeyWay:
        def __init__(self,typ,length,ridgemin,ridgemax,points=None):
            self.type=typ
            self.length=length
            self.ridgemin=ridgemin
            self.ridgemax=ridgemax
            self.ridgediff=ridgemax-ridgemin
            self.keywaypoints=points
if __name__ == "__main__":
    import math
    import numpy as np
    #import cv2 
    from findkey import get_edge
    #A=cv2.imread('Highres.png')
    # Create a new plot
    Key=KeyWay("L",35,5,8.521902)
    # Render the cube faces
    key=Add_Temp(test_terra([(abs(math.sin(i))*Key.ridgediff)+Key.ridgemin for i in np.arange(0,50,.1)],Key=Key),Key=Key)
    #key=Add_Temp(test_terra((np.random.rand(200,1)*Key.ridgediff)+Key.ridgemin,Key),Key)
    #key=test_terra(top_edge(get_edge(A),Key),Key)
    plot_stl(key)
    key.save('Keys/Tan_Key.stl')

