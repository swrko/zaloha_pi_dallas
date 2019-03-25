from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep

DIR1 = 18 # Direction GPIO
STEP1 = 4 # Step GPIO pin

DIR2 = 27 # Direction GPIO
STEP2 = 17 # Step GPIO pin

DIR3 = 23 # Direction GPIO
STEP3 = 22 # Step GPIO pin

DIR4 = 25 # Direction GPIO
STEP4 = 24  # Step GPIO pin


SPR = 400 # Steps per Revolution
CW = 1 # ClockWise rot
CCW = 0 # CounterClockWise rot

# initial setup 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# setup GPIO
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)

GPIO.setup(DIR2, GPIO.OUT)
GPIO.setup(STEP2, GPIO.OUT)

GPIO.setup(DIR3, GPIO.OUT)
GPIO.setup(STEP3, GPIO.OUT)

GPIO.setup(DIR4, GPIO.OUT)
GPIO.setup(STEP4, GPIO.OUT)

step_count = SPR
GPIO.output(DIR1, CW) # nastavenie smeru ClockWise
GPIO.output(DIR3, CCW) # nastavenie smeru ClockWise
delay = .005

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP1, GPIO.HIGH)
	GPIO.output(STEP3, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP1, GPIO.LOW)
	GPIO.output(STEP3, GPIO.LOW)
	sleep(delay)

# setup pre opacny smer 
sleep(2)
GPIO.output(DIR1, CCW) # nastavenie smeru CounterClockWise
GPIO.output(DIR3, CW) # nastavenie smeru CounterClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP1, GPIO.HIGH)
	GPIO.output(STEP3, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP1, GPIO.LOW)
	GPIO.output(STEP3, GPIO.LOW)
	sleep(delay)

sleep(2)