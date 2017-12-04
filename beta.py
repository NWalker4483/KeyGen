import stream as see
import os 
from findkey import get_edge
import modelling as make
from stl import mesh
from argparse import ArgumentParser
parser = ArgumentParser()
argu=["keytype","demo"]
for i in argu:
    parser.add_argument("-"+i[0],"--"+i, type=str,help="N/A")
args = parser.parse_args()
keyway=(args.keytype.upper() if args.keytype != None else "L")
demo=(True if args.demo != None else False)
Key=make.KeyWay(keyway,35,5,8.521902)     
# Load the STL files and add the vectors to the plot
if demo==False:
    cam=see.ConnectCam()
    views=["True"]
    see.Create_Views(views)
    while True: 
        edge=get_edge(cam.read())
        key=see.Update_Views(views,[edge])
        if key==ord("y"):
            print("Proccessing")
            break
else:
    import cv2
    edge=cv2.imread('Logs/BestCase.png')
    edge=cv2.cvtColor(edge,cv2.COLOR_BGR2GRAY)
key = make.Add_Temp(make.test_terra(make.top_edge(edge,Key),Key=Key),Key)
make.plot_stl(key)
demo=False
if demo==False:
    key.save('Keys/Key_{0}.stl'.format(len(os.listdir("Keys"))+1))