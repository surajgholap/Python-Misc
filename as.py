from __future__ import absolute_import, print_function
import cv2
import numpy as np
from matplotlib import pyplot as plt

m = cv2.imread("/home/suraj/Downloads/as.tiff")
height, weight, color = np.shape(m)
for i in range(0, height):
    for j in range(0, weight):
        if(m[i][j][0] == 0):
            m[i][j][0] = 150


plt.subplot(231), plt.imshow(m), plt.title('ORIGINAL')
plt.show()
