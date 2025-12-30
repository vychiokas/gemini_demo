"""
SCENARIO 4: Parallel development - API Endpoints stub.

This module needs implementation. It can be developed in parallel with:
- src/analytics_toolkit/api/middleware.py
- src/analytics_toolkit/api/validators.py
- src/analytics_toolkit/api/serializers.py

Ask the AI agent: "Implement all four API modules in parallel using sub-agents:
endpoints.py, middleware.py, validators.py, and serializers.py"

Each module should follow the interface defined below.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


# === Interface Definitions ===

@dataclass
class Request:
    """HTTP request representation."""

    method: str
    path: str
    headers: dict[str, str]
    body: dict[str, Any] | None = None
    query_params: dict[str, str] | None = None


@dataclass
class Response:
    """HTTP response representation."""

    status_code: int
    body: dict[str, Any]
    headers: dict[str, str] | None = None


class EndpointHandler(Protocol):
    """Protocol for endpoint handlers."""

    def handle(self, request: Request) -> Response:
        """Handle an incoming request."""
        ...


# === TODO: Implement the following endpoints ===

class HealthCheckEndpoint:
    """
    Health check endpoint.

    Requirements:
    - GET /health should return {"status": "healthy", "version": "0.1.0"}
    - Should include timestamp in response
    """

    def handle(self, request: Request) -> Response:
        # TODO: Implement
        raise NotImplementedError


class MetricsEndpoint:
    """
    Metrics submission endpoint.

    Requirements:
    - POST /metrics accepts JSON body with metrics data
    - Validate that body contains required fields: name, value, timestamp
    - Return 201 on success, 400 on validation error
    """

    def handle(self, request: Request) -> Response:
        # TODO: Implement
        raise NotImplementedError


class QueryEndpoint:
    """
    Data query endpoint.

    Requirements:
    - GET /query accepts query_params: start_date, end_date, metric_name
    - Return aggregated metrics for the time range
    - Support pagination via offset/limit params
    """

    def handle(self, request: Request) -> Response:
        # TODO: Implement
        raise NotImplementedError


class Router:
    """
    Simple router for mapping paths to handlers.

    Requirements:
    - Register handlers for specific method + path combinations
    - Support path parameters (e.g., /metrics/{id})
    - Return 404 for unknown routes
    - Return 405 for wrong method on known route
    """

    def __init__(self) -> None:
        # TODO: Implement
        pass

    def register(self, method: str, path: str, handler: EndpointHandler) -> None:
        """Register a handler for a method + path combination."""
        # TODO: Implement
        raise NotImplementedError

    def route(self, request: Request) -> Response:
        """Route request to appropriate handler."""
        # TODO: Implement
        raise NotImplementedError
