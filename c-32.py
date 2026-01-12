#Merge Two Sorted Array

#using Sets
from unittest import result


nums3=[1,1,1,2,4,6,9]
nums4=[1,2,3,6,7,8,9,10]

nums5=nums3+nums4
print(nums5)
nums5=set(nums5)
print(nums5)


#using function

print("\n Using Function: ")

def merge(nums1,nums2):
    num=[]
    n=len(nums1)
    nz=len(nums2)
    i=j=0

    while i<n and j<nz:
        if nums1[i]<=nums2[j]:
            if len(num)==0 or num[-1]!=nums1[i]:
             num.append(nums1[i])
            i+=1
        else:
            if len(num)==0 or num[-1]!=nums2[j]:
                num.append(nums2[j])
            j+=1

    while i<n:
        if len(num)==0 or num[-1]!=nums1[i]:
            num.append(nums1[i])
        i+=1

    while j<nz:
        if len(num)==0 or num[-1]!=nums2[j]:
            num.append(nums2[i])
        j+=1

    return num

print(merge(nums3,nums4))

#Time Complexity=O(N+M)
#Space Complexity=O(1) OPTIMAL AND WORST CASE:-O(N+M)




