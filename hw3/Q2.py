def costOfOptimalPlan(monthCount,M,NYCosts,SFCosts):  #takes mount number, M cost, NY operating costs, SF operating costs
	optimalCostsEndsNY=[0]*monthCount  #dynamic programming table for cost of optimal plans which ends with NY
	optimalCostsEndsSF=[0]*monthCount  #dynamic programming table for cost of optimal plans which ends with SF
	for i in range(0,monthCount):
		optimalCostsEndsNY[i]=NYCosts[i]+min(optimalCostsEndsNY[i-1],M+optimalCostsEndsSF[i-1]) #when there are i month and calculate the cost of the optimal plan which end with NY, there is two option one is SF[i-1]+M second is NY[i-1], we choose the mininmum one(we use the dynamic programming table for getting this info )
		optimalCostsEndsSF[i]=SFCosts[i]+min(optimalCostsEndsSF[i-1],M+optimalCostsEndsNY[i-1]) #when there are i month and calculate the cost of the optimal plan which end with SF, there is two option one is NY[i-1]+M second is SF[i-1], we choose the mininmum one(we use the dynamic programming table for getting this info )

	return min(optimalCostsEndsNY[monthCount-1],optimalCostsEndsSF[monthCount-1]) # after the for loop there are two list,and end of the lists(exact mounthCounts size) one is store the cost of the optimal plan ended with NY the other is store the cost of the optimal plan ended with SF we choose the minimum one and return it



#driver code
monthCount=4
M=10
NYCosts=[1,3,20,30]
SFCosts=[50,20,2,4]
print (costOfOptimalPlan(monthCount,M,NYCosts,SFCosts))










