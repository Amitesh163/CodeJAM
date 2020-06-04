import cv2
import os

def im_thresh (image, path, i):
	img = cv2.imread(image)
	img_resize = cv2.resize(img, (300,400), interpolation = cv2.INTER_AREA)
	blur = cv2.medianBlur(img_resize, 25)
	gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
	_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
	cv2.imwrite(os.path.join(path, 'img_'+str(i)+'.jpg'), thresh)

for i in range(166):
	im_thresh('x_robot_nums/x_num_'+str(i)+'.jpg', 'num_processed', i)
for i in range(146):
	im_thresh('y_robot_nums/y_num_'+str(i)+'.jpg', 'num_processed', i+165)
