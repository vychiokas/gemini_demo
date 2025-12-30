# Scenario 4: Large Task Decomposition

## Overview

This scenario demonstrates how agents break down and tackle larger tasks that
span multiple files. It shows task planning, dependency ordering, and maintaining
consistency across related code.

## Target Files

Four API modules with stub implementations:

1. `src/analytics_toolkit/api/validators.py` - Request validation
2. `src/analytics_toolkit/api/serializers.py` - Model serialization
3. `src/analytics_toolkit/api/middleware.py` - Request/response middleware
4. `src/analytics_toolkit/api/endpoints.py` - HTTP endpoint handlers

## Demo Steps

### Step 1: Start Gemini CLI

```bash
cd /path/to/gemini_demo
gemini
```

### Step 2: Give the Implementation Task

**Prompt:**
```
Implement all four API modules in src/analytics_toolkit/api/:

1. validators.py - Request validation framework with Validator base class
2. serializers.py - Model serialization with MetricSerializer, UserSerializer
3. middleware.py - Logging, Auth, RateLimit, CORS middleware
4. endpoints.py - HealthCheck, Metrics, Query endpoints and Router

Each stub file contains the interface and requirements in docstrings.
Implement them all, following Python best practices with complete type hints
and Google-style docstrings.
```

### Step 3: Watch the Agent Work

**Expected behavior:**
1. Agent reads each stub file to understand requirements
2. Implements validators.py first (no dependencies)
3. Implements serializers.py (no dependencies)
4. Implements middleware.py (depends on endpoints types)
5. Implements endpoints.py (may use validators/serializers)
6. May run basic verification

### Step 4: Verify Integration

**Follow-up prompt:**
```
Verify all four modules work together:
1. Import all modules
2. Create a test that sends a request through middleware to an endpoint
3. Fix any integration issues
```

---

## Module Specifications

### validators.py
```python
class Validator:
    def required(self, field: str) -> "Validator": ...
    def string(self, field: str, min_length, max_length) -> "Validator": ...
    def integer(self, field: str, min_val, max_val) -> "Validator": ...
    def email(self, field: str) -> "Validator": ...
    def validate(self, data: dict) -> ValidationResult: ...

class MetricsValidator(Validator): ...
class QueryParamsValidator(Validator): ...
```

### serializers.py
```python
class Serializer(Generic[T]):
    def serialize(self, obj: T, fields: list[str] | None = None) -> dict: ...
    def deserialize(self, data: dict) -> T: ...

class MetricSerializer(Serializer[Metric]): ...
class UserSerializer(Serializer[User]): ...  # Must exclude api_key!
class PaginatedResponse: ...
```

### middleware.py
```python
class LoggingMiddleware: ...
class AuthenticationMiddleware: ...
class RateLimitMiddleware: ...
class CORSMiddleware: ...
class MiddlewareChain: ...
```

### endpoints.py
```python
class HealthCheckEndpoint:
    def handle(self, request: Request) -> Response: ...

class MetricsEndpoint:
    def handle(self, request: Request) -> Response: ...

class QueryEndpoint:
    def handle(self, request: Request) -> Response: ...

class Router:
    def register(self, method: str, path: str, handler) -> None: ...
    def route(self, request: Request) -> Response: ...
```

---

## What This Demonstrates

1. **Task decomposition:** Agent breaks large task into logical sub-tasks
2. **Dependency ordering:** Agent figures out which modules to implement first
3. **Context management:** Agent keeps track of interfaces across files
4. **Consistency:** Agent maintains consistent patterns across modules
5. **Integration thinking:** Agent considers how modules work together

---

## Alternative: Step-by-Step with Checkpoints

If you want more control, implement one at a time:

```
Implement src/analytics_toolkit/api/validators.py following the stub interface.
```

Then after completion:
```
Now implement serializers.py.
```

And so on. This gives you checkpoints to review each module.

---

## Key Takeaways

- Agents can decompose large tasks into logical steps
- Clear specifications (stub files) help guide implementation
- Agent determines dependency order automatically
- Integration verification is essential after large tasks
- You can add checkpoints by prompting step-by-step instead
