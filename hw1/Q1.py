#Q1
def readExcelFillTheGraph(graph): #read the excel,fill the graph,return the root node
	#read the excel
	from xlrd import open_workbook

	wb = open_workbook('Graph_data.XLS')
	values = []
	for s in wb.sheets():
	    #print 'Sheet:',s.name
	    for row in range(1, s.nrows):
	        col_names = s.row(0)
	        col_value = []
	        for name, col in zip(col_names, range(s.ncols)):
	            value  = (s.cell(row,col).value)
	            try : value = str(int(value))
	            except : pass
	            col_value.append((name.value, value))
	        values.append(col_value)

	#fill the graph
	for i in range(2,len(values)):
		if int(values[i][0][1]) in graph:
			graph[int(values[i][0][1])].append(int(values[i][1][1]))

		else:
			temp =[]
			if values[i][1][1]=='':
				graph[int(values[i][0][1])]=temp
			else:
				temp.append(int(values[i][1][1]))
				graph[int(values[i][0][1])]=temp

	for i in range(2,len(values)): #nodes which do not goes anywehere are added at the end of the dict 
		if values[i][1][1]!='':
			if (int(values[i][1][1]) not in graph):
				graph[int(values[i][1][1])]=[]


	root=int(values[0][1][0])
	return root



def BFS(graph,rootNode): 
  
		visitNodes = [] #visit nodes are represented with true and unvisited nodes are represented with false.Also,node n is in (n-1).index
		i = 0
		while i < len(graph): #len(graph) give us node count and there must be node count visitNodes
			visitNodes.append(False) #at the beginning, there aren't visited nodes, so all visitNodes indeces must be filled with False.
			i=i+1
			

        
		queue = [] #this queue used for storing the adjacents of visited nodes. 
  

		queue.append(rootNode) #starting with root node and adding it to queue 
		visitNodes[rootNode-1] = True #root node visited so update it with True
  

		while len(queue)!=0: #while queue not empty, pop the queue and find its adjacent and add them to queeu(if not visited) and make it visited


		    node = queue.pop(0) #pop the queue and we traverse unvisited adjacents of this node



		    for i in graph[node]:  #find the unvisited adjacent and append to queue and make it visited
		        if visitNodes[i-1] == False: 
		            queue.append(i)  
		            visitNodes[i-1] = True

		    if len(queue)==0:  #if queue is empty then we are in last element so ,no need to append arrow
		    	print (node, end = "")
		    else:
		    	print (node, end = "->") 



def DFS(graph,rootNode): 

		visitNodes = [] #visit nodes are represented with true and unvisited nodes are represented with false.Also,node n is in (n-1).index
		i = 0
		while i < len(graph): #len(graph) give us node count and there must be node count visitNodes
			visitNodes.append(False) #at the beginning, there aren't visited nodes, so all visitNodes indeces must be filled with False.
			i=i+1

		# Call the recursive helper function to print 
		# DFS traversal 
		DFSHelper(graph,rootNode,visitNodes)#helper method is called


def DFSHelper(graph,v,visitNodes): 

		
		visitNodes[v-1]= True #root node visited so update it with True
		
		# iterated nodes are printed
		if False in visitNodes:  #if we are not in last iteration so , need to append arrow
			print (v, end = "->")
		else:					 #if we are in last iteration so ,no need to append arrow
			print (v, end = "")

		for i in graph[v]:  #traverse the adjacent of the node v and if there is an unvisited node send this node to travering its adjacents.
			if visitNodes[i-1] == False:
				DFSHelper(graph,i,visitNodes)


#Driver code
graph = { }
rootNode = readExcelFillTheGraph(graph)
print("BFS: ",end='') 
BFS(graph,rootNode) #1->2->3->4->5->8->6->9->10->7
print('\n')
print("DFS: ",end='') 
DFS(graph,rootNode) #1->2->4->5->6->7->8->9->10->3
