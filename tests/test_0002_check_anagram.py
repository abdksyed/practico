import pytest
import sys
sys.path.insert(0, '..')
from importlib import import_module

# Import the solution
solution_module = import_module('0002_Check_Anagram')
Solution = solution_module.Solution


class TestCheckAnagram:
    def setup_method(self):
        self.solution = Solution()

    # ==================== SIMPLE TESTS ====================

    def test_simple_anagram(self):
        """Simple case: valid anagram"""
        s = "racecar"
        t = "carrace"
        assert self.solution.check_anagram(s, t) is True

    def test_simple_not_anagram(self):
        """Simple case: not an anagram (different characters)"""
        s = "jar"
        t = "jam"
        assert self.solution.check_anagram(s, t) is False

    # ==================== EDGE CASES ====================

    def test_empty_strings(self):
        """Edge case: two empty strings are anagrams"""
        s = ""
        t = ""
        assert self.solution.check_anagram(s, t) is True

    def test_single_character_same(self):
        """Edge case: single identical characters"""
        s = "a"
        t = "a"
        assert self.solution.check_anagram(s, t) is True

    def test_single_character_different(self):
        """Edge case: single different characters"""
        s = "a"
        t = "b"
        assert self.solution.check_anagram(s, t) is False

    def test_different_lengths(self):
        """Edge case: strings of different lengths cannot be anagrams"""
        s = "abc"
        t = "abcd"
        assert self.solution.check_anagram(s, t) is False

    def test_same_characters_different_counts(self):
        """Edge case: same chars but different frequencies"""
        s = "aab"
        t = "abb"
        assert self.solution.check_anagram(s, t) is False

    def test_large_strings_anagram(self):
        """Edge case: large strings (10,000 chars) that are anagrams"""
        s = "abc" * 3333 + "a"  # 10,000 chars
        t = "bca" * 3333 + "a"  # same chars, different order
        assert self.solution.check_anagram(s, t) is True

    def test_large_strings_not_anagram(self):
        """Edge case: large strings (10,000 chars) that are not anagrams"""
        s = "a" * 10000
        t = "a" * 9999 + "b"
        assert self.solution.check_anagram(s, t) is False

    def test_with_repeated_characters(self):
        """Edge case: strings with many repeated characters"""
        s = "aaabbbccc"
        t = "abcabcabc"
        assert self.solution.check_anagram(s, t) is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
