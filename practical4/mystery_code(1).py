# What does this piece of code do?
# Answer: rolling the two dices ramdomly, how many rolls does it take until the two dice is the same

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0 #the times of rolling the dice, regulate the progress number to 0 in the beginning
while progress>=0: # the time of the progress is not smaller than 0
	progress+=1 # when  rolling for another time, plus the progress time
	first_n = randint(1,6) #  the number of the first dice
	second_n = randint(1,6) # the number of the second dice
	if first_n == second_n: # if they are the same
		print(progress) # print the roll count
		break #ending the program
