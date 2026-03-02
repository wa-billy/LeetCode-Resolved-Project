def twoSum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print(f'{nums[i]} {nums[j]} {target}')
                if nums[j] == target - nums[i]:
                    print([i, j])
                    return [i, j]
                elif target == nums[i] + nums[j]:
                    print([i, j])
                    return [i, j]
                else:
                    print(f'{nums[i]} {nums[j]} {target}')
                    if nums[i] == target - nums[j]:
                        print([j, i], 'from if')
                        return [j, i]
                    elif target == nums[j] + nums[i]:
                        print([j, i], 'from elif')
                        return [j, i]

twoSum(nums=[3,2,95,4,-3], target=92)