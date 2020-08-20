#imports
from PIL import Image
import matplotlib.pyplot as plt
import sys
import math


#buat viewer gambar
def tampil(gambar):
   plt.figure()
   plt.imshow(gambar)
   plt.show()

#get file
droppedFile = sys.argv[1]
print(droppedFile)
gambar = Image.open(droppedFile)
#get height
gambar_width, gambar_height = gambar.size
print("Ukuran: ",gambar_width,"*",gambar_height)

#resize width to height
if(gambar_width>gambar_height):
   gambar_width, gambar_height= gambar_height,gambar_height
else:
   gambar_width, gambar_height= gambar_width,gambar_width

print("Ukuran baru: ",gambar_width,"*",gambar_height)
gambar1=gambar.resize((gambar_width, gambar_height))


#rotate 180
gambar1 = gambar.rotate(180)
#convert to polar
#from https://github.com/paul-butcher/tinyplanet

linear_image = gambar_putar

imgX, imgY = linear_image.size
circle_image = Image.new("RGB", (imgX, imgY), (255,255,255,0))

# rectangle to polar coordinates
maxradius = imgX / 2 #math.sqrt(imgX**2 + imgY**2)/2
rscale = imgX / maxradius
tscale = imgY / (2*math.pi)

for y in range(0, imgY):
    dy = y - imgY/2

    for x in range(0, imgX):
        dx = x - imgX/2
        t = math.atan2(dy,dx)%(2*math.pi)*tscale
        r = math.sqrt(dx**2+dy**2)*rscale

        if 0<= t < imgX and 0 <= r < imgY:
            circle_image.putpixel((x, y), linear_image.getpixel((t, r)))

#export image
print("tp-"+droppedFile)
circle_image.save(("tp-"+droppedFile))
