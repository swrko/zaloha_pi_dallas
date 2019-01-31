from RPIO import PWM
from time import sleep

servo = PWM.Servo()

# Set servo1 on GPIO6 to 500us (1.5ms)
servo.set_servo(6, 500)
sleep(1.5)

# Set servo1 on GPIO6 to 1500us (1.7ms)
servo.set_servo(6, 1500)
sleep(1.5)

servo.stop_servo(6)

# Set servo2 on GPIO12 to 500us (1.7ms)
servo.set_servo(13, 500)
sleep(1.5)

# Set servo2 on GPIO12 to 1500us (1.7ms)
servo.set_servo(13, 1500)
sleep(1.5)

servo.stop_servo(13)

# Set servo3 on GPIO13 to 500us (1.7ms)
servo.set_servo(16, 500)
sleep(1.5)

# Set servo3 on GPIO13 to 1500us (1.7ms)
servo.set_servo(16, 1500)
sleep(1.5)

servo.stop_servo(16)

# Set servo4 on GPIO16 to 500us (1.7ms)
servo.set_servo(26, 500)
sleep(1.5)

# Set servo4 on GPIO16 to 1500us (1.7ms)
servo.set_servo(26, 1500)
sleep(1.5)

# Clear servo on GPIO
servo.stop_servo(26)
