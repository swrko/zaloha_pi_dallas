from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep
import functions as FC #FunCtions
import photoshoot2 as FS #FaceString


fnc = FC.functions()
fsc = FS.Dealwithit()

fnc.fromLtoF()
fnc.fromFtoD() #pootocenie hore pre uchyt 
fnc.horizin()
fnc.vertout()
fnc.servclear()