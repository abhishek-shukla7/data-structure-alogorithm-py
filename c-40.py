# Learn about 2D array
# Matrix
  
nums=[[5,20,3],[7,-10,9],[1,-52,6]]

print(nums)
row=len(nums)
cols=len(nums[0])
sum=0

for i in range(0,row):
    for j in range(0,cols):
        print(nums[i][j],end=" ")
        sum+=nums[i][j]
    print()
print(sum)

print("\n printing the upper trainagle \n")

nums1=[[5,10,8],[7,6,3],[2,1,9]]
#MY way code
for k in range(0,row):
    for l in range(0,cols):
        if nums1[k][l]==nums1[1][0]:
            continue
        elif nums1[k][l]==nums1[2][0]:
            continue
        elif nums1[k][l]==nums1[2][1]:
            continue
        else:
            print(nums1[k][l],end=" ")
    print()


print("\n ")

print("Better way")
row1=len(nums1)
cols1=len(nums1[0])
for k in range(0,row1):
    for l in range(0,cols1):
        if l>=k:
            print(nums1[k][l],end=" ")
        else:
            print("*",end=" ")
    print()

print("\n Print the lower triangle: ")

for k in range(0,row1):
    for l in range(0,cols1):
        if k>=l:
            print(nums1[k][l],end=" ")
        else:
            print("*",end=" ")
    print()

print("\n Print diagonal: ")
for k in range(0,row):
    for l in range(0,cols):
        if k==l:
            print(nums1[k][l],end=" ")
        else:
            print("*",end=" ")
    print()

print("\n Print another side diagonal: ")

for k in range(row1):
    for l in range(cols1):
        if l==row1 -1 -k:
            print(nums1[k][l],end=" ")
        else:
            print("*",end=" ")

    print()
