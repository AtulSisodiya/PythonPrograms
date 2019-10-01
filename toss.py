from random import random

def toss():
	r=random()
	if r>0.5:
		return "HEADS"
	else:
		return "TAILS"

def toss():
	if random()>0.5:
		return "HEADS!!!"
	else:
		return "TAILS!!!!"

print(toss())
