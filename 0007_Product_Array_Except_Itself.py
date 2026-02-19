# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.
# Follow-up: Could you solve it in O(n) time without using the division operation?

# Example 1:
# Input: nums = [1,2,4,6]
# Output: [48,24,12,8]

# Example 2:
# Input: nums = [-1,0,1,2,3]
# Output: [0,-6,0,0,0]

class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        # region Simple Solution
        # T -> O(n)
        # S -> O(n)
        # running_prod = 1
        # num_zeros = 0
        # for i in nums:
        #     if i != 0: running_prod *= i
        #     else: num_zeros += 1
        # if num_zeros > 1: return [0] * len(nums)
        # if num_zeros == 1: return [0 if i else running_prod for i in nums]
        # return [running_prod//i for i in nums]
        # endregion

        # region With Division Operaiton
        # T -> O(n)
        # T -> O(1) (O(n) -> for output array)
        output = [1]*len(nums)
        # prefix
        prefix_prod = 1
        for idx in range(len(nums)):
            output[idx] = prefix_prod
            prefix_prod *= nums[idx]
        # postfix
        postfix_prod = 1
        for idx in range(len(nums)-1, -1, -1):
            output[idx] *= postfix_prod
            postfix_prod *= nums[idx]

        return output
        # endregion