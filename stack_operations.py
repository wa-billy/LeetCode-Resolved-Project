target = [2,3,4]
n = 4
result = []
nums = []
for i in range(1, n+1):
    result.append("Push")
    nums.append(i)
    print(nums)
    if nums != target[:i]:
        result.append("Pop")
        nums.pop()
    elif nums == target:
        break
print(result)
