#!/usr/bin/env python

# this script will find all the iages in a folder called 'images' 
# and play them on an OLED

# place this file and the folder on the desktop
# 

import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from os import walk
from PIL import Image

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

f = []
for (dirpath, dirnames, filenames) in walk('images'):
    f.extend(filenames)
    break
print(f)
f.sort()
print(f)
y=0
list=[]


for x in range(len(f)):
    item=Image.open('images/'+f[x]).resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    list.append(item)

while True:    
    # Display image.
    image = list[y]

    disp.image(image)
    disp.display()
    y+=1
    if y > len(list)-1:
        y=0
    # Pause briefly before drawing next frame.
    print(y)
    time.sleep(0.1)
