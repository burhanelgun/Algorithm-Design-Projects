def orderedJobList(jobProcessingTimeList,jobWeightList): #takes ti and wi list and return the ordered job number list
	jobOrderList = [0] * len(jobProcessingTimeList) 	 #creating and initializing the ordered job list which is for storing the ordered job number
	wDividetListTuple = [0] * len(jobProcessingTimeList) #creating and initializing the wDividetListTuple which is for storing the wi/ti result and job number as a tuple

	for i in range(0,len(jobProcessingTimeList)):		# calculating w(i)/t(i) result for all job(i) and store it in the wDividetListTuple with index value(job number)(i)
		wDividetListTuple[i]=(jobWeightList[i]/jobProcessingTimeList[i]),i

    #insertion sort
	for i in range(1, len(wDividetListTuple)):    #sort the non-increasingly the wDividetListTuple by comparing the w(i)/t(i) values
		key,temp = wDividetListTuple[i] 
		j = i-1
		while j >=0 and key > wDividetListTuple[j][0]: #
			wDividetListTuple[j+1] = wDividetListTuple[j] 
			j -= 1
		wDividetListTuple[j+1] = key,temp


	for i in range(len(wDividetListTuple)):   #getting the job number(i)(index) from the tuples and store it in the jobOrderList
		jobOrderList[i]=wDividetListTuple[i][1]

	return jobOrderList





#driver code
jobProcessingTimeList = [8,10,4,6,2,12,8] 
jobWeightList = [24,40,8,30,16,24,8]

jobOrderList=orderedJobList(jobProcessingTimeList,jobWeightList)
print (jobOrderList)