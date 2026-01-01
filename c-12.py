#recursion theory it calls itself at 987 times after that i throws the error 
# and we can also set the value like setrecursionlimit(200 0) then it will run the code for 2000 times then it stops



#print the anirudh 4 times using recursion

#this is known as hash recursion 
# this is first we call the job then we call the function this is head 

#and in the tail we call the function first then the job 


print("Head Recursion ")
count=0
def name():
    global count
    if count==4:
        return
    print("anirudh")
    count+=1
    name()

name()

print("\n")
#Tail recursion 
#print name n time 4 times 


print("Tail recursion")

count1=0

def tail():
    global count1
    if count1==4:
        return
    count1+=1
    tail()
    print("Anirudh")


tail()
    





