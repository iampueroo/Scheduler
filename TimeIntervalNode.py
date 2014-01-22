from TimeInterval import TimeInterval

#Node for Tree composed of a list all TimeIntervals that start at same time
class TimeIntervalNode:
	def __init__(self, interval):
		self.list = [interval] # Ordered list of intervals with same beginning.
		self.start = interval.begin # The starting time of all intervals
		self.max = interval.end # Max endpoint of any interval in list/subtree
		self.leftChild = None
		self.rightChild = None

	#List is ordered from highest to lowest end point
	def addInterval(self, newIntv):
		if newIntv.begin != self.start:
			print "Incorrect interval in node."
			return

		# If empty list, add and set max
		if not self.list:
			self.list += [newIntv]
			self.max = newIntv.end
			return

		# Add to list in order
		index = 0
		isFirst = True
		for elem in self.list:
			if newIntv.end >= elem.end:
				self.list.insert(index, newIntv)
				if isFirst:
					self.max = newIntv.end
				return
			index = index+1
			isFirst = False
		self.list.append(newIntv)

	def __str__(self):
		string = "[" + str(self.start) + "," + str(self.max) + "]"
		for x in self.list:
			 string = string + ": " + str(x) + "\t"
		return string