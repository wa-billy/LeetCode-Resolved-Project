def findErrorNums(nums: list[int]) -> list[int]:
        n, a, b = len(nums), sum(nums), sum(set(nums))
		
        s = n*(n+1)//2
        
        return [a-b, s-b]
        
print(findErrorNums(nums=[4,3,2,7,8,2,3,1]))