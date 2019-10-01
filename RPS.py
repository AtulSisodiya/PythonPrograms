print("ROCK.......")
print("PAPER.......")
print("SCISSOR.......")

p1=input("ENTER YOUR CHOICE PLAYER1: ")
print("@@@ NO CHEATING @@@ \n" *200)
p2=input("ENTER YOUR CHOICE PLAYER2: ")

if p1==p2:
	print("IT IS TIE")
elif p1=="rock":
	if p2=="paper":
		print("PLAYER 2 WIN")
	elif p2=="scissor":
		print("PLAYER 1 WIN")
elif p1=="paper":
	if p2=="rock":
		print("PLAYER 1 WIN")
	elif p2=="scissor":
		print("PLAYER 2 WIN")
elif p1=="scissor":
	if p2=="rock":
		print("PLAYER 2 WIN")
	elif p2=="paper":
		print("PLAYER 1 WIN")
else:
	print("**invalid choice**")
