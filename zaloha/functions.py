from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep

class functions:

	def __init__(self):
		self.setGPIO()
		
	def setGPIO(self):

		# initial setup 
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		
		self.DIR1 = 18 # Direction GPIO
		self.STEP1 = 4 # Step GPIO pin

		self.DIR2 = 27 # Direction GPIO
		self.STEP2 = 17 # Step GPIO pin

		self.DIR3 = 23 # Direction GPIO
		self.STEP3 = 22 # Step GPIO pin

		self.DIR4 = 25 # Direction GPIO
		self.STEP4 = 24  # Step GPIO pin


		self.SPR = 100 # Steps per Revolution
		self.CW = 1 # ClockWise rot
		self.CCW = 0 # CounterClockWise rot

		# setup GPIO
		GPIO.setup(self.DIR1, GPIO.OUT)
		GPIO.setup(self.STEP1, GPIO.OUT)

		GPIO.setup(self.DIR2, GPIO.OUT)
		GPIO.setup(self.STEP2, GPIO.OUT)

		GPIO.setup(self.DIR3, GPIO.OUT)
		GPIO.setup(self.STEP3, GPIO.OUT)

		GPIO.setup(self.DIR4, GPIO.OUT)
		GPIO.setup(self.STEP4, GPIO.OUT)

		self.step_count = self.SPR
		self.delay = .005
		
		#initial servo setup
		self.servo = PWM.Servo()
		self.servo2 = PWM.Servo()
		self.servo3 = PWM.Servo()
		self.servo4 = PWM.Servo()
		
	def servclear(self):
		#ukoncenie servo liniek
		sleep(0.25)
		self.servo.stop_servo(6) # clean servo

		sleep(0.25)
		self.servo2.stop_servo(13) # clean servo

		sleep(0.25)
		self.servo3.stop_servo(16) # clean servo

		sleep(0.25)
		self.servo4.stop_servo(26) # clean servo
		
	def fromFtoU(self):
		
		# setup pre smer 
		GPIO.output(self.DIR2, self.CW) # nastavenie smeru ClockWise
		GPIO.output(self.DIR4, self.CCW) # nastavenie smeru ClockWise

		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP2, GPIO.HIGH)
			GPIO.output(self.STEP4, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP2, GPIO.LOW)
			GPIO.output(self.STEP4, GPIO.LOW)
			sleep(self.delay)	
		sleep(1)

	def fromUtoF(self):

		# setup pre smer 
		GPIO.output(self.DIR2, self.CCW) # nastavenie smeru CounterClockWise
		GPIO.output(self.DIR4, self.CW) # nastavenie smeru CounterClockWise
		
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP2, GPIO.HIGH)
			GPIO.output(self.STEP4, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP2, GPIO.LOW)
			GPIO.output(self.STEP4, GPIO.LOW)
			sleep(self.delay)
		sleep(1)

	def fromFtoL(self):
	
		# setup pre smer 
		GPIO.output(self.DIR1, self.CCW) # nastavenie smeru CounterClockWise
		GPIO.output(self.DIR3, self.CW) # nastavenie smeru CounterClockWise
		
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP1, GPIO.HIGH)
			GPIO.output(self.STEP3, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP1, GPIO.LOW)
			GPIO.output(self.STEP3, GPIO.LOW)
			sleep(self.delay)
		sleep(1)
		
	def fromLtoF(self):
	
		# setup pre smer 
		GPIO.output(self.DIR1, self.CW) # nastavenie smeru CounterClockWise
		GPIO.output(self.DIR3, self.CCW) # nastavenie smeru CounterClockWise
		
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP1, GPIO.HIGH)
			GPIO.output(self.STEP3, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP1, GPIO.LOW)
			GPIO.output(self.STEP3, GPIO.LOW)
			sleep(self.delay)
		sleep(1)
		
	def fromFtoR(self):
	 
		# setup pre smer 
		GPIO.output(self.DIR1, self.CW) # nastavenie smeru CounterClockWise
		GPIO.output(self.DIR3, self.CCW) # nastavenie smeru CounterClockWise
		
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP1, GPIO.HIGH)
			GPIO.output(self.STEP3, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP1, GPIO.LOW)
			GPIO.output(self.STEP3, GPIO.LOW)
			sleep(self.delay)
		sleep(1)	
	
	def fromRtoF(self):
	
		# setup pre smer 
		GPIO.output(self.DIR1, self.CCW) # nastavenie smeru CounterClockWise
		GPIO.output(self.DIR3, self.CW) # nastavenie smeru CounterClockWise
		
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP1, GPIO.HIGH)
			GPIO.output(self.STEP3, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP1, GPIO.LOW)
			GPIO.output(self.STEP3, GPIO.LOW)
			sleep(self.delay)
		sleep(1)
	
	def fromFtoB(self):

		# setup pre smer 
		GPIO.output(self.DIR1, self.CW) # nastavenie smeru CounterClockWise
		GPIO.output(self.DIR3, self.CCW) # nastavenie smeru CounterClockWise
		
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP1, GPIO.HIGH)
			GPIO.output(self.STEP3, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP1, GPIO.LOW)
			GPIO.output(self.STEP3, GPIO.LOW)
			sleep(self.delay)
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP1, GPIO.HIGH)
			GPIO.output(self.STEP3, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP1, GPIO.LOW)
			GPIO.output(self.STEP3, GPIO.LOW)
			sleep(self.delay)
		sleep(1)	
		
	def fromBtoF(self):
	
		# setup pre smer 
		GPIO.output(self.DIR1, self.CCW) # nastavenie smeru CounterClockWise
		GPIO.output(self.DIR3, self.CW) # nastavenie smeru CounterClockWise
		
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP1, GPIO.HIGH)
			GPIO.output(self.STEP3, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP1, GPIO.LOW)
			GPIO.output(self.STEP3, GPIO.LOW)
			sleep(self.delay)
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP1, GPIO.HIGH)
			GPIO.output(self.STEP3, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP1, GPIO.LOW)
			GPIO.output(self.STEP3, GPIO.LOW)
			sleep(self.delay)
		sleep(1)		
	
	def fromFtoD(self):
	
		# setup pre smer 
		GPIO.output(self.DIR2, self.CCW) # nastavenie smeru CounterClockWise
		GPIO.output(self.DIR4, self.CW) # nastavenie smeru CounterClockWise
		
		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP2, GPIO.HIGH)
			GPIO.output(self.STEP4, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP2, GPIO.LOW)
			GPIO.output(self.STEP4, GPIO.LOW)
			sleep(self.delay)
		sleep(1)
	
	def fromDtoF(self):
	
		# setup pre smer 
		GPIO.output(self.DIR2, self.CW) # nastavenie smeru ClockWise
		GPIO.output(self.DIR4, self.CCW) # nastavenie smeru ClockWise

		#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
		for x in range(self.step_count):
			GPIO.output(self.STEP2, GPIO.HIGH)
			GPIO.output(self.STEP4, GPIO.HIGH)
			sleep(self.delay)
			GPIO.output(self.STEP2, GPIO.LOW)
			GPIO.output(self.STEP4, GPIO.LOW)
			sleep(self.delay)	
		sleep(1)	
	
	def vertin(self):

		# Set servo1 on GPIO6 to 500us (1.5ms) #670
		self.servo.set_servo(6, 850) #1200
		#self.servo.set_servo(6, 500)
		sleep(0.5)
		# Set servo3 on GPIO13 to 500us (1.7ms) # 702
		self.servo.set_servo(16, 1100)
		#self.servo.set_servo(16, 500)
		sleep(0.5)
		
	def vertout(self):
		
		# Set servo1 on GPIO6 to 500us (1.5ms)
		self.servo.set_servo(6, 2350)
		sleep(0.5)
		# Set servo3 on GPIO13 to 500us (1.7ms)
		self.servo.set_servo(16, 2300)
		sleep(0.5)

	def horizin(self):
	

		# Set servo2 on GPIO12 to 500us (1.7ms) #757
		self.servo.set_servo(13, 930) #1000
		sleep(0.5)
		# Set servo4 on GPIO16 to 500us (1.7ms) #670
		self.servo.set_servo(26, 950)
		sleep(0.5)
	
	def horizout(self):
		
		# Set servo2 on GPIO12 to 500us (1.7ms)
		self.servo.set_servo(13, 2250)#2350
		sleep(0.5)
		# Set servo4 on GPIO16 to 500us (1.7ms)
		self.servo.set_servo(26, 2500)
		sleep(0.5)
	
	
