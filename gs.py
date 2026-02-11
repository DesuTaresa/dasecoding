def maxSubarraySum( arr, k): 
    wsum=0
    msum=0
    for i in range(k):
        wsum+=arr[i]
    for i in range(k,len(arr)):
        wsum=wsum+arr[i]-arr[i-k]
        msum=max(msum, wsum)
    return msum