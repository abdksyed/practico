import pytest
import sys
sys.path.insert(0, '..')
from importlib import import_module

# Import the solution
solution_module = import_module('0007_Product_Array_Except_Itself')
Solution = solution_module.Solution


class TestProductExceptSelf:
    def setup_method(self):
        self.solution = Solution()

    # ==================== BASIC TESTS (FROM EXAMPLES) ====================

    def test_example_1(self):
        """Example 1 from problem: [1,2,4,6] -> [48,24,12,8]"""
        nums = [1, 2, 4, 6]
        result = self.solution.product_except_self(nums)
        assert result == [48, 24, 12, 8]

    def test_example_2(self):
        """Example 2 from problem: [-1,0,1,2,3] -> [0,-6,0,0,0]"""
        nums = [-1, 0, 1, 2, 3]
        result = self.solution.product_except_self(nums)
        assert result == [0, -6, 0, 0, 0]

    def test_simple_array(self):
        """Simple array with small positive numbers."""
        nums = [1, 2, 3, 4]
        result = self.solution.product_except_self(nums)
        assert result == [24, 12, 8, 6]

    def test_two_elements(self):
        """Array with exactly two elements."""
        nums = [3, 5]
        result = self.solution.product_except_self(nums)
        assert result == [5, 3]

    # ==================== ZERO EDGE CASES ====================

    def test_single_zero(self):
        """Array with exactly one zero."""
        nums = [1, 2, 0, 4]
        result = self.solution.product_except_self(nums)
        assert result == [0, 0, 8, 0]

    def test_single_zero_at_start(self):
        """Zero at the start of array."""
        nums = [0, 2, 3, 4]
        result = self.solution.product_except_self(nums)
        assert result == [24, 0, 0, 0]

    def test_single_zero_at_end(self):
        """Zero at the end of array."""
        nums = [2, 3, 4, 0]
        result = self.solution.product_except_self(nums)
        assert result == [0, 0, 0, 24]

    def test_two_zeros(self):
        """Array with exactly two zeros."""
        nums = [1, 0, 3, 0]
        result = self.solution.product_except_self(nums)
        assert result == [0, 0, 0, 0]

    def test_multiple_zeros(self):
        """Array with more than two zeros."""
        nums = [0, 0, 0, 1]
        result = self.solution.product_except_self(nums)
        assert result == [0, 0, 0, 0]

    def test_all_zeros(self):
        """Array with all zeros."""
        nums = [0, 0, 0, 0]
        result = self.solution.product_except_self(nums)
        assert result == [0, 0, 0, 0]

    def test_zero_with_negatives(self):
        """Zero with negative numbers."""
        nums = [-2, 0, 3, -4]
        result = self.solution.product_except_self(nums)
        assert result == [0, 24, 0, 0]

    # ==================== NEGATIVE NUMBER EDGE CASES ====================

    def test_all_negative(self):
        """Array with all negative numbers."""
        nums = [-1, -2, -3, -4]
        result = self.solution.product_except_self(nums)
        # products: -24, -12, -8, -6
        assert result == [-24, -12, -8, -6]

    def test_mixed_positive_negative(self):
        """Mix of positive and negative numbers."""
        nums = [-1, 2, -3, 4]
        result = self.solution.product_except_self(nums)
        # product of all = 24
        # results: -24, 12, -8, 6
        assert result == [-24, 12, -8, 6]

    def test_single_negative(self):
        """Single negative number in array."""
        nums = [1, -2, 3, 4]
        result = self.solution.product_except_self(nums)
        assert result == [-24, 12, -8, -6]

    def test_two_negatives(self):
        """Two negative numbers (product positive)."""
        nums = [-2, -3, 4, 5]
        result = self.solution.product_except_self(nums)
        # product of all = 120
        assert result == [-60, -40, 30, 24]

    def test_negative_one(self):
        """Array containing -1."""
        nums = [2, -1, 3]
        result = self.solution.product_except_self(nums)
        assert result == [-3, 6, -2]

    # ==================== ONE EDGE CASES ====================

    def test_all_ones(self):
        """Array with all ones."""
        nums = [1, 1, 1, 1]
        result = self.solution.product_except_self(nums)
        assert result == [1, 1, 1, 1]

    def test_contains_one(self):
        """Array containing 1."""
        nums = [2, 1, 3, 4]
        result = self.solution.product_except_self(nums)
        assert result == [12, 24, 8, 6]

    def test_ones_and_negative_ones(self):
        """Mix of 1 and -1."""
        nums = [1, -1, 1, -1]
        result = self.solution.product_except_self(nums)
        assert result == [1, -1, 1, -1]

    # ==================== SINGLE ELEMENT EDGE CASE ====================

    def test_single_element(self):
        """Array with single element."""
        nums = [5]
        result = self.solution.product_except_self(nums)
        # Product of all except self = 1 (empty product)
        assert result == [1]

    def test_single_zero_element(self):
        """Array with single zero element."""
        nums = [0]
        result = self.solution.product_except_self(nums)
        assert result == [1]

    def test_single_negative_element(self):
        """Array with single negative element."""
        nums = [-5]
        result = self.solution.product_except_self(nums)
        assert result == [1]

    # ==================== LARGE NUMBERS EDGE CASES ====================

    def test_large_numbers(self):
        """Array with large numbers."""
        nums = [100, 200, 300]
        result = self.solution.product_except_self(nums)
        assert result == [60000, 30000, 20000]

    def test_large_positive_numbers(self):
        """Array with larger positive numbers."""
        nums = [1000, 2000, 3]
        result = self.solution.product_except_self(nums)
        assert result == [6000, 3000, 2000000]

    def test_mixed_large_and_small(self):
        """Mix of large and small numbers."""
        nums = [1, 1000, 2, 500]
        result = self.solution.product_except_self(nums)
        # total = 1000000
        assert result == [1000000, 1000, 500000, 2000]

    # ==================== SAME NUMBERS EDGE CASES ====================

    def test_all_same_positive(self):
        """Array with all same positive numbers."""
        nums = [2, 2, 2, 2]
        result = self.solution.product_except_self(nums)
        assert result == [8, 8, 8, 8]

    def test_all_same_negative(self):
        """Array with all same negative numbers."""
        nums = [-2, -2, -2, -2]
        result = self.solution.product_except_self(nums)
        assert result == [-8, -8, -8, -8]

    def test_all_twos(self):
        """Array with all 2s."""
        nums = [2, 2, 2]
        result = self.solution.product_except_self(nums)
        assert result == [4, 4, 4]

    # ==================== LONGER ARRAY EDGE CASES ====================

    def test_longer_array(self):
        """Array with more elements."""
        nums = [1, 2, 3, 4, 5, 6]
        result = self.solution.product_except_self(nums)
        # total = 720
        assert result == [720, 360, 240, 180, 144, 120]

    def test_array_with_many_ones(self):
        """Array with many ones and few other numbers."""
        nums = [1, 1, 1, 2, 1, 1, 1]
        result = self.solution.product_except_self(nums)
        assert result == [2, 2, 2, 1, 2, 2, 2]

    # ==================== SPECIAL PATTERNS ====================

    def test_ascending_order(self):
        """Numbers in ascending order."""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.product_except_self(nums)
        assert result == [120, 60, 40, 30, 24]

    def test_descending_order(self):
        """Numbers in descending order."""
        nums = [5, 4, 3, 2, 1]
        result = self.solution.product_except_self(nums)
        assert result == [24, 30, 40, 60, 120]

    def test_alternating_signs(self):
        """Alternating positive and negative numbers."""
        nums = [1, -2, 3, -4, 5]
        result = self.solution.product_except_self(nums)
        # total = 120
        assert result == [120, -60, 40, -30, 24]

    def test_powers_of_two(self):
        """Powers of two."""
        nums = [2, 4, 8, 16]
        result = self.solution.product_except_self(nums)
        # total = 1024
        assert result == [512, 256, 128, 64]

    # ==================== BOUNDARY VALUE TESTS ====================

    def test_min_two_elements_both_positive(self):
        """Minimum size array with positive numbers."""
        nums = [1, 2]
        result = self.solution.product_except_self(nums)
        assert result == [2, 1]

    def test_min_two_elements_both_negative(self):
        """Minimum size array with negative numbers."""
        nums = [-1, -2]
        result = self.solution.product_except_self(nums)
        assert result == [-2, -1]

    def test_min_two_elements_mixed(self):
        """Minimum size array with mixed signs."""
        nums = [-3, 4]
        result = self.solution.product_except_self(nums)
        assert result == [4, -3]

    def test_min_two_elements_with_zero(self):
        """Minimum size array with zero."""
        nums = [0, 5]
        result = self.solution.product_except_self(nums)
        assert result == [5, 0]

    def test_min_two_elements_both_zero(self):
        """Minimum size array with both zeros."""
        nums = [0, 0]
        result = self.solution.product_except_self(nums)
        assert result == [0, 0]

    # ==================== PRODUCT VERIFICATION TESTS ====================

    def test_verify_product_property(self):
        """Verify that result[i] * nums[i] equals total product (for no-zero case)."""
        nums = [2, 3, 4, 5]
        result = self.solution.product_except_self(nums)
        total_product = 2 * 3 * 4 * 5  # 120
        for i in range(len(nums)):
            assert result[i] * nums[i] == total_product

    def test_output_length_matches_input(self):
        """Verify output length matches input length."""
        nums = [1, 2, 3, 4, 5]
        result = self.solution.product_except_self(nums)
        assert len(result) == len(nums)

    # ==================== STRESS TESTS ====================

    def test_medium_array(self):
        """Medium-sized array."""
        nums = list(range(1, 11))  # [1, 2, 3, ..., 10]
        result = self.solution.product_except_self(nums)
        total = 3628800  # 10!
        expected = [total // i for i in nums]
        assert result == expected

    def test_array_with_primes(self):
        """Array with prime numbers."""
        nums = [2, 3, 5, 7, 11]
        result = self.solution.product_except_self(nums)
        total = 2310
        expected = [1155, 770, 462, 330, 210]
        assert result == expected


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
