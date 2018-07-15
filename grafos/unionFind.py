def getParent(no):
	
	global parents
	
	if no == parents[no]: return parents[no]
	else:
		
		parents[no] = getParent(parents[no])
		
		return parents[no]

def union(no1, no2):
	
	global parents
	
	no1Parent = getParent(no1)
	no2Parent = getParent(no2)
	
	parents[no2Parent] = no1Parent

def isSameSet(no1, no2):
	
	return getParent(no1) == getParent(no2)
