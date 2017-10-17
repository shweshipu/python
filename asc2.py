def main():
	for i in range(256):
		c=chr(i)
		print("[",i,"=",c,"]",end="")
		if(i%8==0):
			print("\n",end="")
main()
