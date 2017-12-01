import stream as im
import cv2
import time
from terrain import test_terra
from modelling import top_edge
import numpy as np

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from terrain import test_terra
import numpy as np
from readblank import Add_Temp
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure)
# Load the STL files and add the vectors to the plot
edge=cv2.imread('Logs/BestCase.png')
edge=cv2.cvtColor(edge,cv2.COLOR_BGR2GRAY)
#[[23.7,14.6,1],[23.7,14.6,0],[23.7,20,1]]
key = Add_Temp(test_terra([i*(3.536464) for i in top_edge(edge)],zero=4.985438))
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(key.vectors))

# Auto scale to the mesh size
scale = key.points.flatten(-1)
axes.auto_scale_xyz(scale, scale, scale)
# Show the plot to the screen
pyplot.show()
key.save('ridges2.stl')