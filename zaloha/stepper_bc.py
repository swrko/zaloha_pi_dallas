from time import sleep
import RPi.GPIO as GPIO

DIR1 = 18 # Direction GPIO
STEP1 = 4 # Step GPIO pin

DIR2 = 27 # Direction GPIO
STEP2 = 17 # Step GPIO pin

DIR3 = 23 # Direction GPIO
STEP3 = 22 # Step GPIO pin

DIR4 = 24 # Direction GPIO
STEP4 = 25  # Step GPIO pin


SPR = 410 # Steps per Revolution
CW = 1 # ClockWise rot
CCW = 0 # CounterClockWise rot

# initial setup 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

'''MODE = (4, 17, 18) # stepping mode
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'full':(0, 0, 1)}

GPIO.output(MODE, RESOLUTION['full'])
'''

# setup GPIO
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)

GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)

GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(STEP4, GPIO.OUT)


GPIO.output(DIR1, CW) # nastavenie smeru ClockWise


step_count = SPR
delay = .005

sleep(2)

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP1, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP1, GPIO.LOW)
	sleep(delay)

# setup pre opacny smer 
sleep(.5)
GPIO.output(DIR1, CCW) # nastavenie smeru CounterClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP1, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP1, GPIO.LOW)
	sleep(delay)

sleep(.5)
GPIO.output(DIR2, CW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP2, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP2, GPIO.LOW)
	sleep(delay)

# setup pre opacny smer 
sleep(.5)
GPIO.output(DIR2, CCW) # nastavenie smeru CounterClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP2, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP2, GPIO.LOW)
	sleep(delay)

sleep(.5)
GPIO.output(DIR3, CW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP3, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP3, GPIO.LOW)
	sleep(delay)

# setup pre opacny smer 
sleep(.5)
GPIO.output(DIR3, CCW) # nastavenie smeru CounterClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP3, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP3, GPIO.LOW)
	sleep(delay)

sleep(.5)
GPIO.output(DIR4, CW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP4, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP4, GPIO.LOW)
	sleep(delay)

# setup pre opacny smer 
sleep(.5)
GPIO.output(DIR4, CCW) # nastavenie smeru CounterClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP4, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP4, GPIO.LOW)
	sleep(delay)

