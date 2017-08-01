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

