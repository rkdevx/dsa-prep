class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        l = [1] * len(nums)
        for i in range(1,len(nums)):
            l[i] = l[i-1] * nums[i-1]

        R = 1
        for j in range(len(nums)-2,-1,-1):
            R *= nums[j+1]
            l[j] *= R

        return l
