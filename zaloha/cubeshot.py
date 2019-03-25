from RPIO import PWM
import RPi.GPIO as GPIO
from time import sleep
import functions

fnc = functions.functions()

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
sleep(1) #fotka U
fnc.fromUtoF()
fnc.vertin()
fnc.horizout()
fnc.fromFtoL()
sleep(1) #fotka L
fnc.fromLtoF()
fnc.fromFtoD() #pootocenie hore pre uchyt 
fnc.horizin()
fnc.vertout()
sleep(1) #fotka F
fnc.vertin()
fnc.horizout()
fnc.fromDtoF() #pootocenie dole pre uchyt
fnc.fromFtoR()
sleep(1) #fotka R
fnc.fromFtoR() # z R do B je to rovnaky pohyn ako F to R
fnc.fromFtoD()#pootocenie hore pre uchyt
fnc.horizin()
fnc.vertout()
sleep(1) #fotka B
fnc.vertin()
fnc.horizout()
fnc.fromDtoF() #pootocenie dole pre uchyt
fnc.fromBtoF()
fnc.horizin()
fnc.vertout()
fnc.fromFtoD()
sleep(1) #fotka D
fnc.fromDtoF()
fnc.vertin()

sleep(1)


#ukoncenie servo liniek
fnc.servclear()
