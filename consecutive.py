nums = [1,1,0,1,1,1]
num = []
for i, j in enumerate(nums):
    if j == 0:
        num = []
    if j == 1:
        num.append(j)
print(nums.split(0))