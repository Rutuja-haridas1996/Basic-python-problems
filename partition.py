# Partition array: 19 17 16 13 11 10 9 7 6 2 into 2 equal parts.

def findPartiion(arr, n) :
	Sum = 0
	# Calculate sum of all elements
	for i in range(n) :
		Sum += arr[i]
    # check if sum/2 != odd
	if (Sum % 2 != 0) :
		return 0
	part = [0] * ((Sum // 2) + 1)

	# Initialze the part array as 0
	for i in range((Sum // 2) + 1) :
		part[i] = 0

	# Fill the partition table in bottom up manner
	for i in range(n) :
		for j in range(Sum // 2, arr[i] - 1, -1) :
			if (part[j - arr[i]] == 1 or j == arr[i]) :
				part[j] = 1

	return part[Sum // 2]

arr = [19 ,17 ,16 ,13 ,11 ,10 ,9 ,7 ,6 ,2 ]
n = len(arr)

if (findPartiion(arr, n) == 1) :
	print("Can be divided into two subsets of equal sum")
else :
	print("Can not be divided into two subsets of equal sum")

