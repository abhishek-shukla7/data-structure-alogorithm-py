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
print("\n")

#better  approach
print("better approach")

def better(nums2):
    n1=len(nums2)
    nums2.sort()
    count=0
    last_smaller=float("-inf")
    longest=0

    for i in range(0,n1):
        num1=nums2[i]
        if num1-1==last_smaller:
            count+=1
            last_smaller=num1

        elif num1!=last_smaller:
            count=1
            last_smaller=num1

        longest=max(longest,count)

    return longest

print(better(nums1))

#Tc=O(NLOGN)+O(N)=O(NlogN+N)
#SC=O(1)





