# Scenario 1: Finding Hidden Bugs

## Overview

This scenario demonstrates the AI agent's ability to identify subtle bugs, security
vulnerabilities, and code quality issues that might be missed during code review.

## Target File

`src/analytics_toolkit/data/processor.py`

## Bugs Included

### 1. SQL Injection Vulnerability
```python
# Vulnerable code
query = f"SELECT * FROM users WHERE username = '{username}'"

# Should be
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
```

### 2. Race Condition
```python
# Check-then-act pattern without proper locking
if key in self._cache:
    return self._cache[key]
with self._lock:
    # Missing double-check!
    result = compute_fn()
```

### 3. Resource Leak
```python
conn = sqlite3.connect(db_path)
# Connection never closed - use context manager
```

### 4. Division by Zero
```python
def calculate_percentage_change(old_value: float, new_value: float) -> float:
    return ((new_value - old_value) / old_value) * 100  # Crashes when old_value=0
```

### 5. Float Comparison
```python
def is_equal(a: float, b: float) -> bool:
    return a == b  # Should use tolerance: abs(a - b) < epsilon
```

### 6. Off-by-One Error
```python
for i in range(0, len(items) - 1, batch_size):  # Should be len(items)
```

### 7. Mutable Default Argument
```python
def aggregate_metrics(data, default_metrics={}):  # Bug: shared across calls
```

### 8. Bare Except Clause
```python
except:  # Catches KeyboardInterrupt, SystemExit, etc.
    return 0.0
```

### 9. Assert for Validation
```python
assert len(columns) == expected_columns  # Stripped in optimized mode
```

### 10. Class-Level Mutable Attribute
```python
class MetricsCollector:
    collected_metrics = []  # Shared across all instances!
```

### 11. Shallow Copy Issue
```python
result = base.copy()  # Nested dicts are still shared references
```

## Demo Script

### Step 1: Initial Review
```
Review src/analytics_toolkit/data/processor.py for bugs and security issues.
Categorize findings by severity (Critical, High, Medium, Low).
```

Expected: Agent should find most or all issues.

### Step 2: Request Fixes
```
Fix all the issues you identified. For each fix, explain briefly what was wrong
and why your fix addresses it.
```

Expected: Agent systematically fixes each issue.

### Step 3: Verify Fixes
```
Review your changes to ensure:
1. All original issues are fixed
2. No new issues were introduced
3. Code follows Python best practices
4. Type hints are complete
```

## Discussion Points

- Did the agent find all bugs?
- Were any false positives reported?
- Are the fixes idiomatic Python?
- Did it maintain the original functionality?
- Would you have caught all these in code review?

## Key Takeaway

AI agents excel at systematic code analysis and can catch issues that humans
might miss due to fatigue or familiarity blindness. However, always verify
the fixes are appropriate for your specific context.
