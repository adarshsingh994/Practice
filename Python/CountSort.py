import os

def countSort(arr):
    # Create a count array of length equal to maximum value in array
    countArray = [0]*(len(arr) + 1)

    # Increase the count of index from the given array
    for i in arr:
        countArray[i] += 1

    # Modify counts array so that each item contains sum of previous values
    sum = 0
    for i in range(len(countArray)):
        sum += countArray[i]
        countArray[i] = sum

    # Get the arranged index of each element from the count array
    outputArray = [0]*(len(arr))
    for i in arr:
        outputArray[countArray[i] - 1] = i
        countArray[i] -= 1

    return outputArray
if __name__ == '__main__':
    array = list(map(int, input().rstrip().split()))
    result = countSort(array)
    print(result)
