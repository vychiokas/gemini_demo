# Demo Prompts Reference

Quick reference of prompts to use during the Gemini CLI demo.
Copy and paste these directly into the CLI.

---

## Scenario 1: Finding Hidden Bugs

### Basic Review
```
Review src/analytics_toolkit/data/processor.py for bugs, security issues,
and code quality problems. List all issues found with severity levels.
```

### Detailed Analysis
```
Perform a security audit of src/analytics_toolkit/data/processor.py.
Focus on:
1. Injection vulnerabilities
2. Resource management
3. Thread safety
4. Error handling

Provide OWASP-style categorization for security issues.
```

### Fix All Issues
```
Fix all issues in src/analytics_toolkit/data/processor.py. Follow Python
best practices: complete type hints, context managers for resources,
parameterized queries, and proper exception handling.
```

---

## Scenario 2: Iterative Test Fixing

### Start Iteration
```
Run pytest tests/test_statistics.py -v and fix all failing tests.
After each fix, run the tests again until all pass.
```

### Targeted Fix
```
Run the tests, identify the first failing test, explain what's wrong,
fix it, then run tests again. Continue until all pass.
```

### With Analysis
```
1. Run pytest tests/test_statistics.py -v
2. For each failure, explain:
   - What the test expects
   - What the code does wrong
   - How to fix it
3. Implement fixes one at a time
4. Verify with tests after each fix
```

---

## Scenario 3: Documentation Generation

### Complete Documentation
```
Generate comprehensive documentation for src/analytics_toolkit/data/transformers.py:
1. Module-level docstring explaining the architecture
2. Google-style docstrings for all classes and methods
3. Type hints for all parameters and return values
4. Usage examples in docstrings
```

### Generate README
```
Create a README.md for src/analytics_toolkit/data/ explaining:
1. Purpose of the transformation pipeline
2. Available transform classes
3. How to compose transforms
4. Code examples for common patterns
```

### API Reference
```
Generate an API reference document for the transformers module.
Include all public classes, methods, and their signatures.
```

---

## Scenario 4: Parallel Development

### Full Parallel (if sub-agents available)
```
Using sub-agents, implement these four modules in parallel:

1. src/analytics_toolkit/api/endpoints.py
2. src/analytics_toolkit/api/middleware.py
3. src/analytics_toolkit/api/validators.py
4. src/analytics_toolkit/api/serializers.py

Each implementation should:
- Follow the interface in the stub file
- Include complete type hints
- Include Google-style docstrings
- Handle edge cases
```

### Sequential Alternative
```
Implement the API modules in this order:
1. validators.py
2. serializers.py
3. middleware.py
4. endpoints.py

After each, summarize what was implemented before continuing.
```

### Single Module
```
Implement src/analytics_toolkit/api/validators.py following the interface
defined in the stub. Include complete type hints and docstrings.
```

---

## Scenario 5: Agent Limitations

### Test Assumptions
```
Implement all functions in src/analytics_toolkit/utils/domain_specific.py
without asking any questions. Make reasonable assumptions where needed.
Then list all assumptions you made.
```

### With Context
```
Implement calculate_customer_discount with these business rules:
- Tier "enterprise": 25% base discount
- Tier "professional": 15% base discount
- Tier "starter": 5% base discount
- Accounts over 2 years get additional 5%
- Account balance over $10,000 gets additional 3%
- Maximum total discount is 30%
```

### Demonstrate Limitation
```
Implement sync_with_legacy_erp to sync data with our internal SAP system.
```
(Agent will need to ask for API details or make wrong assumptions)

---

## Bonus Prompts

### Code Refactoring
```
Refactor src/analytics_toolkit/data/processor.py to follow SOLID principles.
First identify violations, then fix them systematically.
```

### Test Generation
```
Generate comprehensive pytest tests for src/analytics_toolkit/data/transformers.py.
Include tests for each transform class and integration tests for pipelines.
```

### Full Code Review
```
Perform a code review of the entire src/analytics_toolkit/ directory.
Categorize findings as: Critical, High, Medium, Low.
Focus on bugs, security, performance, and maintainability.
```

### Explain Complex Code
```
Explain how the Pipeline class in transformers.py works.
Include how the | operator enables composition.
```

### Performance Analysis
```
Analyze src/analytics_toolkit/data/processor.py for potential performance
issues. Suggest optimizations with explanations.
```
