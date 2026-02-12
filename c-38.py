nums1=[5,10,-3,-1,-10,6]


def rearrange(nums):
    n=len(nums)
    pos=[]
    neg=[]

    for i in range(0,n):
        if nums[i]>0:
            pos.append(nums[i])

    for j in range(0,n):
        if nums[j]<0:
            neg.append(nums[j])

    # print(pos)
    # print(neg)

    for i in range(0,len(pos)):
        nums[2*i]=pos[i]
        nums[(2*i)+1]=neg[i]
    
    return nums

print(rearrange(nums1))

# TC->O(n+n/2)
# O(n)


#optimal

def opt(num):
    n1=len(num)
    result=[0]*n1
    posIndex,negIndex=0,1
    for i in range(0,n1):
        if num[i]>=0:
            result[posIndex]=num[i]
            posIndex+=2
        else:
            result[negIndex]=num[i]
            negIndex+=2
    
    return result

print(opt(nums1))

#TC=O(N)
#SC=O(1)