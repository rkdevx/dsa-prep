class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        

        c = 1
        for i in nums:
            new_val = c * i
            left.append(new_val)
            c = new_val
        
        c = 1
        for i in nums[::-1]:
            new_val = c * i
            right.append(new_val)
            c = new_val
        
        right = right[::-1]

        print("left", left)
        print("right", right)

        res = [right[1]]

        for idx in range(1,len(nums)-1):
            res.append(left[idx-1] * right[idx+1])

        res.append(left[-2])
        return res
