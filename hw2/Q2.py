dictionary= {"book","it","pen","board","money","best", 
                           "times","was","weather","paper","the","ceiling","of"}

def isReconstituted(s):
	if len(s)==0:     #if string is empty it can be reconstituted
		return True

	resultsOfSubproblems=[False]*(len(s)+1) #Storing the result of subproblems 

	for i in range(1,(len(s)+1)): 
		if resultsOfSubproblems[i]==False and s[0:i] in dictionary: #if str[0....i-1] isn't a valid word and it is in the dictionary
			resultsOfSubproblems[i]=True  # make it true

		if resultsOfSubproblems[i]==True:   #if str[0....i-1] is a valid word
			if i==len(s): #if all string valid then return true
				return True

			for j in range(i+1,len(s)+1): #traverse rest of the substring
				if resultsOfSubproblems[j]==False and s[i:j] in dictionary:  #if str[0....j-1] isn't a valid word and between i and j indices is in the dictionary
					resultsOfSubproblems[j]=True  #updating the subproblem result true for between s[0.......j-1]

				if j==len(s) and resultsOfSubproblems[j]==True:  # if we reached the last character and every string (0 to j indices) can be reconstituted then return true
					return True
	#if a word is not been found then return false
	return False 


#driver code
print(isReconstituted("itwasthebestoftimes"))



