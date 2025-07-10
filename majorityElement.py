class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = nums[0]
        count = 0
        for i in range(len(nums)):
            if count == 0:
                current = nums[i]
                count = count + 1
            elif nums[i] == current:
                count = count + 1 
            elif nums[i] != current:
                count = count - 1
        return current