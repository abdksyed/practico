import pytest
import sys
sys.path.insert(0, '..')
from importlib import import_module

# Import the solution
solution_module = import_module('0006_Encode_Decode_Strings')
Solution = solution_module.Solution


class TestEncodeDecodeStrings:
    def setup_method(self):
        self.solution = Solution()

    def encode_decode(self, strs: list[str]) -> list[str]:
        """Helper to encode then decode a list of strings."""
        encoded = self.solution.encode(strs)
        return self.solution.decode(encoded)

    # ==================== BASIC TESTS ====================

    def test_example_1(self):
        """Example 1 from problem: ["Hello", "World"]"""
        strs = ["Hello", "World"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_example_2(self):
        """Example 2 from problem: [""]"""
        strs = [""]
        result = self.encode_decode(strs)
        assert result == strs

    def test_simple_words(self):
        """Basic test with simple words."""
        strs = ["apple", "banana", "cherry"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_single_string(self):
        """Single non-empty string."""
        strs = ["hello"]
        result = self.encode_decode(strs)
        assert result == strs

    # ==================== EMPTY AND BLANK EDGE CASES ====================

    def test_empty_list(self):
        """Edge case: empty list []"""
        strs = []
        result = self.encode_decode(strs)
        assert result == strs

    def test_single_empty_string(self):
        """Edge case: list with single empty string [""]"""
        strs = [""]
        result = self.encode_decode(strs)
        assert result == strs

    def test_multiple_empty_strings(self):
        """Edge case: list with multiple empty strings ["", "", ""]"""
        strs = ["", "", ""]
        result = self.encode_decode(strs)
        assert result == strs

    def test_empty_strings_mixed_with_content(self):
        """Edge case: empty strings mixed with non-empty strings."""
        strs = ["hello", "", "world", "", ""]
        result = self.encode_decode(strs)
        assert result == strs

    def test_empty_string_at_start(self):
        """Edge case: empty string at the start."""
        strs = ["", "hello", "world"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_empty_string_at_end(self):
        """Edge case: empty string at the end."""
        strs = ["hello", "world", ""]
        result = self.encode_decode(strs)
        assert result == strs

    # ==================== DELIMITER CHARACTER EDGE CASES ====================

    def test_string_with_single_pipe(self):
        """Edge case: string containing single pipe character."""
        strs = ["hello|world"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_string_with_multiple_pipes(self):
        """Edge case: string containing multiple pipe characters ["|||"]"""
        strs = ["|||"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_string_only_pipes(self):
        """Edge case: strings that are only pipe characters."""
        strs = ["|", "||", "|||", "||||"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_pipes_at_boundaries(self):
        """Edge case: pipes at start and end of strings."""
        strs = ["|hello", "world|", "|both|"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_complex_mixed_with_pipes(self):
        """Edge case: complex mix with pipes, numbers, empty strings."""
        strs = ["asd", "fdgdfg", "123123|123", "", "asd", "|||"]
        result = self.encode_decode(strs)
        assert result == strs

    # ==================== NUMERIC STRING EDGE CASES ====================

    def test_numeric_strings(self):
        """Edge case: strings that are numeric."""
        strs = ["123", "456", "0", "999999"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_strings_looking_like_encoding(self):
        """Edge case: strings that look like the encoding format itself (e.g., '5|hello')."""
        strs = ["5|hello", "3|abc", "0|"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_strings_with_only_numbers_and_pipes(self):
        """Edge case: strings with numbers and pipes mixed."""
        strs = ["1|2|3", "|||123", "123|||"]
        result = self.encode_decode(strs)
        assert result == strs

    # ==================== SPECIAL CHARACTER EDGE CASES ====================

    def test_strings_with_newlines(self):
        """Edge case: strings containing newline characters."""
        strs = ["hello\nworld", "line1\nline2\nline3"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_strings_with_tabs(self):
        """Edge case: strings containing tab characters."""
        strs = ["hello\tworld", "col1\tcol2\tcol3"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_strings_with_spaces(self):
        """Edge case: strings containing spaces."""
        strs = ["hello world", "  ", " leading", "trailing "]
        result = self.encode_decode(strs)
        assert result == strs

    def test_strings_with_special_chars(self):
        """Edge case: strings with various special characters."""
        strs = ["!@#$%^&*()", "<>?:\"{}[]", "\\/'`~"]
        result = self.encode_decode(strs)
        assert result == strs

    # ==================== UNICODE EDGE CASES ====================

    def test_unicode_strings(self):
        """Edge case: strings with unicode characters."""
        strs = ["你好", "مرحبا", "привет", "🎉🚀"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_mixed_ascii_unicode(self):
        """Edge case: mix of ASCII and unicode."""
        strs = ["hello世界", "café", "naïve", "résumé"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_emoji_strings(self):
        """Edge case: strings with emojis."""
        strs = ["😀😃😄", "👨‍👩‍👧‍👦", "🏳️‍🌈"]
        result = self.encode_decode(strs)
        assert result == strs

    # ==================== LENGTH EDGE CASES ====================

    def test_very_long_string(self):
        """Edge case: very long string."""
        long_str = "a" * 10000
        strs = [long_str]
        result = self.encode_decode(strs)
        assert result == strs

    def test_many_short_strings(self):
        """Edge case: many short strings."""
        strs = ["a"] * 1000
        result = self.encode_decode(strs)
        assert result == strs

    def test_varied_length_strings(self):
        """Edge case: strings of highly varied lengths."""
        strs = ["a", "ab" * 50, "abc" * 100, "", "x" * 500]
        result = self.encode_decode(strs)
        assert result == strs

    def test_single_character_strings(self):
        """Edge case: all single character strings."""
        strs = ["a", "b", "c", "d", "e"]
        result = self.encode_decode(strs)
        assert result == strs

    # ==================== DUPLICATE EDGE CASES ====================

    def test_duplicate_strings(self):
        """Edge case: list contains duplicate strings."""
        strs = ["hello", "hello", "hello"]
        result = self.encode_decode(strs)
        assert result == strs

    def test_duplicate_empty_and_non_empty(self):
        """Edge case: duplicates of both empty and non-empty strings."""
        strs = ["", "asd", "", "asd", ""]
        result = self.encode_decode(strs)
        assert result == strs

    # ==================== ENCODING SPECIFIC TESTS ====================

    def test_encode_format(self):
        """Verify the encoding format is correct (length|string)."""
        strs = ["hi", "bye"]
        encoded = self.solution.encode(strs)
        assert encoded == "2|hi3|bye"

    def test_encode_empty_string_format(self):
        """Verify encoding of empty string."""
        strs = [""]
        encoded = self.solution.encode(strs)
        assert encoded == "0|"

    def test_encode_empty_list_format(self):
        """Verify encoding of empty list."""
        strs = []
        encoded = self.solution.encode(strs)
        assert encoded == ""

    def test_encode_string_with_pipe_format(self):
        """Verify encoding handles pipe character correctly."""
        strs = ["a|b"]
        encoded = self.solution.encode(strs)
        assert encoded == "3|a|b"

    # ==================== STRESS TEST ====================

    def test_stress_large_input(self):
        """Stress test: large number of varied strings."""
        strs = [
            "normal",
            "",
            "with|pipe",
            "|||",
            "12345",
            "5|fake",
            "hello\nworld",
            "  spaces  ",
            "🎉",
            "a" * 100,
        ] * 100
        result = self.encode_decode(strs)
        assert result == strs


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
