def isSatisfied(elementsList,constraintsList): #take elemetLists and constraint list than if this constraint is satisfied than return true else return false
	for i in range(0,len(constraintsList)):  #iterating the constraintList
		firstIndex,secondIndex,equality=getIndexesAndEquality(constraintsList[i]) #getting the constraints infos
		if (equality=='!=' and elementsList[firstIndex]==elementsList[secondIndex]) or (equality=="=" and elementsList[firstIndex]!=elementsList[secondIndex]): #if the constraint isn't satisfied then return false otherwise continue the iterate 
		   return False
	return True #if all constraints are satisfied then return true




def getIndexesAndEquality(constraint): #utility function for getting the infos from the constraints string
	if "!" not in constraint:
		firstIndex=constraint[1:].split("=")[0]
		secondIndex=constraint[1:].split("=")[1][1:]
		equality="="
		
	else:
		firstIndex=constraint[1:].split("!=")[0]
		secondIndex=constraint[1:].split("=")[1][1:]
		equality="!="

	return int(firstIndex),int(secondIndex),equality



#driver code
print(isSatisfied([5,2,5,7],[("x0=x2"),("x1!=x3")]))
print(isSatisfied([5,2,5,7],[("x0=x2"),("x1=x3")]))

