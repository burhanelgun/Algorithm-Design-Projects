#Q4
def findLargestSumCrossingWithMiddleSubSet(arr, startIndex, middleIndex, endIndex) : #find the largest sum of the contiguous subarray of array(it must contains the middle element)
	
	sumOfContiguousIndices = 0;  #find the largest sum of the contiguous subarray of left half of the array(contains middle) 
	leftHalfSum = -10000
	for i in range(middleIndex, startIndex-1, -1) : #range for middle to start it is decrease 1 by 1
		sumOfContiguousIndices = sumOfContiguousIndices + arr[i] #add the indices to sumOfContiguousIndices
		if (sumOfContiguousIndices > leftHalfSum) : #if sum of contiguos indices bigger than leftHalfSum we must update it 
			leftHalfSum = sumOfContiguousIndices #leftHalfSum updated
			startIndexOfLargestSubSet=i #startting index for largest sum subset is updated(it is in left half)
	

	sumOfContiguousIndices = 0;  #find the largest sum of the contiguous subarray of right half of the array
	rightHalfSum = -1000 
	for i in range(middleIndex + 1, endIndex + 1) : #range for middle+1 to end it is increase 1 by 1
		sumOfContiguousIndices = sumOfContiguousIndices + arr[i] #add the indices to sumOfContiguousIndices
		if (sumOfContiguousIndices > rightHalfSum) : #if sum of contiguos indices bigger than rightHalfSum we must update it 
			rightHalfSum = sumOfContiguousIndices #rightHalfSum updated
			endIndexForLargestSubset=i #startting index for largest sum subset is updated(it is in right half)
	
	

	return leftHalfSum + rightHalfSum,startIndexOfLargestSubSet,endIndexForLargestSubset; #return sum the both leftHalfSum and rightHalfSum also return the this subarray start and end points


def findLargestSumSubSet(arr, startIndex, endIndex) : 
	
	if (startIndex == endIndex) :  #base case if start and end is same index, return the start index
		return arr[startIndex],startIndex,endIndex 

	middleIndex = int((startIndex + endIndex) / 2) #divide and conquer(divide by two)

	leftHalfMaxSum,startIndexForLargestLeftHalfSubSet,endIndexForLargestLeftHalfSubset=findLargestSumSubSet(arr, startIndex, middleIndex) #solving the leftHalf array recursively
	rightHalfMaxSum,startIndexForLargestRightHalfSubSet,endIndexForLargestRightHalfSubSet=findLargestSumSubSet(arr, middleIndex+1, endIndex) #solving the rightHalf array recursively
	maxSum,startIndexForLargestSubSet,endIndexForLargestSubset=findLargestSumCrossingWithMiddleSubSet(arr, startIndex, middleIndex, endIndex) #solving the crossing with the middle index array

	#choosing the maximum subarray among the left,right or mixed sub arrays and return its sum,start and end indices
	if leftHalfMaxSum >= rightHalfMaxSum and leftHalfMaxSum >= maxSum: 
		return (leftHalfMaxSum,startIndexForLargestLeftHalfSubSet,endIndexForLargestLeftHalfSubset)
	elif rightHalfMaxSum >= leftHalfMaxSum and rightHalfMaxSum >= maxSum:
		return rightHalfMaxSum,startIndexForLargestRightHalfSubSet,endIndexForLargestRightHalfSubSet
	else:
		return maxSum,startIndexForLargestSubSet,endIndexForLargestSubset


def getLargestSumSubSet(arr): #this function call the findLargestSumSubSet function and return the largest sum contiguous subset of sum and the subarray
	maxSum,startIndexOfLargestSubSet,endIndexForLargestSubset = findLargestSumSubSet(arr, 0, len(arr) -1) 
	return arr[startIndexOfLargestSubSet:endIndexForLargestSubset+1],maxSum


#Driver code
arr = [5, -6, 6, 7, -6, 7, -4, 3]
subArr,sumOfSubArr =getLargestSumSubSet(arr)
print("Subarray is this:", subArr) 
print("Maximum contiguous sum is this: ", sumOfSubArr) 


