import random

def diceroll():
	random.seed()
	global d1,d2,sum
	d1 = random.randint(1,6)
	d2 = random.randint(1,6)
	sum = (d1+d2)
	# Read in amt of money
	global cash, bet
	cash = 1000
	print( 'You have ', cash, 'dollars!')
	bet = input("How much to bet: $")
	bet = int(bet)
	
if __name__ == '__main__':

#roll the dice
	diceroll()
#display diceroll
	print ('dice d1 = ',d1,'dice d2 = ',d2,'sum is ',sum)
#first make a bet on the front line (pass or dont pass)

#if roll is 7 or 11 you win!
	if (sum==7 or sum==11):
		cash=cash+bet
		print('You WIN and now have ', cash, ' dollars.')
#if roll is 2,3, or 12 you lose!
	elif (sum==2 or sum==3 or sum==12):
		cash=cash-bet
		print( 'You LOSE and now have ', cash, ' dollars.')
#any other roll becomes the point
	else:
		print('Your POINT is ', sum, ' You must now roll ', sum, ' before you roll a 7')
		print('in order to add to your $', cash,' cash')
		
#Now point must be rolled before a 7 for pass line to win
#if 7 is rolled before point ... pass line loses
