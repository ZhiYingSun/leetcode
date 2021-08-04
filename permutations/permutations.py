class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        backtracks(perms, [ ], nums)
        return perms

def backtracks(perms: List[List[int]], temp_list: List[int], nums: List[int]):
    if (len(temp_list) == len(nums)):
        # must make a copy of temp_list because it is changed in recursion!!
        perms.append(temp_list[:])
    else:
        for i in range(len(nums)):
            if nums[i] in temp_list:
                continue
            temp_list.append(nums[i])
            backtracks(perms, temp_list, nums)
            temp_list.pop()