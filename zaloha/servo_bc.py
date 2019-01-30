from RPIO import PWM

servo = PWM.Servo()

# Set servo on GPIO17 to 1200s (1.5ms)
servo.set_servo(6, 1200)

# Set servo on GPIO17 to 2000s (1.7ms)
servo.set_servo(6, 2000)

# Clear servo on GPIO17
servo.stop_servo(6)
