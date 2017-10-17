a=1
b=1
c=0
print (a)
print(b)
for i in range(1000):
	c=a+b
	a=b
	b=c
	print(c)

