n = int(input())
nums = list(map(int,input().split()))
max_index = 0
next_max = -1

for i in range(1,n):
    if nums[i] > nums[max_index]:
        next_max = max_index
        max_index = i
    elif nums[i] > nums[next_max]:
        next_max = i

print(max_index+1,nums[next_max])