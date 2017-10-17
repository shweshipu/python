#save file as ranint.py
from random import randint

def rint():
	r=randint(64,90)
	if (r==64):
		r=42
	return(r)

def main():
	for i in range(1000):
		z = rint()
		c=chr(z)
		print(z,end="")
		
main()
