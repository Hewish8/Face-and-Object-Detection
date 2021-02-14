import cv2, time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#Calculate time object in front of camera
first_frame = None

video = cv2.VideoCapture(0)

while True:
	
	check, frame = video.read()
	
	faces = face_cascade.detectMultiScale(frame, scaleFactor = 1.05, minNeighbors = 5)


	for x,y,w,h in faces:
		frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),3) 


	cv2.imshow('Colourframe', frame)
	

	key = cv2.waitKey(1) #Generate new frame every 1ms

	#Window destroyed when q pressed
	if key == ord('q'):
		break

video.release()

cv2.destroyAllWindows()