import stream as see
import os 
import findkey
import cv2
import imutils
import modelling as make
from stl import mesh
from argparse import ArgumentParser

parser = ArgumentParser()
argu=["keytype","demo"]
for i in argu:
    parser.add_argument("-"+i[0],"--"+i, type=str,help="N/A")
args = parser.parse_args()
keyway=(args.keytype.upper() if args.keytype != None else "L")
demo=(False if args.demo != None else True)
# Load the STL files and add the vectors to the plot
if demo==True:
    cam=see.ConnectCam()
    views=["Image 1"]
    see.Create_Views(views)
    while True: 
        img = imutils.resize(cam.read(),height = 400)
        img = cv2.flip(img,1)
        edge = findkey.ExtractKeyEdges(img)
        key = see.Update_Views(views,[edge])
        if key==ord("y"):
            print("Proccessing")
            break
else:
    pass
key = make.MakeKey('L', edge, 5, 8.521902, 35)
make.plot_stl(key)
demo=False
if demo==False:
    key.save('Keys/Key_{0}.stl'.format(len(os.listdir("Keys"))+1))
    cv2.destroyAllWindows()