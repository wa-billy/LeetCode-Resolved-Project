nums = [4,3,2,7,8,2,3,1]
some = [i for i in range(1, len(nums)+1)]
print(list(set(some) - set(nums)))