class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Idea: compute all multiples up to i from the left
        and do the same for all multiples up to i, from the right,
        using prefix and postfix arrays

        then ans is just pre[i] * post[i]
        """
        accum = 1
        pre = []
        for n in nums:
            pre.append(accum)
            accum *= n
        # print(pre)
        post = [0] * len(nums)
        accum = 1
        for i in range(len(nums)-1,-1,-1):
            post[i]= accum
            accum *= nums[i]
        # print(post)
        ans = [pre[i] * post[i] for i in range(len(nums))]
        return ans
