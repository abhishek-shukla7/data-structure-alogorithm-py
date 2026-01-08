#Largest Element in a array

#METHOD 1

def large(num):
    lar=num[0]
    n=len(num)
    for i in range(0,n):
        lar=max(lar,num[i])  #Using max function
    return lar

    #     if(num[i]>lar):   #using if 
    #         lar=num[i]
    # return lar


nums=[55,32,-97,99,3,67]
print(large(nums))
print(nums)


#time complexity=O(N)
#Space complexity=O(N)



#Method 2
#giving the ininity value

def ele(num1):
    l=float("-inf")
    n1=len(num1)

    for i in range(0,n1):
        l=max(l,nums[i])
    
    return l


print(ele(nums))



