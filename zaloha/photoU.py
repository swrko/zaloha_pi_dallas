from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep
import functions as FC #FunCtions
import photoshoot2 as FS #FaceString


fnc = FC.functions()
fsc = FS.Dealwithit()

#servo vychodzia poloha
fnc.vertout()
fnc.horizout()
sleep(3)

#uchopenie kocky
fnc.vertin()
fnc.horizin()
sleep(2)

#sekvencia pre oskenovanie kocky U,L,F,R,B,D,
fnc.vertout()
fnc.fromFtoU()
fnc.servclear()
