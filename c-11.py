#hashing in py
#question u have to print the number of of m htey how many times occur in the n


n=[5,3,2,2,1,5,5,7,5,10]

m=[10,111,1,9,5,67,2]

for num in m:
    count=0
    for x in n:
        if x==num:
            count+=1
    print(f"{num} occur {count} times")

    #time complexity 0(m*n)
    #space complexity 0(1)

#Hashing way

print("\n")

n1=[5,3,2,2,1,5,5,7,5,10]

m1=[10,111,1,9,5,67,2]

hash_list=[0]*11

for el in n1:
    hash_list[el]+=1

for val in m1:
    if val<1 or val>10:
        print(f"{val} occurs 0 times")
    else:
        print(f"{val} occur {hash_list[val]} times")

#time complexity=o(N*M)
#SPACE COMPLEXITY=0(11)->O(1) ALWAYS CONSTANT




