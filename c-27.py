#Remove Duplicaates from sorted array in place and count the value how many are in the list

nums=[1,1,1,2,3,4,4,7,9,9,9,10]

#first way u can go for the set because set stores only unique value in it
print("Using set most easiest: ")

set1=set(nums)
print(type(set1))
print(len(set1))
print(set1)
print("\n")

#Second way(Brute force)

nums1=[1,1,1,2,3,4,4,7,9,9,9,10]
n=len(nums1)
fre_map={}
j=0
for i in range(0,n):
    fre_map[nums1[i]]=0

for k in fre_map:
    nums1[j]=k
    j+=1

print("It gives the starting unique element: ",nums1)
print("Finally the total length of the unique element: ",j)

#Worst Case-------
#Time complexity:O(2N) -> O(N)
#space Complexity:O(N)

#OPTIMAL CASE

print("\n")
print("Optimal Solution")

num2=[1,1,1,2,3,4,4,7,9,9,9,10]

def sort(num):
    n=len(num)
    
    if n==1:
        return 1
    
    i=0
    j=i+1
    while j<n:
        if num[j]!=num[i]:
            i+=1
            num[i],num[j]=num[j],num[i]
        j+=1
    return i+1


print(f"total value of unique element :{sort(num2)}")
print(num2)
            
#Time Complexity:O(N)
#Space Complexity:O(1)









