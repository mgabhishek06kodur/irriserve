from __future__ import print_function
from __future__ import division
import cv2 as cv
import numpy as np
import argparse,os

## [Load three images with different environment settings]

#Just change the srcb file for testing
srcb="BandaTest.jpg" #KoduvaiTest/PampletTest/FishTest/BandaTest
src_t1="Fishes/Koduvai.jpg"
src_t2="Fishes/Pamplet.jpg"
print("Test File :",srcb)

#print("Test File :",srcb,"Act1 :",src_t1,"Act2 :",src_t2)
src_base = cv.imread(srcb)
src_test1  = cv.imread(src_t1)
src_test2  = cv.imread(src_t2)

## [Load three images with different environment settings]

## [Convert to HSV]
hsv_base = cv.cvtColor(src_base, cv.COLOR_BGR2HSV)
hsv_test1 = cv.cvtColor(src_test1, cv.COLOR_BGR2HSV)
hsv_test2 = cv.cvtColor(src_test2, cv.COLOR_BGR2HSV)
## [Convert to HSV]

## [Using 50 bins for hue and 60 for saturation]
h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]

# hue varies from 0 to 179, saturation from 0 to 255
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges # concat lists

# Use the 0-th and 1-st channels
channels = [0, 1]
## [Using 50 bins for hue and 60 for saturation]

## [Calculate the histograms for the HSV images]

hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

hist_test1 = cv.calcHist([hsv_test1], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test1, hist_test1, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

hist_test2 = cv.calcHist([hsv_test2], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test2, hist_test2, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)

## [Calculate the histograms for the HSV images]


## [Apply the histogram comparison methods]
compare_method=0
base_base = cv.compareHist(hist_base, hist_base, compare_method)
base_test1 = cv.compareHist(hist_base, hist_test1, compare_method)
base_test2 = cv.compareHist(hist_base, hist_test2, compare_method)
print('Method:', compare_method, 'Perfect,  Base-Test1,  Base-Test2:',base_base, '/',  base_test1, '/',  base_test2)
print("----------------------------------------------")
if base_test1<0 or base_test2<0:
	print("Other Fish")
elif base_test1>base_test2:
	print("Koduvai Fish")
elif base_test2>base_test1:
	print("Pamplet Fish")
else:
	print("Other")

print("----------------------------------------------")
## [Apply the histogram comparison methods]
