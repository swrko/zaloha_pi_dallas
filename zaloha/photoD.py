from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep
import functions as FC #FunCtions
import photoshoot2 as FS #FaceString


fnc = FC.functions()
fsc = FS.Dealwithit()

fnc.vertin()
fnc.horizout()
fnc.fromDtoF() #pootocenie dole pre uchyt
fnc.fromBtoF()
fnc.horizin()
fnc.vertout()
fnc.fromFtoD()
fnc.servclear()