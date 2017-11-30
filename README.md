# KeyGen 
The purpose of this project is to create a device that can automatically create a 3d-printable clone of a key.
## Materials 
* Pi Zero W
* Pi Camera v1.3
* MakerBot Replicator+
* CoolBase Led 
* Light Diffuser "2x Water Bottle Lids"
## Dependencies
* Raspian Stretch v?.??
* python v3.6
* numpy-stl,numpy
* open-cv2
* imutils?
* picamera
* time,datetime

## Imaging
On a Black Background
* ### Key Reading
The image is then converted to a Grayscale image which is then converted to a B&W mask of the key, using the open-cv threshold function. 
* ### Enclosure
The device enclosure was designed in Sketchup and replaces the need for a seperate black drop.
* * #### Circuits
??Ohm Resistor  
* * #### Lighting 
CoolBase Led 
Which is glued to two Water Bottle Caps to diffuse the light

## Modelling
The Modelling is passed a mask of the key.
* ### Edge Extraction 
Since the key orientaion is controlled 
* ### Scaling
The pixel difference between the top and bottom of the mask is compared to the expected height values

* ### Blanks
* * #### Key Way


## Printing 
* ### Material
PLA
* ### Settings 
Mini-Fill
## Developments/Tests 
* Storing keys on server
* Notification Lights
* Reliability with varying key colors
* Method of KeyWay User input
* Hard code Scaling Ratio to reduce computational load
* Portable Power with a Lipo Battery 
