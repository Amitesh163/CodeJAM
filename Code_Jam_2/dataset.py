import cv2
import os
import csv
import numpy as np
from PIL import Image

images=[]
labels=[]
data=0

def getFiles(path, value):
        for file in os.listdir(path):
                if file.endswith(".jpg"):
			image = Image.open(os.path.join(path,file))
			data = np.asarray(image)
                        images.append(data)
                        labels.append(value)

def getData():
	filesPath_1 = "num_processed/ones_1"
	filesPath_2 = "num_processed/twos_2"
	
	getFiles(filesPath_1, 1)
	getFiles(filesPath_2, 2)

	file = open('datasets/img_array.csv', 'w+')
	
	with file:
		write = csv.writer(file)
		write.writerows([images])
	
	file = open('datasets/labels.csv', 'w+')
	
	with file:
		write = csv.writer(file)
		write.writerows([labels])

def loadData():
	filesPath_1 = "num_processed/ones_1"
	filesPath_2 = "num_processed/twos_2"
	getFiles(filesPath_1, 1)
	getFiles(filesPath_2, 2)

	return images, labels

def storeData(images, lables):
	
	with open('datasets/img_array.txt', 'w') as f:
    		for s in images:
        		f.write(str(s) +','+'\n')

	with open('datasets/labels.txt', 'w') as f:
    		for s in labels:
        		f.write(str(s) +'\n')

x,y = loadData()
storeData(x,y)





