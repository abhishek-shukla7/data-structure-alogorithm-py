# Two Sum Problem 
nums=[5,9,1,2,4,15,6]

def two_sum(num,target):
    n=len(num)
    for i in range(n):
        for j in range(i+1,n):
           if num[i]+num[j]==target:
                return i,j


print("usign for loop ",two_sum(nums,13))

# TIME COMPLEXITY=O(N(N+1)/2) SIMILAR O(N2)
#SPACE COMPLEXITY=O(1)



print("\n")
def sum1(num1,target1):
    n1=len(num1)
    i=0
    
    while i<n1:
        j=i+1
        while j<n1:
            if num1[i]+num1[j]==target1:
                return i,j
            j+=1
        i+=1


print("Using while loop",sum1(nums,13))





