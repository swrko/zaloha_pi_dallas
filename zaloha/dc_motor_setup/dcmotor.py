# wiring tip: connect ground between rasp & power supp

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
print " mode ="+str(mode)
GPIO.cleanup()

# GPIO pin = BCM pin
# Define GPIO signals to use
# Physical pins 11,13,-,-
# GPIO17,GPIO27,-,-

StepPinForward=11
StepPinBackward=13
sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepPinForward, GPIO.OUT)
GPIO.setup(StepPinBackward, GPIO.OUT)

def forward(x):
    GPIO.output(StepPinForward, GPIO.HIGH)
    print "forwarding running  motor "
    time.sleep(x)
    GPIO.output(StepPinForward, GPIO.LOW)

def reverse(x):
    GPIO.output(StepPinBackward, GPIO.HIGH)
    print "backwarding running motor"
    time.sleep(x)
    GPIO.output(StepPinBackward, GPIO.LOW)

print "forward motor "
forward(5)
print "reverse motor"
reverse(5)

print "Stopping motor"
GPIO.cleanup()