#insertion sort

def insertion(nums):
    n=len(nums)
    
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1

        nums[j+1]=key

n1=[3,5,6,4,8,9,10,7,1]

insertion(n1)
print(n1)


#Time Complexity:O(N(N+1))/2 SIMILAR TO O(N^2)
#Space Complexity:O(1)