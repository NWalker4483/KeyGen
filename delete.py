from modelling import *
import numpy as np
import math
Key=KeyWay("L",35,0,10)
# Render the cube faces
key=test_terra([(abs(math.sin(i))*Key.ridgediff)+Key.ridgemin for i in np.arange(0,50,.1)],Key=Key)
#key=test_terra(top_edge(get_edge(A),Key),Key)
plot_stl(key)