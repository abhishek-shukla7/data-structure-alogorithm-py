#Reverse an array using recusion 
def revArr(nums,left,right):
    if  left>=right:
        return

    nums[left],nums[right]=nums[right],nums[left]
    return(nums,left+1,right-1)


print("\n Full reverse: ")
n=[5,7,8,3,2,6,1,5,9]

print("Normal array: ",n)


#Full reverse len -1


revArr(n,0,len(n)-1)
print("Full revese:  ",n)


#only from the specific part of the reverese is 

print("\n Only specific part of the reverse: ")


n1=[4,5,6,2,3,1,7,9,8]
print("Normal Array:   ",n1)
revArr(n1,2,5)

print("Specific Array: ",n1)

#Time Complexity of this :O(N/2) Similar to O(N)
#Space Complexity of this :O(N/2) Similar to O(N)->Stack Space