#!/bin/bash


#sekvencia pre oskenovanie kocky U,L,F,R,B,D,

echo "setting acces to X"
xhost +si:localuser:root

echo > CubeMatrixString.txt

echo "turning cube to face camera from U"
python3 photoU.py > Cubelog.txt
echo "taking picture of face --> press 'q' for taking picture / press 'e' for exit"
python3 photoshoot2.py
echo "chechking output string"
python3 stringcontrol.py
echo "turning cube to face camera from L"
python3 photoL.py > Cubelog.txt
echo "taking picture of face --> press 'q' for taking picture / press 'e' for exit"
python3 photoshoot2.py
echo "chechking output string"
python3 stringcontrol.py
echo "turning cube to face camera from F"
python3 photoF.py > Cubelog.txt
echo "taking picture of face --> press 'q' for taking picture / press 'e' for exit"
python3 photoshoot2.py
echo "chechking output string"
python3 stringcontrol.py
echo "turning cube to face camera from R"
python3 photoR.py > Cubelog.txt
echo "taking picture of face --> press 'q' for taking picture / press 'e' for exit"
python3 photoshoot2.py
echo "chechking output string"
python3 stringcontrol.py
echo "turning cube to face camera from B"
python3 photoB.py > Cubelog.txt
echo "taking picture of face --> press 'q' for taking picture / press 'e' for exit"
python3 photoshoot2.py
echo "chechking output string"
python3 stringcontrol.py
echo "turning cube to face camera from D"
python3 photoD.py > Cubelog.txt
echo "taking picture of face --> press 'q' for taking picture / press 'e' for exit"
python3 photoshoot2.py
echo "chechking output string"
python3 stringcontrol.py
echo "moving to initial position"
python3 endofsequence.py > Cubelog.txt

