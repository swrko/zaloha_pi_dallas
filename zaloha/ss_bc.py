from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep


servo = PWM.Servo()

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
delay = .005

## inicializia - nastavenie do vychodiskovej polohy

# Set servo1 on GPIO6 to 500us (1.5ms)
servo.set_servo(6, 1500)
sleep(0.25)
servo.stop_servo(6) # clean servo

# Set servo2 on GPIO12 to 500us (1.7ms)
servo.set_servo(13, 1500)
sleep(0.25)

servo.stop_servo(13) # clean servo

# Set servo3 on GPIO13 to 500us (1.7ms)
servo.set_servo(16, 1500)
sleep(0.25)

servo.stop_servo(16) # clean servo

# Set servo4 on GPIO16 to 500us (1.7ms)
servo.set_servo(26, 1500)
sleep(0.25)
servo.stop_servo(26)


sleep(5) ## cakanie na vlozenie kocky

## uchopenie kocky

# Set servo1 on GPIO6 to 500us (1.5ms)
servo.set_servo(6, 100)
sleep(0.25)
servo.stop_servo(6) # clean servo

# Set servo2 on GPIO12 to 500us (1.7ms)
servo.set_servo(13, 670)
sleep(0.25)

servo.stop_servo(13) # clean servo

# Set servo3 on GPIO13 to 500us (1.7ms)
servo.set_servo(16, 670)
sleep(0.25)

servo.stop_servo(16) # clean servo

# Set servo4 on GPIO16 to 500us (1.7ms)
servo.set_servo(26, 100)
sleep(0.25)
servo.stop_servo(26)

GPIO.output(DIR1, CW) # nastavenie smeru ClockWise


print "ideme cakat na krokace"

sleep(5)

print "tocim krokovim 1 : CV"
#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP1, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP1, GPIO.LOW)
	sleep(delay)
        print x


print "tocim krokovim 1 : CCV"
GPIO.output(DIR1, CCW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP1, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP1, GPIO.LOW)
	sleep(delay)
	

print "tocim krokovim 2 : CV"
GPIO.output(DIR2, CW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP2, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP2, GPIO.LOW)
	sleep(delay)

print "tocim krokovim 2 : CCV"
GPIO.output(DIR2, CCW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP2, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP2, GPIO.LOW)
	sleep(delay)

print "tocim krokovim 3 : CV"
GPIO.output(DIR3, CW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP3, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP3, GPIO.LOW)
	sleep(delay)

print "tocim krokovim 3 : CCV"
GPIO.output(DIR3, CCW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP3, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP3, GPIO.LOW)
	sleep(delay)


print "tocim krokovim 4 : CV"
GPIO.output(DIR4, CW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP4, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP4, GPIO.LOW)
	sleep(delay)


print "tocim krokovim 4 : CCV"
GPIO.output(DIR4, CCW) # nastavenie smeru ClockWise

#vykonanie vo for cyckle pocetkrokov => output HIGH/LOW -> impulzy
for x in range(step_count):
	GPIO.output(STEP4, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP4, GPIO.LOW)
	sleep(delay)


print "serus .... koniec"
