import pytest
import sys
sys.path.insert(0, '..')
from importlib import import_module

# Import the solution
solution_module = import_module('0004_Group_Anagrams')
Solution = solution_module.Solution


def normalize_result(result: list[list[str]]) -> list[tuple[str, ...]]:
    """Normalize result for comparison: sort within groups and sort groups."""
    return sorted(tuple(sorted(group)) for group in result)


class TestGroupAnagrams:
    def setup_method(self):
        self.solution = Solution()

    # ==================== EXAMPLE TESTS ====================

    def test_example_1(self):
        """Example 1 from problem: mixed anagram groups"""
        strs = ["act", "pots", "tops", "cat", "stop", "hat"]
        result = self.solution.group_anagrams(strs)
        expected = [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
        assert normalize_result(result) == normalize_result(expected)

    def test_example_2(self):
        """Example 2 from problem: single string"""
        strs = ["x"]
        result = self.solution.group_anagrams(strs)
        expected = [["x"]]
        assert normalize_result(result) == normalize_result(expected)

    # ==================== SIMPLE TESTS ====================

    def test_all_anagrams(self):
        """All strings are anagrams of each other"""
        strs = ["eat", "tea", "ate"]
        result = self.solution.group_anagrams(strs)
        expected = [["eat", "tea", "ate"]]
        assert normalize_result(result) == normalize_result(expected)

    def test_no_anagrams(self):
        """No strings are anagrams of each other"""
        strs = ["abc", "def", "ghi"]
        result = self.solution.group_anagrams(strs)
        expected = [["abc"], ["def"], ["ghi"]]
        assert normalize_result(result) == normalize_result(expected)

    def test_two_groups(self):
        """Two distinct anagram groups"""
        strs = ["ab", "ba", "cd", "dc"]
        result = self.solution.group_anagrams(strs)
        expected = [["ab", "ba"], ["cd", "dc"]]
        assert normalize_result(result) == normalize_result(expected)

    # ==================== EDGE CASES ====================

    def test_empty_input(self):
        """Edge case: empty input list"""
        strs = []
        result = self.solution.group_anagrams(strs)
        expected = []
        assert normalize_result(result) == normalize_result(expected)

    def test_empty_strings(self):
        """Edge case: list with empty strings (all anagrams of each other)"""
        strs = ["", ""]
        result = self.solution.group_anagrams(strs)
        expected = [["", ""]]
        assert normalize_result(result) == normalize_result(expected)

    def test_single_empty_string(self):
        """Edge case: single empty string"""
        strs = [""]
        result = self.solution.group_anagrams(strs)
        expected = [[""]]
        assert normalize_result(result) == normalize_result(expected)

    def test_single_character_strings(self):
        """Edge case: single character strings"""
        strs = ["a", "b", "a", "c", "b"]
        result = self.solution.group_anagrams(strs)
        expected = [["a", "a"], ["b", "b"], ["c"]]
        assert normalize_result(result) == normalize_result(expected)

    def test_duplicate_strings(self):
        """Edge case: duplicate identical strings"""
        strs = ["abc", "abc", "abc"]
        result = self.solution.group_anagrams(strs)
        expected = [["abc", "abc", "abc"]]
        assert normalize_result(result) == normalize_result(expected)

    def test_different_lengths(self):
        """Strings of different lengths cannot be anagrams"""
        strs = ["a", "ab", "abc"]
        result = self.solution.group_anagrams(strs)
        expected = [["a"], ["ab"], ["abc"]]
        assert normalize_result(result) == normalize_result(expected)

    def test_with_repeated_characters(self):
        """Strings with repeated characters"""
        strs = ["aab", "aba", "baa", "abb", "bab", "bba"]
        result = self.solution.group_anagrams(strs)
        expected = [["aab", "aba", "baa"], ["abb", "bab", "bba"]]
        assert normalize_result(result) == normalize_result(expected)

    def test_larger_input(self):
        """Test with more strings"""
        strs = ["listen", "silent", "enlist", "hello", "world", "olleh"]
        result = self.solution.group_anagrams(strs)
        expected = [["listen", "silent", "enlist"], ["hello", "olleh"], ["world"]]
        assert normalize_result(result) == normalize_result(expected)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
