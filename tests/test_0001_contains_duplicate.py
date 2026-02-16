import pytest
import sys
sys.path.insert(0, '..')
from importlib import import_module

# Import the solution
solution_module = import_module('0001_Contains_Duplicate')
Solution = solution_module.Solution


class TestContainsDuplicate:
    def setup_method(self):
        self.solution = Solution()

    # ==================== SIMPLE TESTS ====================

    def test_simple_with_duplicate(self):
        """Simple case: array with one duplicate"""
        nums = [1, 2, 3, 1]
        assert self.solution.contains_duplicate(nums) is True

    def test_simple_no_duplicate(self):
        """Simple case: array with no duplicates"""
        nums = [1, 2, 3, 4]
        assert self.solution.contains_duplicate(nums) is False

    # ==================== EDGE CASES ====================

    def test_empty_array(self):
        """Edge case: empty array should return False"""
        nums = []
        assert self.solution.contains_duplicate(nums) is False

    def test_single_element(self):
        """Edge case: single element cannot have duplicates"""
        nums = [1]
        assert self.solution.contains_duplicate(nums) is False

    def test_two_identical_elements(self):
        """Edge case: two identical elements"""
        nums = [5, 5]
        assert self.solution.contains_duplicate(nums) is True

    def test_two_different_elements(self):
        """Edge case: two different elements"""
        nums = [5, 6]
        assert self.solution.contains_duplicate(nums) is False

    def test_large_array_no_duplicates(self):
        """Edge case: large array with no duplicates (10,000 elements)"""
        nums = list(range(10000))
        assert self.solution.contains_duplicate(nums) is False

    def test_large_array_with_duplicate_at_end(self):
        """Edge case: large array with duplicate only at the very end"""
        nums = list(range(10000)) + [0]  # 0 appears at start and end
        assert self.solution.contains_duplicate(nums) is True

    def test_negative_numbers(self):
        """Edge case: array with negative numbers and duplicates"""
        nums = [-1, -2, -3, -1, -4]
        assert self.solution.contains_duplicate(nums) is True

    def test_large_numbers(self):
        """Edge case: array with very large integers"""
        nums = [10**9, 10**9 + 1, 10**9 + 2, 10**9]
        assert self.solution.contains_duplicate(nums) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
