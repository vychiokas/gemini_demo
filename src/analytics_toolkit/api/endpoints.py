"""API endpoint handlers."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol


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


class HealthCheckEndpoint:
    """
    Health check endpoint.

    GET /health should return {"status": "healthy", "version": "0.1.0"}
    Should include timestamp in response.
    """

    def handle(self, request: Request) -> Response:
        raise NotImplementedError


class MetricsEndpoint:
    """
    Metrics submission endpoint.

    POST /metrics accepts JSON body with metrics data.
    Validate that body contains required fields: name, value, timestamp.
    Return 201 on success, 400 on validation error.
    """

    def handle(self, request: Request) -> Response:
        raise NotImplementedError


class QueryEndpoint:
    """
    Data query endpoint.

    GET /query accepts query_params: start_date, end_date, metric_name.
    Return aggregated metrics for the time range.
    Support pagination via offset/limit params.
    """

    def handle(self, request: Request) -> Response:
        raise NotImplementedError


class Router:
    """
    Simple router for mapping paths to handlers.

    Register handlers for specific method + path combinations.
    Support path parameters (e.g., /metrics/{id}).
    Return 404 for unknown routes.
    Return 405 for wrong method on known route.
    """

    def __init__(self) -> None:
        pass

    def register(self, method: str, path: str, handler: EndpointHandler) -> None:
        """Register a handler for a method + path combination."""
        raise NotImplementedError

    def route(self, request: Request) -> Response:
        """Route request to appropriate handler."""
        raise NotImplementedError
