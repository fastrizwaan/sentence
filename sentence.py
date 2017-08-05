#!/bin/python3
#(C) GPL v3 Asif Ali Rizvan fast.rizwaan@gmail.com
# sentence generator


import random

def word(pos):
	size=len(pos)
	rword=random.randrange(0,size)
	return pos[rword]

#Part of Speech (pos)
noun=['earth','water','fire','air','land','sea','music','flower','tree','dune','snow']
adje=['pure','clean','serene','wet','sweet','refreshing','hot','cold','dry']


#SENTENCE: X is A
print (word(noun) + " is " + word(adje))

#SENTENCE: not only THIS but also THAT

adjeOne=word(adje)
adjeTwo=word(adje)
# we want different adjective for the second instance
while adjeOne == adjeTwo:
	adjeTwo=word(adje)

print ("not only the " + word(noun) + " is " + adjeOne + " but also " + adjeTwo)


#SENTENCE: if THIS then THAT

nounOne=word(noun)
nounTwo=word(noun)
# we want different noun for the second instance
while nounOne == nounTwo:
	nounTwo=word(noun)

print ("if " + nounOne + " is " + adjeOne + " then the " + nounTwo + " is " + adjeTwo)

# noun is made up of adj1, adj2, adj3 and adj4 noun
# SENTENCE X is made up of A, B, C, D Y

#reset
adjeThree=""
adjeFour=""
adjeTwo =""
adjeOne =""


while adjeOne == adjeTwo or adjeOne == adjeThree or adjeOne == adjeFour or adjeTwo == adjeThree or adjeTwo == adjeFour or adjeThree == adjeOne or  adjeThree == adjeFour or adjeFour == adjeOne:

	adjeThree=word(adje)
	adjeFour=word(adje)
	adjeTwo =word(adje)
	adjeOne =word(adje)


print (nounOne + " is made up of " + adjeOne +", "+ adjeTwo +", "+ adjeThree +", and " + adjeFour + " " + nounTwo)

