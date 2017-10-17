from random import randint
def randlist(r):
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	s=alpha[r]
	return (s)

def main():
	count = 0
	checklist = [0]*26
	while True:
		r=randint(0,25)
		print(checklist)
		checklist[r] = 1
		c=randlist(r)
		print(c,end="")
		if (count == 26):
			break
		count +=1
	print()
	zcount=0
	for i in range(26):
		if(checklist[i]==0):
			zcount+=1
	print(zcount)
if(__name__=='__main__'):
	main()
