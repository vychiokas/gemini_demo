# Scenario 4: Parallel Development with Sub-Agents

## Overview

This scenario demonstrates using multiple AI agents working in parallel to develop
independent modules simultaneously, significantly speeding up development.

## Target Files

Four API modules that can be developed independently:

1. `src/analytics_toolkit/api/endpoints.py` - HTTP endpoint handlers
2. `src/analytics_toolkit/api/middleware.py` - Request/response middleware
3. `src/analytics_toolkit/api/validators.py` - Request validation
4. `src/analytics_toolkit/api/serializers.py` - Model serialization

## Why Parallel Development?

These modules are:
- **Independent:** No circular dependencies
- **Well-defined:** Clear interfaces in stub files
- **Similar complexity:** Each takes roughly same effort
- **Integratable:** Work together but developed separately

## Demo Script

### Step 1: Analyze Dependencies
```
Analyze the four API modules (endpoints.py, middleware.py, validators.py,
serializers.py) and confirm they can be developed independently. List any
shared types or dependencies.
```

### Step 2: Parallel Implementation (if sub-agents available)
```
Using sub-agents, implement all four API modules in parallel:

Sub-agent 1: Implement endpoints.py
- HealthCheckEndpoint, MetricsEndpoint, QueryEndpoint, Router

Sub-agent 2: Implement middleware.py
- LoggingMiddleware, AuthenticationMiddleware, RateLimitMiddleware,
  CORSMiddleware, MiddlewareChain

Sub-agent 3: Implement validators.py
- Validator base class with all methods
- MetricsValidator, QueryParamsValidator

Sub-agent 4: Implement serializers.py
- Serializer base class
- MetricSerializer, MetricSeriesSerializer, UserSerializer
- PaginatedResponse, serialize_error

Each implementation must follow the interface in the stub file and include
complete type hints and docstrings.
```

### Step 3: Integration Verification
```
After all modules are implemented, verify they work together:
1. Create an endpoint that uses validators and serializers
2. Wrap it with middleware
3. Route a test request through the full stack
```

## Alternative: Sequential with Progress Tracking

If sub-agents aren't available:

```
Implement these four modules in sequence. After completing each, provide a
brief summary of what was implemented before moving to the next:

1. validators.py (needed by endpoints)
2. serializers.py (needed by endpoints)
3. middleware.py (wraps endpoints)
4. endpoints.py (uses validators and serializers)

Track progress and estimate completion.
```

## Module Specifications

### endpoints.py
```python
# Must implement:
class HealthCheckEndpoint:
    def handle(self, request: Request) -> Response: ...

class MetricsEndpoint:
    def handle(self, request: Request) -> Response: ...

class QueryEndpoint:
    def handle(self, request: Request) -> Response: ...

class Router:
    def register(self, method: str, path: str, handler: EndpointHandler) -> None: ...
    def route(self, request: Request) -> Response: ...
```

### middleware.py
```python
# Must implement:
class LoggingMiddleware
class AuthenticationMiddleware
class RateLimitMiddleware
class CORSMiddleware
class MiddlewareChain
```

### validators.py
```python
# Must implement:
class Validator:
    def required(self, field: str) -> "Validator": ...
    def string(self, field: str, ...) -> "Validator": ...
    def integer(self, field: str, ...) -> "Validator": ...
    # ... all methods
    def validate(self, data: dict) -> ValidationResult: ...

class MetricsValidator(Validator): ...
class QueryParamsValidator(Validator): ...
```

### serializers.py
```python
# Must implement:
class Serializer(Generic[T]):
    def serialize(self, obj: T, fields: list[str] | None = None) -> dict: ...
    def deserialize(self, data: dict) -> T: ...

class MetricSerializer(Serializer[Metric]): ...
class MetricSeriesSerializer(Serializer[MetricSeries]): ...
class UserSerializer(Serializer[User]): ...  # Must exclude api_key!
class PaginatedResponse: ...
```

## Timing Comparison

| Approach | Estimated Time | Notes |
|----------|----------------|-------|
| Sequential | ~20 min | One module at a time |
| Parallel (4 agents) | ~5-7 min | All modules simultaneously |

## Integration Test

After implementation, test integration:

```python
# Example integration test
from analytics_toolkit.api.endpoints import Router, HealthCheckEndpoint, MetricsEndpoint
from analytics_toolkit.api.middleware import MiddlewareChain, LoggingMiddleware
from analytics_toolkit.api.validators import MetricsValidator
from analytics_toolkit.api.serializers import MetricSerializer

# Create router with endpoints
router = Router()
router.register("GET", "/health", HealthCheckEndpoint())
router.register("POST", "/metrics", MetricsEndpoint())

# Wrap with middleware
chain = MiddlewareChain(router)
chain.add(LoggingMiddleware)

# Process request
request = Request(method="GET", path="/health", headers={})
response = chain.build().handle(request)
```

## Key Takeaway

Parallel development with sub-agents can significantly speed up implementing
independent modules. The key requirements are:
- Clear interfaces between modules
- No circular dependencies
- Well-defined specifications
- Integration testing after completion
