class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        ans = {}

        for i in range(len(nums)):
            checknum = target - nums[i]
            if (checknum in ans):
                return [ans[checknum], i]
            ans[nums[i]] = i
            
