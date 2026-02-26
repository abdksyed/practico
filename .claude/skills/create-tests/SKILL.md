---
name: create-tests
description: Create comprehensive test cases with all possible edge cases for a problem/solution file
allowed-tools: Read, Write, Glob, Grep, Bash
argument-hint: [problem-file-or-name]
---

# Create Comprehensive Tests

Create detailed test cases for the specified problem: $ARGUMENTS

## Process

1. **Read the solution file** - Understand the implementation, function signature, and expected behavior
2. **Analyze the problem** - Identify all possible edge cases based on:
   - Input boundaries (empty, single element, minimum/maximum values)
   - Special values (zeros, negatives, duplicates)
   - Data structure specific cases (for arrays: sorted, reverse sorted, all same)
   - Problem-specific edge cases
   - Invalid inputs that should be handled
   - Stress tests with larger inputs

3. **Create the test file** in the `tests/` folder following the existing naming convention:
   - File name: `test_XXXX_problem_name.py` matching the solution file
   - Use pytest with descriptive test names
   - Group tests by category with clear section comments
   - Each test should have a docstring explaining what it tests

4. **Test categories to cover** (adapt based on problem type):
   - Basic examples from the problem description
   - Empty/minimal inputs
   - Single element cases
   - Boundary values
   - Negative numbers (if applicable)
   - Zeros (if applicable)
   - Duplicates
   - Large numbers
   - Same elements
   - Sorted/reverse sorted (if order matters)
   - Special patterns
   - Multiple valid outputs (if applicable)
   - Invalid inputs (if applicable)

5. **Run the tests** using:
   ```bash
   source /Users/syedal/oss/practico/.venv/bin/activate && python -m pytest tests/test_XXXX_*.py -v
   ```

## Test File Structure

Follow this structure for consistency:

```python
import pytest
import sys
sys.path.insert(0, '..')
from importlib import import_module

# Import the solution
solution_module = import_module('XXXX_Problem_Name')
Solution = solution_module.Solution


class TestProblemName:
    def setup_method(self):
        self.solution = Solution()

    # ==================== BASIC TESTS (FROM EXAMPLES) ====================

    def test_example_1(self):
        """Description from problem."""
        pass

    # ==================== EDGE CASE CATEGORY ====================

    def test_edge_case(self):
        """What this tests."""
        pass


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

## Important

- Do NOT miss any edge case
- Every test must have a clear docstring
- Use descriptive test method names
- Group related tests with section comments
- Verify all tests pass before completing
