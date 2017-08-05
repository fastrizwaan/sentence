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
adj=['pure','clean','serene','wet','sweet','refreshing','hot','cold','dry']


#SENTENCE: X is A
print (word(noun) + " is " + word(adj))

#SENTENCE: not only THIS but also THAT

adj1=word(adj)
adj2=word(adj)
# we want different adjctive for the second instance
while adj1 == adj2:
	adj2=word(adj)

print ("not only the " + word(noun) + " is " + adj1 + " but also " + adj2)


#SENTENCE: if THIS then THAT

noun1=word(noun)
noun2=word(noun)
# we want different noun for the second instance
while noun1 == noun2:
	noun2=word(noun)

print ("if " + noun1 + " is " + adj1 + " then the " + noun2 + " is " + adj2)

# noun is made up of adj1, adj2, adj3 and adj4 noun
# SENTENCE X is made up of A, B, C, D Y

#reset
adj3=""
adj4=""
adj2 =""
adj1 =""


while adj1 == adj2 or adj1 == adj3 or adj1 == adj4 or adj2 == adj3 or adj2 == adj4 or adj3 == adj1 or  adj3 == adj4 or adj4 == adj1:

	adj3=word(adj)
	adj4=word(adj)
	adj2 =word(adj)
	adj1 =word(adj)


print (noun1 + " is made up of " + adj1 +", "+ adj2 +", "+ adj3 +", and " + adj4 + " " + noun2)

