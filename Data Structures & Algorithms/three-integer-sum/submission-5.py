class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = len(nums) - 1
    
        nums.sort()
        ans = []

        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            k = i + 1
            j = len(nums) - 1
            
            while k < j:
                total = nums[i] + nums[k] + nums[j]

                if total == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    k += 1
                    j -= 1

                    while k < j and nums[k] == nums[k-1]:
                        k += 1

                    while k < j and nums[j] == nums[j+1]:
                        j -= 1
                
                elif total < 0:
                    k += 1
                else:
                    j -= 1
            
            i += 1
           
        return ans