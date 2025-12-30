# Scenario 2: Iterative Problem-Solving

## Overview

This scenario demonstrates how AI agents can iteratively fix code based on test
feedback, similar to test-driven development (TDD) workflow.

## Target Files

- `src/analytics_toolkit/models/statistics.py` - Implementation with bugs
- `tests/test_statistics.py` - Tests that expose the bugs

## Bugs to Fix

### Bug 1: Median for Even-Length Lists
```python
# Buggy
if n % 2 == 0:
    return sorted_values[mid]  # Wrong: returns only one value

# Fixed
if n % 2 == 0:
    return (sorted_values[mid - 1] + sorted_values[mid]) / 2
```

### Bug 2: Sample vs Population Variance
```python
# Buggy - always uses population formula
return squared_diff_sum / len(values)

# Fixed
divisor = len(values) if population else len(values) - 1
return squared_diff_sum / divisor
```

### Bug 3: Percentile Validation
```python
# Missing validation
# Fixed
if not 0 <= percentile <= 100:
    raise ValueError(f"Percentile must be 0-100, got {percentile}")
```

### Bug 4: Division by Zero in Normalize
```python
# Buggy
range_val = max_val - min_val
return [(v - min_val) / range_val for v in values]  # Crashes if all same

# Fixed
if range_val == 0:
    return [0.0] * len(values)
```

### Bug 5: Correlation Edge Cases
```python
# Missing handling for:
# - Single value lists
# - Constant values (zero std dev)
```

## Demo Script

### Step 1: Run Tests
```
Run pytest tests/test_statistics.py -v and show me the results.
```

Expected: Multiple test failures.

### Step 2: Begin Fixing
```
Fix the failing tests one at a time. After each fix, run the tests again to
verify the fix works before moving to the next issue.
```

Expected: Agent enters an iteration loop:
1. Identify failure
2. Analyze cause
3. Implement fix
4. Run tests
5. Repeat

### Step 3: Verify Completion
```
Run the full test suite and confirm all tests pass.
Then run ruff check and mypy to ensure code quality.
```

## What to Observe

### Good Agent Behavior
- Reads test output carefully
- Makes minimal, targeted fixes
- Doesn't change unrelated code
- Tests after each change
- Explains reasoning for fixes

### Potential Issues
- Over-engineering solutions
- Breaking other tests while fixing one
- Not understanding the test expectation
- Making assumptions without checking

## Iteration Pattern

```
┌──────────────────┐
│   Run Tests      │
└────────┬─────────┘
         │
         ▼
    ┌────────┐     Yes
    │ Pass?  │──────────► Done
    └────┬───┘
         │ No
         ▼
┌──────────────────┐
│ Analyze Failure  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│  Implement Fix   │
└────────┬─────────┘
         │
         └────────────┐
                      │
         ┌────────────┘
         ▼
┌──────────────────┐
│   Run Tests      │ (repeat)
└──────────────────┘
```

## Key Takeaway

AI agents can effectively work in a test-driven manner, using test feedback to
guide their fixes. This is often more reliable than asking them to fix code
without concrete success criteria.

**Best practice:** Always have tests when asking an agent to fix code.
