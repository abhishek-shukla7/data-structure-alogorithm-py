#Sorted array 

def sort(num):
    n=len(num)
    for i in range(0,n):
        for j in range(0,i+1):
            if(num[j])>num[i+1]:
                return False
    return True

nums=[3,16,6,8,9,10,20]
print(sort(nums))

#Time Complexity:O(N)
#Space Complexity:O(1)