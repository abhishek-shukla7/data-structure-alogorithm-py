#Armstrong number
num=153
n=num
copy_n=n
count=0

while copy_n>0:
    count+=1
    copy_n=copy_n//10

print(count)

sum=0
while n>0:
    digit=n%10
    sum+=digit ** count
    n=n//10

if(num==sum):
    print("number is armstrong: ",num)


else:
    print("number is not a armstrong number: ")


print("\n ")


#second way 

print("second way of th code ")

num2=153

copy_n2=num2

nod=len(str(num2))

total=0

while num2>0:
    digit2=num2%10
    total+=digit2 ** nod

    num2=num2//10

if(copy_n2==total):
    print("number is armstrong: ",copy_n2)

else:
    print("number is not a armstrong number: ")


