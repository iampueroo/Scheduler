import datetime

# Holds two DateTime objects to represent a time interval.
class TimeInterval:
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end
		self.owner = None

	def equals(self, other):
		return self.begin == other.begin and self.end == other.end

	def equalsWithOwner(self, other):
		return self.equals(other) and self.owner is not None and self.owner == other.owner
	
	def __str__(self):
		return str(self.begin) + " - " + str(self.end)

#Node for Tree composed of a list all TimeIntervals that start at same time
class TimeIntervalNode:
	def __init__(self, interval):
		self.list = [interval]
		self.start = interval.begin
		self.max = interval.end

	#List is ordered from highest to lowest end point
	def addInterval(self, newInt):
		if newInt.begin != self.start:
			print "Incorrect interval in node."
			return

		if not self.list:
			self.list += [newInt]
			self.max = newInt.end
			return

		index = 0
		isFirst = True
		for elem in self.list:
			if newInt.end >= elem.end:
				self.list.insert(index, newInt)
				if isFirst:
					self.max = newInt.end
				return
			index = index+1
			isFirst = False
		self.list.append(newInt)

	def __str__(self):
		string = "[" + str(self.start) + "," + str(self.max) + "]"
		for x in self.list:
			 string = string + ": " + str(x) + "\t"
		return string

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



#Dates
d1 = datetime.datetime(2000,12,12,12)
d2 = datetime.datetime(2000,12,12,13)
d3 = datetime.datetime(2000,12,12,14)
d4 = datetime.datetime(2000,12,12,15)
d5 = datetime.datetime(2000,12,12,16)
d6 = datetime.datetime(2000,12,12,17)
d7 = datetime.datetime(2000,12,12,18)

ti1 = TimeInterval(d1,d2)
ti2 = TimeInterval(d2,d3)
ti3 = TimeInterval(d2,d5)
ti4 = TimeInterval(d1,d6)
ti5 = TimeInterval(d3,d7)
ti6 = TimeInterval(d3,d6)

nodes1 = TimeIntervalNode(ti1)
nodes1.addInterval(ti4)
nodes2 = TimeIntervalNode(ti2)
nodes2.addInterval(ti3)
nodes3 = TimeIntervalNode(ti5)
nodes3.addInterval(ti6)

nodeArray = [nodes1, nodes2, nodes3]
tree = TimeIntervalTree(nodeArray)

print tree


