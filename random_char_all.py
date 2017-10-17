from random import randint


asc = []

#initialize all the ascii characters in a list called asc
def makelist():
	
	for i in range(32,127):
		asc.insert(-1,chr(i))
		
#return a character from asc and remove it from the list
def takechar(r):
	
	s = asc[r]
	del asc[r]
	return s
	
def main():
	makelist()
	
	checktotal = []
	iterat = len(asc)
	
	#take characters from asc, store them, and print them
	for i in range(iterat):
		string = takechar(randint(0,len(asc)-1))
		checktotal.insert(-1,string)
		#also format it to a nice rectangle
		print(string,end = "")
		if(len(checktotal)%20==0):
			print()
	
	check(checktotal)
	
#check if all the characters put into asc were used (its double checked)
def check(total):
	print("\n##################################################\n",len(asc) , "items left in list")
	present = []
	if len(asc)==0:
		makelist()
	for j in range(len(asc)):
		for i in range(len(asc)):
			if(asc[i] == total[j]):
				present.insert(-1,True)
	print (len(asc),"characters printed")
	if(len(present)==len(asc)):
		print("all characters present!")#probably right
	
main()
