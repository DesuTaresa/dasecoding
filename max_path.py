def maxPathSum(arr1, arr2):
    i = j = 0
    sum1 = sum2 = 0
    result = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        else:
            # common element
            result += max(sum1, sum2) + arr1[i]
            sum1 = sum2 = 0
            i += 1
            j += 1

    # add remaining elements
    while i < len(arr1):
        sum1 += arr1[i]
        i += 1

    while j < len(arr2):
        sum2 += arr2[j]
        j += 1

    result += max(sum1, sum2)
    return result


Arr1 = [1, 5, 7, 8]
Arr2 = [2, 3, 7, 10, 12]

print(maxPathSum(Arr1, Arr2))
