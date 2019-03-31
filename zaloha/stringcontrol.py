
file = open("CubeMatrixString.txt", "r")
somestring = file.read()
print(somestring)

if "None" not in somestring: 
    print("String fromat OK")
else:
	print("String format contains None")
	
file.close()