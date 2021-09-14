class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use sum from 0 to n to get the missing number
        # n*(n-1)/2 - sum(of all the numbers in nums) 
        
        num_sum = 0
        for i in range(len(nums)):
            num_sum += nums[i]
        
        n = len(nums) + 1                  # including n since there is a missing number
        
        return (n*(n-1)//2) - num_sum