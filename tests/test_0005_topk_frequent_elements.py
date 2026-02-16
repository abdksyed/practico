import pytest
import sys
sys.path.insert(0, '..')
from importlib import import_module

# Import the solution
solution_module = import_module('0005_TopK_Frequent_Elements')
Solution = solution_module.Solution


class TestTopKFrequentElements:
    def setup_method(self):
        self.solution = Solution()

    # ==================== SIMPLE TESTS ====================

    def test_example_1(self):
        """Example 1 from problem: [1,2,2,3,3,3], k=2 -> [2,3]"""
        nums = [1, 2, 2, 3, 3, 3]
        k = 2
        result = self.solution.topK_frequent(nums, k)
        assert sorted(result) == sorted([2, 3])

    def test_example_2(self):
        """Example 2 from problem: [7,7], k=1 -> [7]"""
        nums = [7, 7]
        k = 1
        result = self.solution.topK_frequent(nums, k)
        assert result == [7]

    # ==================== EDGE CASES ====================

    def test_single_element(self):
        """Edge case: array with single element, k=1"""
        nums = [42]
        k = 1
        result = self.solution.topK_frequent(nums, k)
        assert result == [42]

    def test_all_same_element(self):
        """Edge case: all elements are identical"""
        nums = [5, 5, 5, 5, 5]
        k = 1
        result = self.solution.topK_frequent(nums, k)
        assert result == [5]

    def test_k_equals_unique_count(self):
        """Edge case: k equals number of unique elements (return all)"""
        nums = [1, 1, 2, 2, 3, 3]
        k = 3
        result = self.solution.topK_frequent(nums, k)
        assert sorted(result) == sorted([1, 2, 3])

    def test_negative_numbers(self):
        """Edge case: array contains negative numbers"""
        nums = [-1, -1, -1, -2, -2, -3]
        k = 2
        result = self.solution.topK_frequent(nums, k)
        assert sorted(result) == sorted([-1, -2])

    def test_mixed_positive_negative(self):
        """Edge case: mix of positive and negative numbers"""
        nums = [-5, -5, -5, 0, 0, 3, 3, 3, 3]
        k = 2
        result = self.solution.topK_frequent(nums, k)
        assert sorted(result) == sorted([3, -5])

    def test_zero_frequency(self):
        """Edge case: zero is the most frequent element"""
        nums = [0, 0, 0, 1, 2]
        k = 1
        result = self.solution.topK_frequent(nums, k)
        assert result == [0]

    def test_large_k_with_varied_frequencies(self):
        """Edge case: larger k with clearly different frequencies"""
        nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        k = 3
        result = self.solution.topK_frequent(nums, k)
        assert sorted(result) == sorted([1, 2, 3])

    def test_large_numbers(self):
        """Edge case: array contains large integer values"""
        nums = [1000000, 1000000, 999999, 999999, 999999]
        k = 1
        result = self.solution.topK_frequent(nums, k)
        assert result == [999999]

    def test_single_occurrence_each(self):
        """Edge case: each element appears exactly once"""
        nums = [1, 2, 3, 4, 5]
        k = 3
        result = self.solution.topK_frequent(nums, k)
        # Any 3 elements are valid since all have same frequency
        assert len(result) == 3
        assert all(elem in nums for elem in result)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
