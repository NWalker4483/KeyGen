from stl import mesh
import math
import numpy
def test_terra(y):
    #length=35#mm
    length=len(y)
    # Create 3 faces of a cube
    data = numpy.zeros(len(y), dtype=mesh.Mesh.dtype)
    #a=int(input("How Far?"))
   #red,green,blue
    x=1
    for i in range(len(data["vectors"]),2):
        data['vectors'][i] = numpy.array([[x, 1, y[x-1]],
                                    [x, 0, y[x-1]],
                                    [x+1, 0, y[x]]])
        data['vectors'][i+1] = numpy.array([[x+1, 1, y[x]],
                                    [x+1, 0, y[x]],
                                    [x, 1, y[x-1]]])
        x+=1
    # Optionally render the rotated cube faces

if __name__ == "__main__":
    from matplotlib import pyplot
    from mpl_toolkits import mplot3d
    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    # Render the cube faces
    data=mesh.Mesh(data)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(data.vectors))

    # Auto scale to the mesh size
    scale = data.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()
    data.save('ridge.stl')
#test_terra(y)