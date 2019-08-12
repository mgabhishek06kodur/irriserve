import cv2
import numpy as np
from deepgaze.color_classification import HistogramColorClassifier

mu_1 = 2154.8209 #mean of the first distribution
mu_2 = 3665.4928 #mean of the second distribution
data_1 = np.random.normal(mu_1, 786.41, 1000)
data_2 = np.random.normal(mu_2, 814.150, 1000)
hist_1, _ = np.histogram(data_1, bins=100, range=[0, 2400])
hist_2, _ = np.histogram(data_2, bins=100, range=[2500,5000])
print(hist_1)
print(hist_2)
#print(data_1)
#print(data_2)

my_classifier = HistogramColorClassifier(channels=[0, 1, 2], 
                                         hist_size=[128, 128, 128], 
                                         hist_range=[0, 256, 0, 256, 0, 256], 
                                         hist_type='BGR')

def return_intersection(hist_1, hist_2):
    minima = np.minimum(hist_1, hist_2)
    intersection = np.true_divide(np.sum(minima), np.sum(hist_2))
    return intersection
    
model_1 = cv2.imread('2.jpg') #Flash Model
my_classifier.addModelHistogram(model_1)

model_2 = cv2.imread('1.jpg') #Batman Model
my_classifier.addModelHistogram(model_2)
