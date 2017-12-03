from stl import mesh
import numpy as np
def Add_Temp(ridges):
    #Read in Keyway File 
    temp=mesh.Mesh.from_file('lway.stl')
    #Store Ridge Length in mm 
    size=int((len(ridges.vectors)/6))
    #Create Empty mesh to hold extended keyway
    data = np.zeros(int(size//.2)*77, dtype=mesh.Mesh.dtype)
    '''
    # Dead Reach Protocol 
    i=0
    for a in [temp.vectors+[[j,0,0],[j,0,0],[j,0,0]] for j in np.arange(0,size,.2)]:
        for b in a: 
            data['vectors'][i]=b
            i+=1
    '''
    # Return Combined Meshes
    return mesh.Mesh(np.concatenate([
    mesh.Mesh(data).data,ridges.data   
]))
if __name__ =="__main__":
    from mpl_toolkits import mplot3d
    from matplotlib import pyplot
    from terrain import test_terra
    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    ridge = test_terra(np.random.rand(30)*10+4.985438,zero=4.985438)

    #s1=[[23.7,14.6,1],[23.7,14.6,0],[23.7,20,1]]

    key = Add_Temp(ridge)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(key.vectors))

    # Auto scale to the mesh size
    scale = key.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    pyplot.show()
    key.save('ridges.stl')