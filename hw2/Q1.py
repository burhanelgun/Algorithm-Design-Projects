def minimumPenaltyAndPath(i,a):
    minimumPenalty=100000000  #for finding the minimum
    hotelRank = 0 #start in the first index hotel
    stoppedHotelPath=[] #for storing the stopped hotels
    if i is 0:     #base case if there is no hotel so its penalty 0 and its path empty
        return 0, []
    for j in range(0,i):  #traversing the hotels
        minPenaltyPrevious, stoppedHotelPathPrevious = minimumPenaltyAndPath(j,a) #recursive call and calculating the other othels penalties and paths
        sumPenalty =  ((200-(a[i]-a[j]))**2) + minPenaltyPrevious #summing other otels and todays otel pernalties
        if minimumPenalty > sumPenalty: #select the minimum penalty
            minimumPenalty = sumPenalty
            hotelRank = j+1
            stoppedHotelPath = stoppedHotelPathPrevious  # assign as a stopped 
    stoppedHotelPath.append(hotelRank) # append the stopped hotel rank to the path

    return minimumPenalty, stoppedHotelPath

#driver code
a = [190, 220, 410, 580, 640, 770, 950, 1100, 1350]
print(minimumPenaltyAndPath(len(a)-1,a))

