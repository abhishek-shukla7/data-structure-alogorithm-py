#count the number of digit 

print("\n")

from math import log10


n=54785

count=0

while n>0:
    count+=1
    n=n//10

print("number of digit in n:= ",count)


print("\n Second way ")

#second way wwe can use log 10

#in this if we take anyone number with the log 10 (5438) it gives=3.73 
# after if we add 1 int that it become 4.73
# then if we convert float to int then it gives only 4 so its the number of digit 

n=5438

def log(n):
    print("so the number of digit by log : ",int(log10(n)+1))


log(n)