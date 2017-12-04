from stl import mesh
import numpy as np
from matplotlib import pyplot
from mpl_toolkits import mplot3d
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
    zero=max(y)+1
    y=[(zero/(i+1))/2 for i in y]
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
            temp.vectors[i][j]=list(map(lambda x: Key.length if x==1 else x,temp.vectors[i][j]))
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
        def __init__(self,type,length,ridgemin,ridgemax):
            self.type=type
            self.length=length
            self.ridgemin=ridgemin
            self.ridgemax=ridgemax
if __name__ == "__main__":
    # Create a new plot
    Key=KeyWay("L",35,5,8.521902)
    # Render the cube faces
    plot_stl(Add_Temp(test_terra([0,0,0,0,0,0,0,0],Key=Key),Key=Key))

