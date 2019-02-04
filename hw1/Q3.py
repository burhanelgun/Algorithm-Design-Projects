#Q3
def specificBinarySearch (arr, l, r): #it doesn't take a serching number parameter beacause we search arr[i]==i

	if r >= l: #(base case for recursive algorithm) if right index bigger than the left index ,enter the below block
		mid = int(l + (r - l)/2) #divide and conquer(divide by two)

		if arr[mid] == mid: # If element is in the middle
			print ("arr[%d]=" % mid,mid) #print the index and value and return true
			return True
		elif arr[mid] > mid: #if element less then the middle than it is in left half of the array
			return specificBinarySearch(arr, l, mid-1) # search in the left sub array
		else: 				#if element bigger than the middle then it is in right half of the array
			return specificBinarySearch(arr, mid + 1, r)# search in the right sub array
	else:
		return False #if it can't find then return false


def isThereAnIndex(arr): #runs the above function with initial arguments and arr
	return specificBinarySearch(arr,0,len(arr)-1)


#Driver code
arr = [ -1, 0, 1, 3, 6 ]
result = isThereAnIndex(arr)
print("Result= %r" % result)

