# Holds two DateTime objects to represent a time interval.
class TimeInterval:
	def __init__(self, begin, end):
		self.begin = begin
		self.end = end
		self.owner = None

	'''
	Returns true if only begin and end match.
	'''
	def equals(self, other):
		return self.begin == other.begin and self.end == other.end

	'''
	Returns true only if interval matches and owner matches.
	'''
	def equalsWithOwner(self, other):
		return self.equals(other) and self.owner is not None and self.owner == other.owner
	
	def __str__(self):
		return str(self.begin) + " - " + str(self.end)
