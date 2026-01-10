#Right Rotate Array by 1 Place

#First Way Slicing 
print("\n first way with slicing: ")
nums=[5,-2,3,9,0,6,10,7]

nums[:]=[nums[-1]]+nums[0:-1]
print(nums)

#Time Complexity=O(1)+O(N-1)=O(N)
#Space Complexity=O(1)

#Second way using for loopp 
print("\n Second way using for loop: ") 

num1=[5,-2,3,9,0,6,10,7]
n=len(num1)
temp=num1[-1]

for i in range(n-2,-1,-1):
    num1[i+1]=num1[i]

num1[0]=temp

print(num1)

#Time Complexity:O(N-1)=O(N)
#Space Complexity:O(1)






