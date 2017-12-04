import stream as im
import cv2
import os 
import time
from modelling import test_terra
from modelling import top_edge
import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from modelling import Add_Temp
from modelling import plot_stl
from modelling import KeyWay
Key=KeyWay("L",35,5,8.521902)     
# Load the STL files and add the vectors to the plot
edge=cv2.imread('Logs/BestCase.png')
edge=cv2.cvtColor(edge,cv2.COLOR_BGR2GRAY)
#[[23.7,14.6,1],[23.7,14.6,0],[23.7,20,1]]
key = Add_Temp(test_terra([i*Key.ridgemax for i in top_edge(edge)],Key=Key),Key)
plot_stl(key)
key.save('Keys/Key_{0}.stl'.format(len(os.listdir("Keys"))))