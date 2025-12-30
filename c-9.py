#print factor of a given number

#in this u have to run the whole code and its time complexity is oredr of n

num=int(input("enter the number u want to print: "))
result=[]

# for j in range(1,num+1):
#     if(num%j==num):
#         print("number is prime: ",j)

# else:
for i in range(1,num+1):
    if (num % i == 0):
        result.append(i)
               
print(result)


print("\n")


#second way in this if we go only half of the way to the number
# then it after teh half 
# example-take 10 from starting factor of 10 is ,1,2,5 but after 5 there is no any number before then 
# so in this u have to go half and then print the last num

#better solution

print("second appproach: ")
num2=10

result1=[]

for k in range(1,(num2//2)+1):
    if(num2%k==0):
        result1.append(k)

result1.append(num2)

print(result1)

#optimal solution:
#in this we will only go half of teh code

print("\n ")
print("Optimal Way ")

from math import sqrt
num3=36
result3=[]

for l in range(1,int(sqrt(num3))+1):
    if(num3%l==0):
        result3.append(l)
        if num3//l!=l:
            result3.append(num3//l)

result3.sort()

print(result3)








