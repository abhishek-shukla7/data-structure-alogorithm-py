#Quick Sort

#Pick the pivot (BUt u have to take one and for the whole code not like u take first then last if u are taking first num than in whole code take the first nuumber only)
# it can be the first element
# It can be the last element 
# it can be middle element 
# it can be any random element

# Step 2 Put pivot at its correct position /Index

def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high

    while i<j:
        while i<=high and nums[i]<=pivot:
            i+=1

        while nums[j]>pivot:
            j-=1

        if i<j:
            nums[i],nums[j]=nums[j],nums[i]

    nums[low],nums[j]=nums[j],nums[low]
    return j

def quick_sort(nums,low,high):
    if low<high:
        p_index=partition(nums,low,high)
        quick_sort(nums,low,p_index-1)
        quick_sort(nums,p_index+1,high)



num=[4,1,7,6,3,2,8]
quick_sort(num,0,len(num)-1)
print(num)

# Best case 
#Time Complexity;O(logN*N)->O(NlogN)
#Space Complexity:O(1)

#Worst Case
#Time Complexity:O(N*N)->O(N2)
#Space Complexity:O(1)

