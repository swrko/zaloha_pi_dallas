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
fsc.getFaceColors() # vrati mi String Face U
sleep(1) #fotka U
fnc.fromUtoF()
fnc.vertin()
fnc.horizout()
fnc.fromFtoL()
#facematrix = "facematrix" + fs.getFaceColors() # vrati mi String Face L
sleep(1) #fotka L
fnc.fromLtoF()
fnc.fromFtoD() #pootocenie hore pre uchyt 
fnc.horizin()
fnc.vertout()
#facematrix = "facematrix" + fs.getFaceColors() # vrati mi String Face F
sleep(1) #fotka F
fnc.vertin()
fnc.horizout()
fnc.fromDtoF() #pootocenie dole pre uchyt
fnc.fromFtoR()
#facematrix = "facematrix" + fs.getFaceColors() # vrati mi String Face R
sleep(1) #fotka R
fnc.fromFtoR() # z R do B je to rovnaky pohyn ako F to R
fnc.fromFtoD()#pootocenie hore pre uchyt
fnc.horizin()
fnc.vertout()
#facematrix = "facematrix" + fs.getFaceColors() # vrati mi String Face B
sleep(1) #fotka B
fnc.vertin()
fnc.horizout()
fnc.fromDtoF() #pootocenie dole pre uchyt
fnc.fromBtoF()
fnc.horizin()
fnc.vertout()
fnc.fromFtoD()
#facematrix = "facematrix" + fs.getFaceColors() # vrati mi String Face D
sleep(1) #fotka D
fnc.fromDtoF()
fnc.vertin()
sleep(1)

fnc.horizout()
fnc.vertout()
sleep(1)

#ukoncenie servo liniek
fnc.servclear()
