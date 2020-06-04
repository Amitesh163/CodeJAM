import cv2
import os
import numpy as np

def number_scan(image, path, i):
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
	cv2.imwrite(os.path.join(path, 'y_num_'+str(i)+'.jpg'), cropped)


for i in range(0,165):
	#number_scan('y_robot_images/y'+str(i)+'.jpg', 'y_robot_nums', i)
	#number_scan('x_robot_images/x'+str(i)+'.jpg', 'x_robot_nums', i)
	


