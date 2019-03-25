from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep


servo1 = PWM.Servo()
servo2 = PWM.Servo()
servo3 = PWM.Servo()
servo4 = PWM.Servo()


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
servo1.set_servo(6, 1500)

# Set servo2 on GPIO12 to 500us (1.7ms)
servo2.set_servo(13, 1500)

# Set servo3 on GPIO13 to 500us (1.7ms)
servo3.set_servo(16, 1500)


# Set servo4 on GPIO16 to 500us (1.7ms)
servo4.set_servo(26, 1500)


sleep(5) ## cakanie na vlozenie kocky

## uchopenie kocky

# Set servo1 on GPIO6 to 500us (1.5ms) #670
servo1.set_servo(6, 670)


# Set servo2 on GPIO12 to 500us (1.7ms) #757
servo2.set_servo(13, 760)


# Set servo3 on GPIO13 to 500us (1.7ms) # 702
servo3.set_servo(16, 700)


# Set servo4 on GPIO16 to 500us (1.7ms) #670
servo4.set_servo(26, 670)


#ukoncenie servo liniek
sleep(0.25)
servo1.stop_servo(6) # clean servo

sleep(0.25)
servo2.stop_servo(13) # clean servo

sleep(0.25)
servo3.stop_servo(16) # clean servo

sleep(0.25)
servo4.stop_servo(26) # clean servo
