#Given an array of numbers, nums, return an array of numbers products
#where products[i] is the product of all nums[j], j != i

l=[1,2,3,4,5]

left = [0]*len(l)
left[0]=1
right = [0]*len(l)
right[len(l)-1]=1

for i in range(1,len(l)):
    left[i]=l[i-1]*left[i-1]
for i in range(len(l)-2,-1,-1):
    right[i]=right[i+1]*l[i+1]

print(left)
print(right)

new=[0]*len(l)

for i in range(0, len(l)):
    new[i]=left[i]*right[i]

print(new)
