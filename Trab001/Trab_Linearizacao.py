from PIL import Image
import numpy

#########
##
##

divisao = 100

##
##
########

img = Image.open('lena_B.png')
(l,h) = img.size
'''
# Sobel derivative filters
imx = zeros(im.shape)
filters.sobel(im,1,imx)

imy = zeros(im.shape)
filters.sobel(im,0,imy)

magnitude = sqrt(imx**2+imy**2)

print(type(imx))
im = Image.fromarray(imy + imx)
'''
out = Image.new('L', (l,h))
def linear(x, i, j):
    if x > divisao:
        return 255, i, j
    else:
        return 0, i, j

for i in range(0,l):
   for j in range(0,h):
       pix, px, py = linear(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)


out.save('Linearizacao.png')

####################################################################################
####################################################################################
####################################################################################
