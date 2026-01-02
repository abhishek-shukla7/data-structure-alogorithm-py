#Fibonacci Series
#Recursion

def func(num):
    if num==0 or num==1:
        return num
    
    return func(num-1)+func(num-2)


print(func(7))


#Time Complexity:O(2^N)
#Space Complexity:O(2^N)