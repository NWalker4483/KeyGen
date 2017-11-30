from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)

# Load the STL files and add the vectors to the plot
data = mesh.Mesh.from_file('Keys/Key_Blank_L.stl')
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(data.vectors[100:]))

# Auto scale to the mesh size
scale = data.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()