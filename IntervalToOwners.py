import TimeInterval
import Owner

'''

'''
class IntervalToOwners:
	def __init__(self, interval, owners):
		self.interval = interval
		self.owners = owners
	
	def isEmpty(self):
		if self.owners:
			return False
		else:
			return True

	def assignOwner(self):
		corrOwn = Owner("", 9000)
		for o in owners:
			if corrOwn.hours > o.hours or (corrOwn.hours == o.hours and corrOwn.hoursLeft > o.hoursLeft):
				corrOwn = o
			o.hoursLeft = o.hoursLeft-1
		corrOwn.hours = corrOwn.hours+1
		self.interval.owner = corrOwn

	def ownerWithMaxHoursLeft(self):
		for e in employees:
			if most is None or e.hoursLeft > most.hoursLeft:
				most = e;
		return most

