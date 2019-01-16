from time import sleep
import RPi.GPIO as GPIO

DIR = 20 # Direction GPIO
STEP = 21 # Step GPIO pin
SPR = 200 # Steps per Revolution
CW = 1 # ClockWise rot
CCW = 0 # CounterClockWise rot

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)


step_count = SPR
delay = .005

sleep(2)

for x in range(step_count):
	GPIO.output(STEP, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	sleep(delay)
sleep(.5)
GPIO.output(DIR, CCW)

for x in range(step_count):
	GPIO.output(STEP, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	sleep(delay)
