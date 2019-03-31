import cv2
import numpy as np
import picamera
import time
from picamera.array import PiRGBArray
from picamera import PiCamera
from PIL import Image as image
import colorRoir as cr

class Capture:

	def	getFaceColors(self):
		#poznamka
		# set camera
		self.camera  = PiCamera()
		self.camera.resolution = (640,480)
		self.rawCapture = PiRGBArray(self.camera, size=(640, 480))
		time.sleep(0.2) # warm up time 
		# resize okna
		cv2.namedWindow("camera",cv2.WINDOW_NORMAL)
		cv2.resizeWindow("camera", 640,480)
		#cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
		#cv2.namedWindow("resolution", cv2.WINDOW_NORMAL)
		#cv2.resizeWindow("mask", 640,480)
		#cv2.resizeWindow("resolution", 640,480)

		# set ROI stvorcov
		self.ROI = []
		[self.x,self.y,self.width,self.height]=[160,160,80,80] # hodnota prveho ROI
		self.X = [160, 160, 160, 240, 240, 240, 320, 320, 320]
		self.Y = [160, 240, 320, 160, 240, 320, 160, 240, 320]
		#nastavenie tresholdu +-
		self.treshold = 20
		#vytvorenie oblasti ROI
		for self.index in range(9):
			
			self.ROI.append(cr.Roi(self.X[self.index], self.Y[self.index], self.height, self.width, self.index))
		
		# capture frames from the camera
		for self.frame in self.camera.capture_continuous(self.rawCapture, format ="bgr" , use_video_port = True):
			self.image = self.frame.array # ulozeny frame
			#time.sleep(0.500)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				list(map(lambda x: x.prepareImg(self.image), self.ROI))
				self.Str = ''.join(str(x) for x in (list(map(lambda x: x.getColor(), self.ROI))) )	
				cv2.imshow("camera", self.image)
			cv2.waitKey(0)
			break
			# zapis do okna -> zobrazenie framu	
			cv2.imshow("camera", self.image)
			# zahodenie framu z camery
			self.rawCapture.truncate(0)
				# prerusenie co nejde
			key = cv2.waitKey(1) & 0xFF
			if key == None:
				break
		# zavrie vsetky okna
		print("Tu sa nedostanem")
		self.camera.close()
		cv2.destroyAllWindows()
		
	def getFaceString(self):
		return self.Str

def	main():
	myCapture = Capture()
	myCapture.getFaceColors()
	print(myCapture.getFaceString())

if	__name__ == "__main__":
	main() 