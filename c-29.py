#Right rotate by k place
#Better Solution


print("\n Better through slicing: ")
nums=[3,9,5,6,7,2]
k=3
n=len(nums)
k=k%n
nums[:]=nums[k:]+nums[:k]
print(nums)

#Time Complexity=O(N)
#Space Complexity=O(1)

print("\n")

#Through brute force

print("Brute Force Solution: ")

nums1=[3,9,5,6,7,2]
for _ in range(0,k):
    e=nums1.pop()
    nums1.insert(0,e)

print(nums1)

#Time Complexity=O(R*n)
#Space Complexity=O(1)

#Optimal Solution:
print("\n optimal solution")
nums2 = [3, 9, 5, 6, 7, 2, 10, 9]
k1 = 5
n1 = len(nums2)

k1 = k1 % n1   # important

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Step 1: reverse last k elements
reverse(nums2, n1 - k1, n1 - 1)

# Step 2: reverse first n-k elements
reverse(nums2, 0, n1 - k1 - 1)

# Step 3: reverse whole array
reverse(nums2, 0, n1 - 1)

print(nums2)
#Time Complexity:





