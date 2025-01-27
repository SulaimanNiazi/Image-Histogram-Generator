import cv2
import pylab
from skimage import img_as_ubyte
import numpy as np
import os

def plot_image(imag, title=''):
    pylab.title(title, size=20), pylab.imshow(imag)
    pylab.axis('off') # comment this line if you want axis ticks

def plot_hist(r, title=''):
    r = img_as_ubyte(r)
    pylab.hist(np.array(r).ravel(), bins=256, range=(0, 256), color='r', alpha=0.5) 
    pylab.xlabel('pixel value', size=20), pylab.ylabel('frequency', size=20)
    pylab.title(title, size=20)

def main():
    path=input("Enter path to an image: ")
    im = cv2.imread(path)
    gray = im #cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    pylab.style.use('ggplot') 
    pylab.figure(figsize=(15, 5))
    pylab.subplot(121), plot_image(gray, 'original image')
    pylab.subplot(122), plot_hist(gray, 'histogram for RGB channels')
    pylab.show() 

if __name__=="__main__":
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
    main()