# nuts and bolts
# If you have a list of nuts and a list of bolts that are unsorted, take an input of both lists
# and return a list of tuples of the matching pairs. (based on size, but those can be represented
# by numbers) Both lists have the same number of elements. 
#Your helper function takes an input of a nut and a bolt and returns 'True' if they are a match
#and 'False' if they aren't

nuts = [2,3,1,4]
bolts = [1,2,4,3]

# helper function:
def compare(nut, bolt):
	if nut == bolt:
		return True
	else:
		return False

# runtime: O(n^2) - better solution would be implementing a binary tree

def find_matches(nuts, bolts):
	
	results = []

	for nut in nuts:
		for bolt in bolts:
			if compare(nut,bolt) == True:
				match = (nut,bolt)
				results.append(match)
	return results


