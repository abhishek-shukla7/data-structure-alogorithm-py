#Recursion using parameter

# question print(x,N times)

def func(x,n):
    if n==0:
        return
    print(x)
    func(x,n-1)

func(15,4)


print("\n")

#print 1 to N using recursion
#using head recursion
print("print 1 to N")

def para(l,m):
    if l>m:
        return
    print(l)
    para(l+1,m)

para(1,5)


#Time complexity-o(n)
#space complexity-o(n)

print("\n")

print("tail recursion printing 1 to N Backtracking ")

#Tail recursion:
def tail(i,j):
    if i>j:
        return
    tail(i,j-1)
    print(j,end=" ")

tail(1,5)
