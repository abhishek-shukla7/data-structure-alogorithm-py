#Linear Search

num=[5,3,9,8,1,6,4,-10,-100]

print("Using For lOOP:")
def linear(nums,target):
    n=len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i
        
    return -1

print(linear(num,2))
#TC=O(N)
#SC=O(1)


print("\n With While lOOP")

def search(num1,target1):
    i=0
    while i<len(num):
        if num[i]==target1:
            print(i)
        
        i+=1

    return -1


print(search(num,99))

