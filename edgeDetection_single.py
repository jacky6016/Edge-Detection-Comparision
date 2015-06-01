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

if __name__ == '__main__':
	import argparse, sys
	from os.path import isfile
	from argparse import ArgumentParser
	
	# Program arguments
	parser = ArgumentParser(description="Image Edge detection")
	parser.add_argument("-i", "--input", required=True, help="input image file")
	parser.add_argument("-o", "--output", default="output.png", help="file to write output to")
	args = parser.parse_args()	
	inputFile, outputFile = args.input, args.output

	# Creating a numpy array from an image file
	inputImg = misc.imread(inputFile)
	inputArr = misc.imread(inputFile, flatten = 1) # flattens the color layers into a single gray-scale layer

	# Do edge detection(and estimate the time elapsed)
	start_time = time.time()
	lx, ly = inputArr.shape
	outputArr = np.zeros((lx, ly))

	for i in range(lx):
		for j in range(ly):
			outputArr[i, j] = convolution(inputArr, i, j)
	elapsed_time = time.time() - start_time
	print "Elapsed_time:" + str(elapsed_time)

	# Display pictures for comparison
	fig = plt.figure()
	ax1 = fig.add_subplot(121)
	ax1.imshow(inputImg, cmap=plt.cm.gray, vmin=30, vmax=200)
	ax2 = fig.add_subplot(122)
	ax2.imshow(outputArr, cmap=plt.cm.gray, vmin=30, vmax=200)
	plt.show()

	# Store the result in another picture file
	misc.imsave(outputFile, outputArr)
