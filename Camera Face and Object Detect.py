import cv2, time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Calculate time object in front of camera
first_frame = None

video = cv2.VideoCapture(0)

while True:
	
	check, frame = video.read()
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#gray = cv2.GaussianBlur(gray, (21,21), 0)

	faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.05, minNeighbors = 5)


	#Store first frame
	if first_frame is None:
		first_frame = gray
		continue


	delta_frame = cv2.absdiff(first_frame, gray)

	thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
	# Threshold value is 30. If diff< 30, pixel turns black >30, turns white

	thresh_delta = cv2.dilate(thresh_delta, None, iterations = 0)

	#Adding borders
	cnts,hierarchy = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	#removing Noises and shadows
	#To detect a specific object size -Keep only that part white which has area>10000 pixels
	for contour in cnts:
		if cv2.contourArea(contour) < 5000:
			continue
		
		#Create rectangular box
		(x,y,w,h) = cv2.boundingRect(contour)
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)


	# To detect face with blue box
	for x,y,w,h in faces:
		frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),3) 



	cv2.imshow('Colourframe', frame)
	#cv2.imshow('Capturing', gray)
	#cv2.imshow('delta', delta_frame)
	#cv2.imshow('thresh', thresh_delta)

	key = cv2.waitKey(1) #Generate new frame every 1ms

	#Window destroyed when q pressed
	if key == ord('q'):
		break

video.release()

cv2.destroyAllWindows()