#Moving zeros to the end 

#Worst case

def zero(num):
    n=len(num)
    temp=[]

    for i in range(0,n):
        if num[i]!=0:
            temp.append(num[i])
    
    nz=len(temp)
    for i in range(0,nz):
        nums[i]=temp[i]

    for i in range(nz,n):
        num[i]=0


nums=[1,0,2,4,3,0,0,3,5,1]
zero(nums)
print(nums)


#Time Complexity=O(N+N)->O(2N)->O(N)
#Space Complexity=O(N)


print('\n')


#Optimal Case
print("using for loops: ")

def move(num1):
    pos=0
    l=len(num1)

    if len(num1)==0:
        return

    for i in range(0,l):
        if num1[i]!=0:
            num1[pos]=num1[i]
            pos+=1

    for i in range(pos,l):
        num1[i]=0

num2=[1,2,0,4,3,0,0,3,5,1]
move(num2)
print(num2)



#using while loop 

print("\n Using while loop")

def whi(nu):
    if len(nu)<=1:
        return
    
    i=0
    while i<len(nu):
        if nu[i]==0:
            j=i+1

            while j<len(nu):
                if nu[j]!=0:
                    nu[i],nu[j]=nu[j],nu[i]
                    break
                j+=1
    
        i+=1

num3=[1,2,0,4,3,0,0,3,5,1]
whi(num3)
print(num3)




#time Complexity=O(n)
#Space Complexity=O(1)