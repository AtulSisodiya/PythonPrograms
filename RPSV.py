import random
print("ROCK.......")
print("PAPER.......")
print("SCISSOR.......")

p1=input("ENTER YOUR CHOICE PLAYER1: ").lower()
ra=random.randint(1,3)
if ra==1:
	comp="rock"
elif ra==2:
	comp="paper"
else:
	comp="scissor"

print(f"Computer choose {comp}")

if p1==comp:
	print("IT IS TIE")
elif p1=="rock":
	if comp=="paper":
		print("COMPUTER WIN")
	elif comp=="scissor":
		print("YOU WIN")
elif p1=="paper":
	if comp=="rock":
		print("YOU WIN")
	elif comp=="scissor":
		print("COMPUTER WIN")
elif p1=="scissor":
	if comp=="rock":
		print("COMPUTER WIN")
	elif comp=="paper":
		print("YOU WIN")
else:
	print("**invalid choice**")
