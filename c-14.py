#Recusion using parameterized and functional recursion

#Sume of 1 to N natural number
# like 10-> 1+2+3+4+5+6+7+8+9+10

#Parameterized
def add(total,x,y):

    if(x>y):
        print(total)
        return
    add(total+x,x+1,y)
    
add(0,1,5)

print("\n")


#Functional Recursion

print("Functional Recursion: ")

def fun(n):
    if n==1:
        return 1
    return n+fun(n-1)



print(fun(5))

#factorial of number thorugh recursion 

print("\n")
print("Factorial through functional recursion: ")

def fact(l):
    if l==1:
        return 1
    return l*fact (l-1)

print(fact(3))


# For all the code 
#time complexity O(n)
#space complexity O(N):-Stack space


