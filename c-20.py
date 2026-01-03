#Bubble Sort

nums=[5,1,6,8,2,4,9]

def bubble(num):
    n=len(num)
    for i in range(n-2,-1,-1):

        for j  in range(0,i+1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]



bubble(nums)
print(nums)
