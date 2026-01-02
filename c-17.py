#chech string is palindrome or not 
#using recursion
def pali(str,left,right):

    if(left>=right):
        return True
    
    if(str[left]!=str[right]):
        return False
    
    pali(str,left+1,right-1)

s='nitin'

print("string is: ", pali(s,0,len(s)-1))


#Using For loop 

print("\n Palindrome using For loops: ")

s1='mom'
copy_n=s1

for ch in s1:
    z=s1[::-1]

if(z==copy_n):
    print("String is Plaindrome: ",s1)

else:
    print("String is not palindrome: ")


#Using While Loop

print("\n Using while loop recursion:  ")


def whi(s2):
    n=len(s2)
    l=0
    r=n-1

    while l<r:
        if s2[l]!=s2[r]:
            return False
        
        left+=1
        right-=1

        return True
    
    
    

s2='sahl'

print(whi(s2))

#time complxity=o(N/2) similar O(N)
#Space complexity=O(1)