######### Attempt 1, passes. #########
class NumArray:

    def __init__(self, nums: List[int]):
        acuum = [0] * (len(nums) + 1)
        for i in range(len(nums)-1, -1, -1):
            acuum[i] = nums[i] + acuum[i+1]
        self.p = acuum
        # print(self.p)        

    def sumRange(self, left: int, right: int) -> int:
        return self.p[left] - self.p[right+1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)



######### Attempt 2, left to right solution #########
class NumArray:

    def __init__(self, nums: List[int]):
        accum = 0
        self.p = [0]
        for n in nums:
            accum += n
            self.p.append(accum)
        # print(self.p)

    def sumRange(self, left: int, right: int) -> int:
        # let p[i] = n[0...i-1]
        # therefore if we want n from left to right
        # p[right+ 1] = n[0...right]
        # p[left] = n[0...left-1]
        # diff = n[left...right]
        return self.p[right+1] - self.p[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)