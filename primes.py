  GNU nano 2.7.5                    File: count.py                              

count=1
countcheck=2
prime=False
notprime=False
while True:
	while True:
                if count%countcheck==0:
                        notprime=True
                countcheck+=1
                if countcheck==count:
                        prime=True
                        countcheck=2
                if prime | notprime:
                        print(count,"broke!")
                        break
        if prime:
                print(count,"is prime")
        count+=1
        if count>256**2: break
                               [ Read 20 lines ]
^G Get Help  ^O Write Out ^W Where Is  ^K Cut Text  ^T To Linter ^Y Prev Page
^X Exit      ^R Read File ^\ Replace   ^U Uncut Text^C Cur Pos   ^V Next Page

