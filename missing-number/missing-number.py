class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set()                    # use set over list or nums directly bc set look up is O(1)
        
        for i in range(len(nums)):      # space and time complexity O(n)
            seen.add(nums[i])
        
        for i in range(len(nums) + 1):
            if i not in seen:
                return i