
# Given an array with subarrays containing integers, 
#return the subarray with the greatest average.
# The subarrays can have multiple (or no) integers. 
# edgecases: empty subarray, empty array, value of 0 or negative numbers

nums = [[1,2],[2,4,6],[7], [], [-5,-9]]

# runtime: O(n * m)

def findMaxAvg1():
	
	max_avg = None
	for num in nums:
		if num > max_avg:
			max_avg += sum(num)// float(len(num))
			avg_subarray = num

	return max_avg

#another solution:
#runtime: O(n * m) + N(log n) + O(1) 
def findMaxAvg2():
	
	avg_dict = {}
	for num in nums:
		avg = sum(num)// float(len(num))
		if avg_dict[avg] not in avg_dict:
			avg_dict[avg] = [num]
		else: 
			#taking into account multiple unique avgs
			avg_dict[avg].append(num)

	max_avg = max(avg_dict.keys())
	return avg_dict[max_avg][0]
