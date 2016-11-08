from PIL import Image
import numpy

#########

nrCores = 6

########

img = Image.open('lena_B.png')
(l,h) = img.size
delta = 256/nrCores
out = Image.new('L', (l,h))
def linear(x, i, j):
    coisa = delta
    if x < coisa:
        return 0, i, j
    while x > coisa:
        coisa = coisa + delta
    return coisa, i, j

for i in range(0,l):
   for j in range(0,h):
       pix, px, py = linear(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)

out.save('DiminuirBits.png')
