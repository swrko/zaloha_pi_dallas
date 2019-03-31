from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep
import functions as FC #FunCtions
import photoshoot2 as FS #FaceString


fnc = FC.functions()
fsc = FS.Dealwithit()

fnc.fromFtoR() # z R do B je to rovnaky pohyn ako F to R
fnc.fromFtoD()#pootocenie hore pre uchyt
fnc.horizin()
fnc.vertout()
fnc.servclear()