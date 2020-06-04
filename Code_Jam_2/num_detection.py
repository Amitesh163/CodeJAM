from dataset import loadData
import numpy as np
import cv2
from PIL import Image

img_array, label = loadData()

def number_scan(image):

	img = cv2.imread(image)
	img_resize = cv2.resize(img, (1000,1000), interpolation = cv2.INTER_AREA)
	img_copy = img_resize.copy()
        img_hsv=cv2.cvtColor(img_resize, cv2.COLOR_BGR2HSV)

	# lower mask (0-10)
	lower_red = np.array([0,50,50])
	upper_red = np.array([10,255,255])
	mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

	# upper mask (170-180)
	lower_red = np.array([170,50,50])
	upper_red = np.array([180,255,255])
	mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

        # join my masks
        mask_red = mask0+mask1

	yellow_lower = np.array([25, 146, 190])
        yellow_upper = np.array([62, 174, 250])
        mask_yellow = cv2.inRange(img_hsv, yellow_lower, yellow_upper)

	mask_final = mask_yellow + mask_red

        # set my output img to zero everywhere except my mask
        output_img = img_resize.copy()
        output_img[np.where(mask_final!=0)] = 1

	gray = cv2.cvtColor(output_img, cv2.COLOR_BGR2GRAY)
	ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_TOZERO)
	edges = cv2.Canny(thresh, 100, 200)
	_, contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	max_ = 0
	biggest = 0

	for cnt in contours:
		if len(cnt) != 0:
			(x, y, w, h) = cv2.boundingRect(cnt)
			if (w+h)>max_ :
				max_=w+h
				(x1, y1, w1, h1) = (x, y, w, h)
		
	cv2.rectangle(img_resize, (x1, y1), (x1 + w1, y1 + h1), (255, 255, 255), 3)
	cropped = img_copy[y1-10:y1+h1+10, x1-10:x1+w1+10]
	cv2.imwrite('test.jpg', cropped)
	
def im_thresh (image):

	img = cv2.imread(image)
	img_resize = cv2.resize(img, (300,400), interpolation = cv2.INTER_AREA)
	blur = cv2.medianBlur(img_resize, 25)
	gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
	cv2.imwrite('test_thresh.jpg', thresh)

def im_to_array(image):

	data = 0
	image = Image.open(image)
	data = np.asarray(image)
	
	return data

def match_img_num(img_array, label, data):
	
	index = -1
	for i in range(len(img_array)):
		if np.array_equal(data,img_array[i]):
			index = i
	
	if index != -1:
		return label[index]
	else:
		return 0
		
def final_num_det():
	number_scan('test_main.jpg')
	im_thresh('test.jpg')
	data = im_to_array('test_thresh.jpg')
	result = match_img_num(img_array, label, data)
	return result

