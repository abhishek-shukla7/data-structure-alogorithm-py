#Store frequency in dictionary

#method 1

nums=[5,6,7,7,1,9,1,3,5,1,1,5]

dict={}

for i in range(0,len(nums)):
    if nums[i] in dict:
        dict[nums[i]]+=1
    else:
        dict[nums[i]]=1

print(dict)

print(dict[1])