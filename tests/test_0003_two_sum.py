import pytest
import sys
sys.path.insert(0, '..')
from importlib import import_module

# Import the solution
solution_module = import_module('0003_Two_Sum')
Solution = solution_module.Solution


class TestTwoSum:
    def setup_method(self):
        self.solution = Solution()

    def _verify_result(self, nums, target, result):
        """Helper to verify the result is valid"""
        i, j = result[0], result[1]
        assert i != j, "Indices must be different"
        assert i < j, "Smaller index should come first"
        assert nums[i] + nums[j] == target, f"nums[{i}] + nums[{j}] should equal {target}"

    # ==================== SIMPLE TESTS ====================

    def test_simple_adjacent_pair(self):
        """Simple case: adjacent elements sum to target"""
        nums = [3, 4, 5, 6]
        target = 7
        result = self.solution.two_sum(nums, target)
        assert list(result) == [0, 1]

    def test_simple_non_adjacent_pair(self):
        """Simple case: non-adjacent elements sum to target"""
        nums = [4, 5, 6]
        target = 10
        result = self.solution.two_sum(nums, target)
        assert list(result) == [0, 2]

    # ==================== EDGE CASES ====================

    def test_two_elements(self):
        """Edge case: minimum array size (2 elements)"""
        nums = [1, 2]
        target = 3
        result = self.solution.two_sum(nums, target)
        assert list(result) == [0, 1]

    def test_pair_at_end(self):
        """Edge case: matching pair at the end of array"""
        nums = [1, 2, 3, 4, 5]
        target = 9
        result = self.solution.two_sum(nums, target)
        assert list(result) == [3, 4]

    def test_negative_numbers(self):
        """Edge case: array with negative numbers"""
        nums = [-3, 4, 3, 90]
        target = 0
        result = self.solution.two_sum(nums, target)
        assert list(result) == [0, 2]

    def test_negative_target(self):
        """Edge case: negative target sum"""
        nums = [-5, -3, 1, 2]
        target = -8
        result = self.solution.two_sum(nums, target)
        assert list(result) == [0, 1]

    def test_zero_target(self):
        """Edge case: target is zero with positive and negative"""
        nums = [5, -5, 10, 20]
        target = 0
        result = self.solution.two_sum(nums, target)
        assert list(result) == [0, 1]

    def test_large_numbers(self):
        """Edge case: very large integers"""
        nums = [10**9, 10**9 + 1, 2, 3]
        target = 2 * 10**9 + 1
        result = self.solution.two_sum(nums, target)
        assert list(result) == [0, 1]

    def test_large_array(self):
        """Edge case: large array (10,000 elements) with pair at end"""
        nums = list(range(1, 10001))  # [1, 2, 3, ..., 10000]
        target = 19999  # 9999 + 10000
        result = self.solution.two_sum(nums, target)
        assert list(result) == [9998, 9999]

    def test_duplicate_values(self):
        """Edge case: array with duplicate values"""
        nums = [3, 3, 4, 5]
        target = 6
        result = self.solution.two_sum(nums, target)
        assert list(result) == [0, 1]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
