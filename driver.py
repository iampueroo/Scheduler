import datetime
from TimeIntervalTree import TimeIntervalTree
from TimeIntervalNode import TimeIntervalNode
from TimeInterval import TimeInterval

	

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

# Need constants

# Range and Delta
start = datetime.datetime(2000,12,12,10,00)
end  = datetime.datetime(2000,12,12,16,00)
timeDelta = datetime.timedelta(minutes=30)

shiftBegin = start
shiftInterval = TimeInterval(shiftBegin, shiftBegin+timeDelta) 
tree.addInterval(shiftInterval)

while shiftBegin < end:
	shiftInterval = TimeInterval(shiftBegin, shiftBegin+timeDelta) 
	#tree.addInterval(shiftInterval)	
	shiftBegin += timeDelta

print "After adding the shifts:"
print ""
print tree