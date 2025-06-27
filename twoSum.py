class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in myDict:
                return [myDict[ans], i]
            else:
                myDict[nums[i]] = i
        return 

        