#Factorial of a a number


#Functional Recursion

def fact(n):
   
    if(n==1):
        return 1
    
    return n*fact(n-1)


print(fact(3))

#Time Complexity=O(n)
#Space Complexity=O(n)->Stack Space
