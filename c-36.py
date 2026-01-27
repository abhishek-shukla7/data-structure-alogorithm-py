#Maximum Sub array
nums=[-2,1,-3,4,-1,2,1,-5,4]


#Brute force
def max_sum(num):
    n=len(num)
   
    maxi=float("-inf")

    for i in range(0,n):
        total=0
        for j in range(i,n):
            total=total+nums[j]
            maxi=max(maxi,total)

    return maxi


print(max_sum(nums))

#Time Complexity:-O(N(N+1)/2)->O(N2)
#Space Complexity:-O(1)



