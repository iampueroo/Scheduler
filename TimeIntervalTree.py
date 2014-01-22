from TimeIntervalNode import TimeIntervalNode

class TimeIntervalTree:
	def __init__(self, nodeArray):
		self.root = self.buildTree(nodeArray, 0, len(nodeArray)-1)

	def buildTree(self, nodeArray, left, right):
		if left > right:
			return None

		middle = (right + left) / 2
		newNode = nodeArray[middle]

		leftChild = newNode.leftChild = self.buildTree(nodeArray, left, middle-1)
		rightChild = newNode.rightChild = self.buildTree(nodeArray, middle+1, right)
		newNode.max = self.getHighestEndpoint(newNode, leftChild, rightChild)
		return newNode

	def getHighestEndpoint(self, curr, leftChild, rightChild):
		currMax = curr.max
		if leftChild is not None and leftChild.max > currMax:
			currMax = leftChild.max	
		if rightChild is not None and rightChild.max > currMax:
			currMax = rightChild.max
		return currMax
	
	def addInterval(self, interval):
		self.__addIntervalHelper(self.root, interval)

	def __addIntervalHelper(self,node,interval):
		print ("Another interation")
		if node.start == interval.begin:
			node.addInterval(interval)
			return
		elif node.start < interval.begin:
			#EAFP
			try: 
				exists = getattr(node.leftChild, 'start')
			except AttributeError:
				# Create new Node and add it to the tree
				node.leftChild = TimeIntervalNode(interval)
				return
			self.__addIntervalHelper(node.leftChild, interval)
		elif node.start > interval.begin:
			#EAFP
			try: 
				exists = getattr(node.rightChild, 'start')
			except AttributeError:
				# Create new Node and add it to the tree
				node.rightChild = TimeIntervalNode(interval)
				return
			self.__addIntervalHelper(node.rightChild, interval)
	

	def __str__(self):
		return self.toStringHelper(self.root, 0);
	
	def toStringHelper(self, node, count):
		soFar = ""
		if node.rightChild is not None:
			soFar = self.toStringHelper(node.rightChild, count+1)

		currentString = ""
		for x in range (0, count):
			currentString = currentString + "\t"
		currentString = currentString + str(node) + "\n"

		soFar = soFar + currentString

		if node.leftChild is not None:
			soFar = soFar + self.toStringHelper(node.leftChild, count+1)
		return soFar