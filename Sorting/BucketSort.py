import math

def insertionSort(customList):
	for i in range(1,len(customList)):
		key = customList[i]
		j = i-1
		while j>=0 and key<customList[j]:
			customList[j+1] = customList[j]
			j -= 1
		customList[j+1] = key
	return customList


def bucketSort(customList):
	numberOfBuckets = round(math.sqrt(len(customList)))
	maxVal = max(customList)
	arr = []

	for i in range(numberOfBuckets):
		arr.append([])

	# Add elements into appropriate buckets
	for j in customList:
		bucket_index = math.ceil(j*numberOfBuckets/maxVal)
		arr[bucket_index-1].append(j)

	# Sort individual buckets
	for b in range(numberOfBuckets):
		arr[b] = insertionSort(arr[b])

	# Merge the buckets
	k = 0
	for i in range(numberOfBuckets):
		for j in range(len(arr[i])):
			customList[k] = arr[i][j]
			k += 1
	return customList


l = [4,7,2,1,9,4,3]
print(insertionSort(l))
print(bucketSort(l))