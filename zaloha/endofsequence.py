from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep
import functions as FC #FunCtions
import photoshoot2 as FS #FaceString


fnc = FC.functions()
fsc = FS.Dealwithit()

fnc.fromDtoF()
fnc.vertin()
sleep(1)

fnc.horizout()
fnc.vertout()
sleep(1)

#ukoncenie servo liniek
fnc.servclear()