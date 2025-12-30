# Scenario 3: Documentation Generation

## Overview

This scenario demonstrates the AI agent's ability to generate comprehensive
documentation from code, including docstrings, type hints, and README files.

## Target File

`src/analytics_toolkit/data/transformers.py`

This file contains a data transformation pipeline implementation that is:
- Technically complex (generics, protocols, composition)
- Poorly documented (minimal docstrings)
- Missing some type hints

## Demo Script

### Step 1: Analyze Current State
```
Analyze src/analytics_toolkit/data/transformers.py and list:
1. Classes and functions without docstrings
2. Missing or incomplete type hints
3. Complex logic that needs explanation
```

### Step 2: Generate Docstrings
```
Add comprehensive Google-style docstrings to all classes and methods in
transformers.py. Include:
- One-line summary
- Detailed description where needed
- Args with types and descriptions
- Returns description
- Raises if applicable
- Usage examples for main classes
```

### Step 3: Improve Type Hints
```
Review and improve all type hints in transformers.py:
- Add missing type hints
- Use modern Python 3.11+ syntax (list[str] not List[str])
- Ensure generic types are properly bounded
- Add TypeVar constraints where appropriate
```

### Step 4: Generate Module Documentation
```
Create a comprehensive README for the data module that explains:
1. The pipeline architecture and design patterns used
2. Available transform classes and their purposes
3. How to compose transforms using | operator
4. Code examples for common use cases
5. Performance considerations
```

## Expected Output Quality

### Good Docstrings
```python
class Pipeline(Generic[T, U]):
    """A composable data transformation pipeline.

    Pipeline allows chaining multiple transforms together using the pipe
    operator (|) or the add() method. Transforms are applied sequentially
    to input data.

    Type Parameters:
        T: Input type for the pipeline.
        U: Output type after all transforms are applied.

    Example:
        >>> pipeline = Pipeline()
        >>> pipeline.add(lambda x: x * 2).add(lambda x: x + 1)
        >>> pipeline([1, 2, 3])
        [3, 5, 7]

        >>> # Using pipe operator
        >>> double = Pipeline([lambda x: [i * 2 for i in x]])
        >>> add_one = Pipeline([lambda x: [i + 1 for i in x]])
        >>> combined = double | add_one
        >>> combined([1, 2, 3])
        [3, 5, 7]

    Attributes:
        _transforms: Internal list of transform functions.
    """
```

### Good Type Hints
```python
# Before
def __init__(self, transforms=None):
    self._transforms = transforms or []

# After
def __init__(self, transforms: list[Callable[[Any], Any]] | None = None) -> None:
    self._transforms: list[Callable[[Any], Any]] = transforms or []
```

## Documentation Types to Generate

1. **Inline Docstrings**
   - Module-level overview
   - Class docstrings with examples
   - Method docstrings with full signatures

2. **External Documentation**
   - README.md for the module
   - API reference
   - Usage guide with examples

3. **Code Comments**
   - Complex algorithm explanations
   - Design decision rationale
   - Performance notes

## Quality Checklist

- [ ] All public classes have docstrings
- [ ] All public methods have docstrings
- [ ] Type hints are complete and correct
- [ ] Examples are runnable
- [ ] Edge cases are documented
- [ ] Related classes are cross-referenced

## Key Takeaway

AI agents are excellent at generating documentation because they can:
- Understand code semantics
- Explain complex patterns clearly
- Generate consistent formatting
- Add helpful examples

However, review generated docs for:
- Accuracy of explanations
- Appropriateness of examples
- Domain-specific terminology
