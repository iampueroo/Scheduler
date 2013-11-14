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

#testing
