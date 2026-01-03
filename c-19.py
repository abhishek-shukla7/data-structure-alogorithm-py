#Selection Sort 

print("Selection sort with the ascending order: ")

def sort(num):
    n=len(num)
    for i in range(0,n):
        min_in=i
        for j in range(i+1,n):

            if(num[j]<num[min_in]):
                min_in=j
            
        num[i],num[min_in]=num[min_in],num[i]
            
l=[5,7,8,4,1,6,9,2]

sort(l)

print(l)

#Time complexity:-O(N(N+1)/2) SIMILAR to O(N^2)
#Space Complexity:-O(1)


#with the desccending order

print("\n with the descending order: ")

def sel(n1):
    k=len(n1)

    for i in range(0,k):
        max_in=i
        for j in range(i+1,k):
            if(n1[j]>n1[max_in]):
                max_in=j

        n1[i],n1[max_in]=n1[max_in],n1[i]


a=[5,7,8,4,1,6,9,2]
sel(a)
print(a)
