#imports
from PIL import Image
import matplotlib.pyplot as plt
#get file
import sys

#buat viewer gambar
def tampil(gambar):
   plt.figure()
   plt.imshow(gambar)
   plt.show()

print("test")
droppedFile = sys.argv[1]
print(droppedFile)
gambar = Image.open(droppedFile)
#get height
gambar_width, gambar_height = gambar.size
print("Ukuran: ",gambar_width,"*",gambar_height)
# tampil(gambar)
#resize width to height
if(gambar_width>gambar_height):
   gambar_width, gambar_height= gambar_height,gambar_height
else:
   gambar_width, gambar_height= gambar_width,gambar_width

print("Ukuran baru: ",gambar_width,"*",gambar_height)
gambar1=gambar.resize((gambar_width, gambar_height))
# tampil(gambar1)
#rotate 180

#convert to polar

#export image