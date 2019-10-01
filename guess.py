import random
num=random.randint(1,10)

while True:
	dum=int(input("ENTER GUESSED NO BETWEEN 1-10 : "))
	if num>dum:
		print("YOU ARE TOO LOW!!")
		dum=dum
	elif num<dum:
		print("YOU ARE TOO HIGH!")
		
	else:
		print("YOU WON!!")
		pa=input("Do you want to play again (y/n) ")
		if pa=="y":
			num=random.randint(1,10)
			dum=None
		else:
			print("Thanks for playing")
			break



