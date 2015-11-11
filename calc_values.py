#!/usr/bin/env python
from skimage.measure import structural_similarity as ssim
import matplotlib.pyplot as plt
import numpy as np
import cv2
def mse(imageA, imageB):
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err
from math import *
def psnr(MSE):
	try:
		return 20*log10(255)-(10*log10(MSE))
	except ValueError:
		return "-infinity"

def compare_images(imageA, imageB, title):
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
	p=psnr(m)
	fig = plt.figure(title)
	plt.suptitle("MSE: %.10f, SSIM: %.10f,psnr: %.10s" % (m, s, p))
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
	plt.show()

print "Please enter the name of the Primary name"
ori=raw_input("")
ori=str(ori)
print "Please enter the name of the Stego Image"
new=raw_input("")
new=str(new)
original = cv2.imread(ori)
contrast = cv2.imread(new)
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
fig = plt.figure("Images")
images = ("Original", original), ("Contrast", contrast)

# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")

# show the figure
plt.show()
compare_images(original, original, "Original vs. Original")
compare_images(original, contrast, "Original vs. Contrast")
