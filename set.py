a=[1,2]
b=[2,3]

def union(set1,set2):
        print(set1+[x for x in set2 if (x not in set1)])
              
def intersection(set1,set2):
	print([x for x in set1 if (x in set2)])
	
def setDifference (set1, set2):
	print([x for x in set1 if (x not in set2)])

def symmetricDifference(set1,set2):
	print([x for x in set1 if (x not in set2)]+[x for x in set2 if (x not in set1)])
	
def cartesianProduct(set1,set2):
	print([(x,y) for x in set1 for y in set2])
