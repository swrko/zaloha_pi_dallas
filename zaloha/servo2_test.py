from RPIO import PWM
from time import sleep
import functions


fnc = functions.functions()

'''
servo = PWM.Servo()
'''
	
# Set servo2 on GPIO12 to 500us (1.7ms)

'''   # Ja thas ist gut
servo.set_servo(6, 1200)
sleep(0.5)

servo.set_servo(16, 1000)
sleep(0.5)

servo.set_servo(13,1170)
sleep(0.5)

servo.set_servo(26,2500)
sleep(1.5)

servo.set_servo(26,1000)
sleep(0.5)
'''

'''
servo.set_servo(6, 900)
sleep(0.5)
servo.set_servo(16,900)
sleep(0.5)
servo.set_servo(13,900)
sleep(0.5)
servo.set_servo(26,900)
sleep(0.5)
'''

'''
servo.set_servo(6, 2500)
sleep(0.5)
servo.set_servo(16,2500)
sleep(0.5)
servo.set_servo(13,2500)
sleep(0.5)
servo.set_servo(26,2500)
sleep(0.5)
'''


fnc.vertout()
fnc.horizout()
sleep(3)
fnc.vertin()
fnc.horizin()


'''
# Set servo2 on GPIO12 to 500us (1.7ms)
servo1.set_servo(13, 2500)
sleep(1.5)

sleep(3)
# Set servo2 on GPIO12 to 1500us (1.7ms)
servo1.set_servo(13, 900)
sleep(1.5)

sleep(3)
# Clear servo on GPIO
servo1.stop_servo(13)
'''
sleep(1.5)
servo.stop_servo(6)
servo.stop_servo(16)
servo.stop_servo(13)
servo.stop_servo(26)