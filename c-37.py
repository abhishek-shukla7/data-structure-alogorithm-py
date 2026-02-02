#list problem (medium)
# leetcode 121
# Stock buy and sell 

#brute force
from math import inf


prices=[7,2,1,5,6,4,8]


def price(num):
    n=len(num)
    max_profit=0

    for i in range(0,n):
        pick=num[i]
        for j in range(i+1,n):
            sell=num[j]
            if (sell>pick):
                result=sell-pick

                if(result > max_profit):
                
                    max_profit=result

    print(max_profit)
    return max_profit

# print(price(prices))
price(prices)

#Time Complexity:-0(n(n+1)/2) similar O(n2)
#space complexity:-o(1)




#Optimal Solution
print("\n Optimal Way:  ")

def opt(num1):
    n1=len(num1)
    min_profit=float("inf")
    max_profit1=0


    for i in range(0,n1):

        min_profit=min(min_profit,num1[i])

        max_profit1=max(max_profit1,num1[i]-min_profit)


    return max_profit1

print(opt(prices))

#TC=O(N)
#SC=O(1)     
