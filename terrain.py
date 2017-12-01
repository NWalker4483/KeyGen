from stl import mesh
import math
import numpy

def test_terra(y,index=0,zero=0):
    #length=35#mm
    length=len(y)
    step=35/length
    # Create 3 faces of a cube
    data = numpy.zeros(len(y)*6, dtype=mesh.Mesh.dtype)
    #a=int(input("How Far?"))
   #red,green,blue
    y=[0]+y
    x=1
    for i in range(0,len(data['vectors']),6):
        data['vectors'][i] = numpy.array([[index, y[x-1],1],
                                    [index, y[x-1], 0],
                                    [index+step, y[x], 0]])
        data['vectors'][i+1] = numpy.array([[index+step, y[x], 1],
                                    [index+step, y[x], 0],
                                    [index, y[x-1],1]])
        data['vectors'][i+2] = numpy.array([[index, y[x-1], 1],
                                    [index, zero, 1],
                                    [index+step, zero,1]])
        data['vectors'][i+3] = numpy.array([[index, y[x-1], 1],
                                    [index+step, y[x], 1],
                                    [index+step, zero,1]])
        data['vectors'][i+4] = numpy.array([[index, y[x-1], 0],
                                    [index, zero, 0],
                                    [index+step, zero,0]])
        data['vectors'][i+5] = numpy.array([[index, y[x-1], 0],
                                    [index+step, y[x], 0],
                                    [index+step, zero,0]])
        x+=1
        index+=step
    return mesh.Mesh(data)
    # Optionally render the rotated cube faces

if __name__ == "__main__":
    from matplotlib import pyplot
    from mpl_toolkits import mplot3d
    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    # Render the cube faces
    data=test_terra(np.random.rand(10)*10+23.7)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(data.vectors))

    # Auto scale to the mesh size
    scale = data.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()
    data.save('ridge.stl')
#test_terra(y)