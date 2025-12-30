# Gemini CLI Demo: AI Coding Agent Capabilities

A demonstration repository showcasing AI coding agent capabilities and limitations using
Gemini CLI. This project includes multiple scenarios to demonstrate various use cases.

## Prerequisites

```bash
# Install dependencies
pip install -e ".[dev]"

# Or with uv
uv pip install -e ".[dev]"
```

## Project Structure

```
gemini_demo/
├── src/analytics_toolkit/
│   ├── data/
│   │   ├── processor.py       # Scenario 1: Hidden bugs
│   │   └── transformers.py    # Scenario 3: Needs documentation
│   ├── models/
│   │   └── statistics.py      # Scenario 2: Iterative fixes
│   ├── api/
│   │   ├── endpoints.py       # Scenario 4: Parallel dev
│   │   ├── middleware.py      # Scenario 4: Parallel dev
│   │   ├── validators.py      # Scenario 4: Parallel dev
│   │   └── serializers.py     # Scenario 4: Parallel dev
│   └── utils/
│       └── domain_specific.py # Scenario 5: Agent limitations
├── tests/
│   └── test_statistics.py     # Failing tests for Scenario 2
├── docs/scenarios/            # Detailed scenario documentation
└── README.md
```

---

## Demo Scenarios

### Scenario 1: Finding Hidden Bugs

**Purpose:** Demonstrate the agent's ability to identify subtle issues that humans might miss.

**File:** `src/analytics_toolkit/data/processor.py`

**Bugs included:**
- SQL injection vulnerability
- Race condition in caching
- Resource leaks (unclosed connections)
- Float comparison issues
- Off-by-one errors
- Mutable default arguments
- Bare except clauses
- Class-level mutable attributes
- Shallow copy issues

**Demo Steps:**

```bash
# Start Gemini CLI in the project directory
gemini

# Then ask:
```

**Prompt to use:**
```
Review the file src/analytics_toolkit/data/processor.py for bugs, security issues,
and code quality problems. List all issues found, explain why each is problematic,
and propose fixes.
```

**Expected agent behavior:**
1. Read the file
2. Identify multiple issues (should find 10+)
3. Explain each issue with code examples
4. Propose fixes for each

**Follow-up prompt:**
```
Fix all the issues you found in processor.py. Make sure to follow Python best
practices including type hints, proper resource management, and thread safety.
```

---

### Scenario 2: Iterative Problem-Solving

**Purpose:** Show how the agent iteratively fixes code based on test feedback.

**Files:**
- `src/analytics_toolkit/models/statistics.py` (buggy implementation)
- `tests/test_statistics.py` (tests that expose bugs)

**Demo Steps:**

```bash
# Start Gemini CLI
gemini
```

**Prompt to use:**
```
Run the tests in tests/test_statistics.py and fix all failing tests.
Keep running tests after each fix until all tests pass.
```

**Expected agent behavior:**
1. Run `pytest tests/test_statistics.py`
2. See multiple failures
3. Analyze first failure, fix it
4. Run tests again
5. Repeat until all pass

**Bugs the agent needs to fix:**
- Incorrect median for even-length lists
- Sample vs population variance calculation
- Missing percentile validation
- Division by zero in normalize
- Missing edge case handling in correlation

This demonstrates the agent's ability to:
- Interpret test output
- Make targeted fixes
- Iterate until success
- Not over-engineer solutions

---

### Scenario 3: Documentation Generation

**Purpose:** Show the agent's ability to generate comprehensive documentation.

**File:** `src/analytics_toolkit/data/transformers.py`

**Demo Steps:**

```bash
gemini
```

**Prompt to use:**
```
Generate comprehensive documentation for src/analytics_toolkit/data/transformers.py:

1. Add a detailed module-level docstring explaining the transformation pipeline architecture
2. Add Google-style docstrings to all classes and methods
3. Improve type hints where they are missing or incomplete
4. Add usage examples in docstrings

Follow Python best practices and ensure documentation is clear for other developers.
```

**Expected output:**
- Module overview explaining the pipeline concept
- Class docstrings explaining purpose and usage
- Method docstrings with Args, Returns, Raises, Examples
- Complete type hints using modern Python syntax

**Alternative prompt for README generation:**
```
Based on the transformers.py module, generate a README.md for the data subpackage
explaining the transformation pipeline, available transforms, and usage examples.
```

---

### Scenario 4: Parallel Development with Sub-Agents

**Purpose:** Demonstrate using sub-agents to develop multiple modules simultaneously.

**Files to implement:**
- `src/analytics_toolkit/api/endpoints.py`
- `src/analytics_toolkit/api/middleware.py`
- `src/analytics_toolkit/api/validators.py`
- `src/analytics_toolkit/api/serializers.py`

**Demo Steps:**

```bash
gemini
```

**Note:** Gemini CLI's sub-agent feature allows spawning multiple agents to work in
parallel. The exact syntax may vary - check Gemini CLI documentation for current usage.

**Prompt to use:**
```
I need to implement four API modules in parallel. Each module has stub classes
with requirements in the docstrings:

1. endpoints.py - HTTP endpoint handlers and router
2. middleware.py - Request/response middleware (logging, auth, rate limiting, CORS)
3. validators.py - Request validation framework
4. serializers.py - Model serialization/deserialization

These modules are independent and can be developed in parallel. Use sub-agents
to implement all four simultaneously. Each implementation should:
- Follow the interfaces defined in the stub files
- Include complete type hints
- Include docstrings
- Handle edge cases properly
```

**Expected behavior:**
1. Agent spawns sub-agents for parallel work
2. Each sub-agent implements one module
3. Results are collected and integrated
4. Agent verifies implementations work together

**If sub-agents aren't available, alternative prompt:**
```
Implement the endpoints.py module first, then middleware.py, then validators.py,
then serializers.py. After each, briefly verify it follows the interface before
moving to the next.
```

---

### Scenario 5: Understanding Agent Limitations

**Purpose:** Demonstrate tasks where AI agents struggle and human guidance is needed.

**File:** `src/analytics_toolkit/utils/domain_specific.py`

**Demo Steps:**

```bash
gemini
```

**Prompt to use:**
```
Look at src/analytics_toolkit/utils/domain_specific.py and implement the
calculate_customer_discount function.
```

**Expected behavior:**
- Agent will ask clarifying questions about business rules
- Or make assumptions and generate generic logic
- The result won't match your actual business needs

**Discussion points:**

1. **Business Logic:** Agent doesn't know your company's rules
2. **External Systems:** Agent can't access your internal APIs
3. **Subjective Decisions:** Agent makes arbitrary choices
4. **Specialized Domains:** Agent lacks industry expertise
5. **Ambiguous Requirements:** Agent fills gaps with assumptions

**Prompt to demonstrate the issue:**
```
Without asking me any questions, implement all the functions in domain_specific.py.
Make reasonable assumptions where needed.
```

Then review the output and discuss:
- What assumptions did it make?
- Are they correct for your business?
- What's missing or wrong?

---

## Additional Demo Ideas

### Code Refactoring

```
Refactor src/analytics_toolkit/data/processor.py to follow SOLID principles.
Identify violations first, then systematically address each.
```

### Test Generation

```
Generate comprehensive tests for src/analytics_toolkit/data/transformers.py.
Include unit tests for each transform class and integration tests for pipelines.
Aim for high coverage of edge cases.
```

### Code Review

```
Perform a code review of this entire repository. Identify:
1. Code quality issues
2. Potential bugs
3. Security concerns
4. Performance improvements
5. Documentation gaps

Prioritize findings by severity.
```

### Migration Tasks

```
Analyze this codebase and create a plan to migrate from dataclasses to Pydantic
models. Identify all affected files and the changes needed for each.
```

---

## Best Practices When Using AI Coding Agents

### DO use agents for:
- Finding bugs and security issues
- Writing tests
- Generating documentation
- Refactoring well-defined code
- Implementing standard patterns
- Code review and analysis
- Explaining complex code

### DON'T rely on agents for:
- Business-specific logic (without clear specs)
- Integration with undocumented internal systems
- Subjective design decisions
- Highly specialized domain algorithms
- Security-critical code (without review)
- Ambiguous requirements

### Tips for better results:
1. **Be specific:** Detailed prompts get better results
2. **Provide context:** Share relevant files and constraints
3. **Iterate:** Let the agent refine based on feedback
4. **Review critically:** Always review generated code
5. **Test thoroughly:** Don't assume generated code is correct
6. **Document business rules:** Agents can implement rules you specify

---

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/analytics_toolkit

# Run specific scenario tests
pytest tests/test_statistics.py -v
```

## Linting and Formatting

```bash
# Format code
ruff format .

# Check for issues
ruff check .

# Fix auto-fixable issues
ruff check --fix .

# Type checking
mypy src/
```

---

## Troubleshooting

**Tests fail with import errors:**
```bash
pip install -e .
```

**Gemini CLI not found:**
Follow Gemini CLI installation instructions from official documentation.

**Sub-agents not working:**
Check Gemini CLI version and documentation for sub-agent feature availability.
