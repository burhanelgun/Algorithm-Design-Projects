#Q5
def isPatternValiedHelper(givenString,currentIndexForString,givenPattern,currentIndexForPattern,patternAndWordDict,wordSet):#this function is a recursive function and it solve the problem that whether a the givenPattern match to givenString 

	if currentIndexForString==len(givenString) and currentIndexForPattern==len(givenPattern): #Base condition for recursive call
		return True																			  #If traversing all the both givenString and givenPattern is finish, it returns True

	elif currentIndexForString==len(givenString) or currentIndexForPattern==len(givenPattern): #Base condition for recursive call
		return False																		   #If traversing all givenString or givenPattern is finish, it returns false

	patternChar=givenPattern[currentIndexForPattern] #Getting next char from the pattern string

	if patternChar in patternAndWordDict: #if patternChar is already in the dict,it means this word has already match a word
		dictWord=patternAndWordDict[patternChar] #Getting the already matched word
		givenStringWord=givenString[currentIndexForString:len(dictWord)+currentIndexForString]#getting the substring of the givenString

		if givenStringWord.lower() != dictWord.lower(): #if this substring is not equal to dictWord,it will return false
			return False
		else:                                           #if this substring is equal to dictWord,it will made a recursion call return for solving the remaining characters
			return isPatternValiedHelper(givenString,currentIndexForString+len(dictWord),givenPattern,currentIndexForPattern+1,patternAndWordDict,wordSet)
	else:									#if patterChar is not already in the dict. we must try all subset of givenString		   
		for i in range(1,len(givenString)-currentIndexForString):
			if givenString[currentIndexForString:i+currentIndexForString] in wordSet: #subset of givenString must be a word 
			
				patternAndWordDict[patternChar]=givenString[currentIndexForString:i+currentIndexForString] #subset of givenString send as a value of patternChar

				if isPatternValiedHelper(givenString,currentIndexForString+i,givenPattern,currentIndexForPattern+1,patternAndWordDict,wordSet):#another recursive call for solving the new pattern and word pair
					return True																												#if it is true the matching is true			
				else:
					patternAndWordDict.pop(patternChar)  #if it is false the matching is false so we must remove the mistaken matching from the dict
		return False

def isPatternValid(givenString,givenPattern,wordSet): #main method for solving the problem it takes the string,pattern and wordSet

	if len(givenString)<len(givenPattern): #if given string is smaller then the givenPattern, return false
		return False
	else:
		patternAndWordDict={} #creating an empty dict for representing the key=patternChar : value=subString(word)
		return isPatternValiedHelper(givenString.lower(),0,givenPattern,0,patternAndWordDict,wordSet),patternAndWordDict # there are two return value first one is problem result which is True or false,second one is 
																														 #dictionary which is store the pattern char and its word (patternChar is key, word is value)
#Driver code
wordSet={"not","to","or","be"}
res,patternAndWordDict=isPatternValid("Tobeornottobe","ABCDAB",wordSet)
print(res)
print(patternAndWordDict)