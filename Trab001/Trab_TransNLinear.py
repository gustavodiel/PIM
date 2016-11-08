from PIL import Image
import numpy

#########
##
##

tamanho = 10.0
ondas = 9.0
freq = 1.0

##
##
########

im = Image.open('lena_B.png')

m = numpy.asarray(im)
m2 = numpy.zeros((im.size[0],im.size[1],3))
width = im.size[0]
height = im.size[1]

A = m.shape[0] / tamanho
w = ondas / m.shape[1]

shift = lambda x: A * numpy.sin(freq*numpy.pi*x * w)

for i in range(m.shape[0]):
    m2[:,i] = numpy.roll(m[:,i], int(shift(i)))

im2 = Image.fromarray(numpy.uint8(m2))
im2.save('TransNaoLinearDistorcao.png')

####################################################################################
####################################################################################
####################################################################################

out = Image.new('L', (l,h))
def root(x, i, j):
    x = (256.0/np.sqrt(1+x))
    return int(x), i, j


for i in range(0,l):
   for j in range(0,h):
       pix, px, py = root(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)


out.save('TransNLinearRootInv.png')

####################################################################################
####################################################################################
####################################################################################
out = Image.new('L', (l,h))
def roota(x, i, j):
    x = (np.sqrt(1+x))
    return int(x), i, j


for i in range(0,l):
   for j in range(0,h):
       pix, px, py = roota(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)


out.save('TransNLinearRoot.png')

####################################################################################
####################################################################################
####################################################################################
out = Image.new('L', (l,h))
def loot(x, i, j):
    x = (10*np.log(x**2 + 1))
    return int(x), i, j


for i in range(0,l):
   for j in range(0,h):
       pix, px, py = loot(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)


out.save('TransNLinearLog.png')

####################################################################################
####################################################################################
####################################################################################
out = Image.new('L', (l,h))
def eoot(x, i, j):
    x = np.exp(np.multiply(0.021746,x))
    return int(x), i, j


for i in range(0,l):
   for j in range(0,h):
       pix, px, py = eoot(img.getpixel((i,j))[0], i, j)
       out.putpixel((px,py),pix)


out.save('TransNLinearExp.png')

####################################################################################
####################################################################################
####################################################################################
