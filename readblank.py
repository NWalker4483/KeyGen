from stl import mesh
import numpy as np
def Add_Temp(ridges):
    temp=mesh.Mesh.from_file('lway.stl')
    size=int((len(ridges.vectors)/6))
    data = np.zeros(int(size//.2)*77, dtype=mesh.Mesh.dtype)
    #i=0
    #for a in [temp.vectors+[[j,0,0],[j,0,0],[j,0,0]] for j in np.arange(0,size,.2)]:
    #    for b in a: 
    #        data['vectors'][i]=b
    #        i+=1
    #    print(a.shape)
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
    # Load the STL files and add the vectors to the plot

    #[[23.7,14.6,1],[23.7,14.6,0],[23.7,20,1]]
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