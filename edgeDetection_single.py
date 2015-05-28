#!/usr/bin/python

from scipy import misc
from scipy import ndimage
from array import array
import numpy as np
import math
import matplotlib.pyplot as plt
import time

def convolution(matrix, x, y):
	x_mask = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
	y_mask = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
	ret_x = 0
	ret_y = 0
	lx, ly = matrix.shape

	for i in range(-1, 2):
		for j in range(-1, 2):
			x_index = (x + i if x + i < lx else (x + i) % lx)
			y_index = (y + j if y + j < ly else (y + j) % ly)
			ret_x += matrix[x_index, y_index] * x_mask[i + 1, j + 1]
			ret_y += matrix[x_index, y_index] * y_mask[i + 1, j + 1]
	
	return math.sqrt(ret_x**2 + ret_y**2)

# Creating a numpy array from an image file
image = misc.imread('lena.png')

# Do edge detection
start_time = time.time()
lx, ly = image.shape
output = np.zeros((lx, ly))

for i in range(lx):
	for j in range(ly):
		output[i, j] = convolution(image, i, j)
elapsed_time = time.time() - start_time
print "elapsed_time:" + str(elapsed_time)
# Display picture
plt.imshow(output)
plt.show()
#plt.imshow(image, cmap=plt.cm.gray)

plt.imshow(image, cmap=plt.cm.gray, vmin=30, vmax=200)
plt.show()

# Store the result in another picture file
misc.imsave('output.png', output)
