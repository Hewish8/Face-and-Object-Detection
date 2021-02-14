import cv2, time

video = cv2.VideoCapture(0)
# 0 is built-in camera 1,2 ... can be external camera 
#or put path of video file

#Use while loop to capture video. Unless check is true

a= 1

while True:
	a = a + 1

	check, frame = video.read()

	#print(check) #returns True if able to capture video
	print(frame) #returns 3D array

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	cv2.imshow('Capturing', gray)

	key = cv2.waitKey(1) #Generate new frame every 1ms

	#Window destroyed when q pressed
	if key == ord('q'):
		break

print(a) #Prints number of frame
video.release()

cv2.destroyAllWindows()