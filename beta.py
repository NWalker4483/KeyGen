import stream as see
import cv2
import os 
from findkey import get_edge
import modelling as make
from stl import mesh
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-k","--keytype", type=str,help="The KeyWay")
args = parser.parse_args()
keyway=(args.keytype.upper() if args.keytype != None else "L")


Key=make.KeyWay(keyway,35,5,8.521902)     
# Load the STL files and add the vectors to the plot
#edge=cv2.imread('Logs/BestCase.png')
#edge=cv2.cvtColor(edge,cv2.COLOR_BGR2GRAY)
cam=see.ConnectCam()
views=["True"]
see.Create_Views(views)
while True: 
    edge=get_edge(cam.read())
    see.Update_Views(views,edge)
    key=cv2.waitKey(1)
    if key==ord("y"):
        break
key = make.Add_Temp(make.test_terra([i*Key.ridgemax for i in make.top_edge(edge)],Key=Key),Key)
make.plot_stl(key)
key.save('Keys/Key_{0}.stl'.format(len(os.listdir("Keys"))))