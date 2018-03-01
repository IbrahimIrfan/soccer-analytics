# take pics for training based on current mouse location
import autopy
import time
import os

imgLocation = "~/Desktop/training/ref/"
cropLocation = "training/ref/"
w = 1440
h = 900 

def cropPic(x, y, id):
    left = x - 30
    top = y - 30
    c1 = "convert -crop 60x60+" + str(left) + "+" + str(top) + " " + cropLocation + str(id) + ".jpg " + cropLocation + str(id) + "-crop.jpg"
    os.system(c1)
    os.system("rm -rf " + cropLocation + str(id) + ".jpg")

def takePic(id):
    os.system("screencapture -x " + imgLocation + str(id) + ".jpg")

def begin():
    id = 0
    while True:
        time.sleep(0.1)
        coords = autopy.mouse.get_pos()
        x = coords[0]
        y = coords[1]
        takePic(id)
        cropPic(x, y, id)
        id += 1

time.sleep(5)
begin()
