# Longest Consecutive Sequence

nums1=[1,99,101,98,2,5,3,100]

def long(nums):
    n=len(nums)
    max_count=0

    for i in range(0,n):
        num=nums[i]
        count=1
        while num+1 in nums:
            count+=1
            num=num+1
        max_count=max(max_count,count)

    return max_count


print(long(nums1))


#TC=O(N2)
#SC=o(1)


