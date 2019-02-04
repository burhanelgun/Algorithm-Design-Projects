def mergeTooArrays(lists):  #take sorted lists in a list and merge them return one sorted list
	
    if len(lists)==1:  # if there is one list in the list , we only return it 
        return lists[0]

    arr1=mergeTooArrays(lists[:len(lists)//2])   #divide by two(first half of lists) recursively solve sub problem
    arr2=mergeTooArrays(lists[len(lists)//2:])   #divide by two(second half of lists) recursively solve sub problem
    return mergeTwoArrays(arr1,arr2) #send two array to mergeTwoArrays



def mergeTwoArrays(arr1, arr2):  #take two sorted array and return one sorted merged array
    resultArr = [None] * (len(arr1)+len(arr2)) #creating an array for returning the result sorted array
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):  #traversing the both two arrays
        if arr1[i] < arr2[j]:  # if arr1 i. element is smaller than the arr2 
            resultArr[k] = arr1[i] #store this element to resultArr then increment arr1 and resultArr indices
            k = k + 1
            i = i + 1
        else: 
            resultArr[k] = arr2[j] #otherwise store arr2 j. element to resultArr
            k = k + 1  #increment resultArr and arr2 indices
            j = j + 1
      
    while i < len(arr1): #if there are more element  in the arr1,we traverse it and store rest of element to resultArr
        resultArr[k] = arr1[i]; 
        k = k + 1 #increment arr1 and resultArr indices
        i = i + 1
  
    while j < len(arr2):  #if there are more element  in the arr1,we traverse it and store rest of element to resultArr
        resultArr[k] = arr2[j]; 
        k = k + 1 #increment arr1 and resultArr indices
        j = j + 1

    return resultArr  #return the sorted result array


#driver code
lists=[[1,2,4,7],[5,9,10,12],[3,6,8,11]]
print (mergeTooArrays(lists))