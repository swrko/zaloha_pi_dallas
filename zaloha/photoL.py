from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep
import functions as FC #FunCtions
import photoshoot2 as FS #FaceString


fnc = FC.functions()
fsc = FS.Dealwithit()

fnc.fromUtoF()
fnc.vertin()
fnc.horizout()
fnc.fromFtoL()
fnc.servclear()