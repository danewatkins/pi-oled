 # Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Beaglebone Black pin configuration:
# RST = 'P9_12'
# Note the following are only used with SPI:
# DC = 'P9_15'
# SPI_PORT = 1
# SPI_DEVICE = 0

# 128x32 display with hardware I2C:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

# 128x32 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# 128x64 display with hardware SPI:
# disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

x=1
y=1
list1=[]
# Load image based on OLED display height.  Note that image is converted to 1 bit color.
##if disp.height == 64:
##    image = Image.open('happycat_oled_64.ppm').convert('1')
##else:
##    image = Image.open('happycat_oled_32.ppm').convert('1')

# Alternatively load a different format image, resize it, and convert to 1 bit color.
# image = Image.open('StapleHill/StapleHill0071.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

#item1=Image.open('exit-g-solo/bg.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
#disp.image(item1)
#disp.display()
font = ImageFont.load_default()
#background = Image.open('kiss/south_side.jpg').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

for x in range(1, 32):
    item=Image.open('exit-f/exit-f'+str(x).zfill(5)+'.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    list1.append(item)

while True:    
    # Display image.
    background = Image.open('kiss/south_side.jpg').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    
    image = list1[y]
    background.paste(image, (0, 0), image)
 

    draw = ImageDraw.Draw(background)
    #draw = ImageDraw.Draw(image)
    #draw.text((x, 20),    'Hello',  font=font, fill=255)
    #draw.text((x, 20+20), 'World!', font=font, fill=0) 
    disp.image(background)
    disp.display()
    y+=1
    if y > 30:
        y=1
    # Pause briefly before drawing next frame.
    print(y)
    time.sleep(0.05)
