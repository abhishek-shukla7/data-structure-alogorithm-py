# Max Consecutive Ones

num=[1,1,0,1,0,1,1,1,1,0,1,1]


def consecutive(nums):
    n=len(nums)
    count=0
    max_count=0
    for i in range(0,n):
        if nums[i]==1:
            count+=1
            max_count=max(max_count,count)
        else:
            count=0
    return max_count

                  
print(consecutive(num))

#Time Complexity=O(N)
#Space Complexity=O(1)
