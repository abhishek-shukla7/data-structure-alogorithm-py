#Find the second largest element
from math import inf
nums=[55,32,97,-55,45,32,88,21]
print("Easy/Brute Force Solution")
#Method1
nums.sort()
print(nums[-2])

#method 2
n=len(nums)
print("\n",nums[n-2])

#TC->O(NlogN)
#SC->o(1)


#better solution
print("\n Better Solution")
def sec(num):
    large=float("-inf")
    s_large=float("-inf")
    n1=len(num)
    for i in range(0,n1):
        large=max(large,num[i])

    for j in range(0,n1):
        if num[j]>s_large and num[j]!=large:
            s_large=nums[j]
    

    return s_large

n2=[55,32,97,-55,45,32,88,21]
print(sec(n2))

#TC->0(N+N)=O(2N)->O(N)
#SC->O(1)


#Optimal
print("\n Optimal solution with tc and sc")
def opt(num3):
    l=float("-inf")
    sl=float("-inf")
    n3=len(num3)
    for i in range(0,n3):
        if(num3[i]>l):
            sl=l
            l=num3[i]

        elif num3[i]>sl and num3[i]!=l:
            sl=num3[i]
    return sl
    

n4=[55,32,97,-55,45,32,88,21]
print(opt(n4))

#TC->O(N)
#SC->O(1)


