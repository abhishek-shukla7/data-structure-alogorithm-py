#missing number in the array

def miss(nums):
    n=len(nums)
    for i in range(0,n):
        if i not in nums:
            print(i)
            break

nums1=[1,0,3,4]
miss(nums1)
print("\n")

nums2=[9,6,4,2,3,5,7,0,1]
miss(nums2)


print("\n")
nums3=[3,0,1]
miss(nums3)

print("\n")
nums4=[0,1]
miss(nums4)

#Time Complexity=O(N2) 
#SPACE COMPLEXITY=O(1)


print("\n worst Solution: ")

def number(num):
    dict={}
    n1=len(num)

    for i in range(0,n1+1):
        dict[i]=0
    
    for nu in num:
        dict[nu]=1

    for k,u in dict.items():
        if u==0:
            return k
        

        
nums4=[1,3,5,0,4]
print(number(nums4))

#Time Complexity:-O(3N)->O(N)
#Space Complexity:-O(N)

print("\n Optimal Solution: ")
def miss_number(num4):
    n=len(num4)

    return n*(n+1)//2-sum(num4)


nump=[9,6,4,2,3,5,7,0,1]
print(miss_number(nump))

#time complexity=0(N)
#Space Complexity=O(1)