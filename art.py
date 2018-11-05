import numpy as np 
import cv2 as cv2
from scipy import misc
import pdb

sz = 480

img = np.zeros((sz,sz))
pad_sz = int(sz*(1.42 - 1)/2)

img_pad = np.pad(img,(pad_sz,pad_sz),'constant',constant_values=(0,0))


step = 0
num_wt_mats = sz*180
wt_matrix = np.zeros((sz,sz,num_wt_mats))

for r in range(sz):
	for theta in range(180):
		print(r)
		
		img = np.zeros((sz,sz))
		pad_sz = int(sz*(1.42 - 1)/2) #pad the image with root(2) - 1 
		img_pad = np.pad(img,(pad_sz,pad_sz),'constant',constant_values=(0,0))

		rotated = misc.imrotate(img_pad, -theta).astype('float64')
		rotated[:,pad_sz + r] = rotated[:,pad_sz + r] + 1

		wt = misc.imrotate(rotated, theta).astype('float64')
		wt = wt/np.max(wt)
		# wt[wt>0.5] = 1
		wt_resized = wt[pad_sz:pad_sz+sz,pad_sz:pad_sz+sz]

		wt_matrix[:,:,step] = wt_resized
		step = step + 1

img = cv2.imread("/Users/sachin007/Desktop/phantom.png", 0)
img = cv2.resize(img, dsize=(480, 480), interpolation=cv2.INTER_CUBIC)

sinogram = np.zeros((sz,180))

step = 0
r=0
theta = 0
for r in range(sz):
	for theta in range(180):
		print(r)
		# pdb.set_trace()
		sinogram[r,theta] = (np.multiply(img,wt_matrix[:,:,step])).sum()
		step = step + 1

cv2.imshow('sinogram',sinogram, cmap = 'gray')


