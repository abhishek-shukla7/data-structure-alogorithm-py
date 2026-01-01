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

print("with the list ")

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


#With the dictionary

print("\n")
print("With the dictionary")

n2=[5,3,2,2,1,5,5,7,5,10]

m2=[10,111,1,9,5,67,2]

hash_dict={}

for el1 in n2:
    if el1 in hash_dict:
        hash_dict[el1]+=1

    else:
        hash_dict[el1]=1


for val2 in m2:
    print(f"{val2} occurs {hash_dict.get(val2,0)} times")
    

#Character hashing

# constrainst:
# 1) 'a'<=s[i]<='z'
# ascii =97-122


print("\n")
print("character hashing  ")

s=['a','z','y','x','y','y','z','a','a','a','a']
q=['d','a','y','x']

hash_list1=[0]*123

for ch in s:
    ascii_val=ord(ch)
    index=ascii_val-97
    hash_list1[index]+=1


for ch in q:
    ascii_val=ord(ch)
    index=ascii_val-97
    print(f" {ch} occurs {hash_list1[index]} times")

#time complexity=o(N+M)
#SC->0(26)
