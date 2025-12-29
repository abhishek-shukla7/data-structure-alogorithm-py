#palindrome of a number


n=123


copy_n=n

rev=int(str(n)[::-1])

print("so the reverse number is this : " ,rev)

if(rev==copy_n):
    print("number is palindrome ",copy_n)

else:
    print("number is not a palindrome: ",copy_n)


print("\n")


#second way 

print("second approach for the palindrome: ")

num=456

rev1=0


while n>0:
    digit=num%10
    rev1=rev1 * 10 + digit
    n=n//10


if(rev1==num):
    print(" number is palindrome: ",num)

else:
    print("number is not palindcrome: ",num)



print("\n")


#same for the string 

print("checking string is palindrome or not")


str1="nitin"

copy_str=str1


rev2=str1[::-1]


if(rev2==copy_str):
    print("string is palindrome: ",str1)

else:
    print("string is not palindrome",str1)
