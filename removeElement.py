class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0 
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                count = count + 1
                nums[j] = nums[i]
                j = j + 1 
        return count