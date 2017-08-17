import numpy as np
import matplotlib.pyplot as plt

im1 = np.zeros([256,256])
im2 = np.zeros([256,256])
radout1 = 70
radin1 = 50
radout2 = 55
#radout2 = 40
radin2 = np.sqrt(radin1**2+radout2**2-radout1**2)
print(radin2)
center = [128,128]

for (x,y), pixel in np.ndenumerate(im1):
    pointrad = np.sqrt((x-center[0])**2+(y-center[1])**2)
    #print(pointrad)
    if(pointrad>=radin1 and pointrad<=radout1):
        im1[x,y] = 1
for (x,y), pixel in np.ndenumerate(im2):
    pointrad = np.sqrt((x-center[0])**2+(y-center[1])**2)
    #print(pointrad)
    if(pointrad>=radin2 and pointrad<=radout2):
        im2[x,y] = 1
print(im1.sum())
print(im2.sum())

plt.subplot(1, 2, 1)
imgplot = plt.imshow(np.real(im1),cmap='gray')
plt.subplot(1, 2, 2)
imgplot = plt.imshow(np.real(im2),cmap='gray')
plt.show()
