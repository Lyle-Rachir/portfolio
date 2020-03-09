import random

while True:
	try:
		A = int(input("Select the die size "))
		min, max = 1, A
		break
	except ValueError:
		print("use numbers not letters!!!")

while True:
	try:
		C = int(input("How many times rolled? "))
		break
	except ValueError:
		print("Use Numbers not Letters!!!")
	
def rollDie(C = 1):
	B = 0
	Max_Counter = 0
	while B < C:
		X = (random.randint(1, A))
		if X == A:
			Max_Counter = Max_Counter+1
		print (X)
		B = B+1
	return Max_Counter

def Critical_Success():
	Critical_Success = (input("do you want to reroll max die? Y or N   "))
	if (Critical_Success == "Y" or "y"):
		critical_Counter = 0
		X = rollDie(C)
		while X > 0 or critical_Counter < 5:
			X = rollDie(X)
			if critical_Counter == 4:
				print("Stop beating that dead horse, it's dead Jim!")

	elif (Critical_Success == "N" or "n"):
		print("thank you for rolling me!!!")
		rollDie(C)

	else:
		print("We dont accept that here")

Critical_Success()
