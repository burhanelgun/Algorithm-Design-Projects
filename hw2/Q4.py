def knownPeopleNumber(people,pairs,name): #take people and people pairs and person name and return the number of people which is know this person
	counter=0
	for person1,person2 in pairs: #iterate the pairs and count the name 
		if person1==name or person2==name: #if person1 or person2 is equal the name increment the counter
			counter=counter+1
	return counter  #return the number of people


def unKnownPeopleNumber(people,pairs,name): #take people and people pairs and person name and return the number of people which is not know this person
	return len(people)-1-knownPeopleNumber(people,pairs,name) # using above function, we subtract the known people from the total people number and also we substruct the person itselfs


def removePair(name,pairs): #remove the perosn from the pairs list
	i=0
	while i<len(pairs):   # iterate the pairs list and if person1 or person2 is equal the name then remove it
		person1,person2=pairs[i]
		if person1==name or person2==name:
			del pairs[i]
		else:
			i=i+1 #if we remove it we don't increment the index otherwise we increment


def bestChoices(people,pairs): #get people and pairs and output is the best choice of party invitees.
	i=0
	while i<len(people): #traverse the people array
		if knownPeopleNumber(people,pairs,people[i])<5 or unKnownPeopleNumber(people,pairs,people[i])<5: #if we see a person which is know less than 5 people or is not know less than 5 people
			removePair(people[i],pairs)   #we remove this person both pairs and peoples becaus we can't choose him for the party. 
			del people[i]                                                                                
			i=0 	 #then we need to iterate again the people list beacuse we remove a person and a lot of pair, and it can be effect the other pairs.
		else:
			i=i+1 	 #otherwise we only  increment the index                                                                                      

	return people 	#lastly people list contains the best choice of party invitees and we return it



#driver code
people = ["A","B","C","D","E","F","G","K","L","M","N"]
pairs = [
		("A","B"),("A","C"),("A","E"),("A","F"),
		("A","G"),("A","K"),("A","L"),("A","M"),
		("A","N"),("M","D"),("M","E"),("M","K"),
		("M","L"),("M","D"),("M","E"),("M","K"),
		("M","L"),("G","F"),("G","D"),("G","C"),
		("G","B"),
		]
print(bestChoices(people,pairs))  #output is the empty list
