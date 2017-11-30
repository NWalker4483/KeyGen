# KeyGen 
The purpose of this project is to create a device that can automatically create a 3d-printable clone of a key.
## Materials 
* Pi Zero W
* Pi Camera v1.3
* MakerBot Replicator+
* CoolBase Led 
* Light Diffuser "2x Water Bottle Lids"
## Dependencies
* Raspian Jessie v?.??
* python v3.6
* numpy-stl,numpy
* open-cv2
* imutils?
* picamera
* time,datetime
## Imaging
On a <del>Black</del> Background
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
Key Blanks are manually created for the program to modify
* * #### Key Way
## Printing
* ### Settings 
* * Mini-Fill
## Current Tests
* Inclusion of a umbrella effect to reduce light flares
* Remove Gloss from paint with steel wool to reduce light flares
* Testing on a white background to reduce light flares
* Powering CoolBase Led from Pi3 and Pi Zero 
* Sharpening Image to correct for blurry images 
* Adjusting the picamera lens for [macro photography](https://www.raspberrypi.org/blog/macro-photography-with-the-camera-board/)
## Future Developments 
* Storing keys on server
* Notification Lights
* Reliability with varying key colors
* Method of KeyWay User input
* Hard code Scaling Ratio to reduce computational load
* Portable Power with a Lipo Battery 
* Using Button to initiate cloning procedure
## Shopping List
* [Adafruit Powerboost](https://www.adafruit.com/product/1944)
* [Pi Zero Camera Adapter](https://www.adafruit.com/product/3157)
## References
* [Powering Pi from Lipo](https://github.com/NeonHorizon/lipopi)
* [Installing Opencv on Pi](https://www.pyimagesearch.com/2015/10/26/how-to-install-opencv-3-on-raspbian-jessie/)