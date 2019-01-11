from stl import mesh
import numpy as np
from matplotlib import pyplot
from mpl_toolkits import mplot3d

def MakeKey(key_type, ridges, ridge_min = 10, ridge_max = 7, ridge_length = 35):
    if type(ridges) not in [list,np.ndarray]:
        if len(ridges.shape) != 1:
            ridges = ExtractTopRidge(ridges,ridge_max)
    scaled_ridges = [ridges[i] * (ridge_max-ridge_min) + ridge_min for i in range(len(ridges))]
    ridges = GenerateRidgeTerrian(scaled_ridges, ridge_min = ridge_min, ridge_max = ridge_max, ridge_length = ridge_length)
    Key = AddKeyTemplate(ridges, ridge_length = ridge_length, key_type=key_type)
    return Key

def ExtractTopRidge(key_edge_img, ridge_max = 10):
    y = []
    a = len(key_edge_img)
    # Range of all Possible Rows
    for i in range(len(key_edge_img[0])):
        try: 
            #Search column at all row indexes until a value is found
            O = next(filter(lambda x: key_edge_img[x][i]>0,range(len(key_edge_img))))
            #Add to list of edges
            y.append(a-O)
        except: # next() fails if no white pixels are found in the column
            y.append(y[-1]) # No Value was found so repeat the last value seen 

    zero = 1 / max(y)
    y=[((i * zero) * ridge_max) for i in y]
    return y

def GenerateRidgeTerrian(y, ridge_min = 7, ridge_max = 10, ridge_length = 35):
    zero = ridge_min
    index = 0
    step = ridge_length/len(y)
    if step > 1:
        step = 1

    data = np.zeros(len(y) * 6, dtype=mesh.Mesh.dtype)
    y += [zero] # TODO: Remove List Function Call
    x = 1
    for i in range(0,len(data['vectors']),6): 
        # The Roof
        data['vectors'][i] = np.array([[index, y[x-1],1],
                                    [index, y[x-1], 0],
                                    [index + step, y[x], 0]])
        data['vectors'][i+1] = np.array([[index + step, y[x], 1],
                                    [index + step, y[x], 0],
                                    [index, y[x-1],1]])
        #The Walls
        data['vectors'][i+2] = np.array([[index, y[x-1], 1],
                                    [index, zero, 1],
                                    [index + step, zero,1]])
        data['vectors'][i+3] = np.array([[index, y[x-1], 1],
                                    [index + step, y[x], 1],
                                    [index + step, zero,1]])
        data['vectors'][i+4] = np.array([[index, y[x-1], 0],
                                    [index, zero, 0],
                                    [index + step, zero,0]])
        data['vectors'][i+5] = np.array([[index, y[x-1], 0],
                                    [index + step, y[x], 0],
                                    [index + step, zero,0]])
        x += 1
        index += step
    return mesh.Mesh(data)

def AddKeyTemplate(ridges,ridge_length = 35, key_type = 'L'):
    #Read in Keyway File 
    temp = mesh.Mesh.from_file('KeyWays/{0}_Way.stl'.format(key_type))
    #Read in handle file 
    handle = mesh.Mesh.from_file(filename = 'KeyWays/Handle.stl') 

    #Filter through KeyWay template and set length equal to the length of the keytype
    for i in range(len(temp.vectors)):
        for j in range(3): 
            if temp.vectors[i][j][0] == 1:
                temp.vectors[i][j][0] = ridge_length 
    # Return Combined Meshes
    return mesh.Mesh(np.concatenate([handle.data,
    temp.data,ridges.data]))

def plot_stl(img):
    # Create a new plot
    figure = pyplot.figure()
    axes = mplot3d.Axes3D(figure)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(img.vectors))
    # Auto scale to the mesh size
    scale = img.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)
    pyplot.show()

if __name__ == "__main__":
    import math

    sine_wave = [abs(math.sin(i)) for i in np.arange(0,50,.1)]
    # Render the cube faces
    key = MakeKey('L', sine_wave, 5, 8.521902, 35)
    plot_stl(key)
    key.save('Keys/Sine_Key.stl')

