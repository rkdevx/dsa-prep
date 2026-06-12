class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        s = set(nums)
        nums.sort()

        for i in range(len(nums)):
            curr = 1
            counter = 1
            if nums[i]-1 not in s:
                print("start is:-",nums[i])
                for j in range(i, len(nums)):
                    if nums[i] + counter == nums[j]:
                        counter+=1
                        curr+=1
            res = max(res, curr)

        return res



        