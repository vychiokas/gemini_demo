"""
SCENARIO 4: Parallel development - Middleware stub.

This module needs implementation. Develop in parallel with other API modules.

Requirements:
- Middleware should wrap endpoint handlers
- Support chaining multiple middleware
- Each middleware can modify request/response or short-circuit
"""

from __future__ import annotations

import time
from typing import Callable

from .endpoints import EndpointHandler, Request, Response


# === TODO: Implement the following middleware ===

class LoggingMiddleware:
    """
    Logging middleware.

    Requirements:
    - Log incoming request method, path, and timestamp
    - Log outgoing response status code and duration
    - Use structlog or standard logging
    """

    def __init__(self, handler: EndpointHandler) -> None:
        # TODO: Implement
        pass

    def handle(self, request: Request) -> Response:
        # TODO: Implement
        raise NotImplementedError


class AuthenticationMiddleware:
    """
    Authentication middleware.

    Requirements:
    - Check for 'Authorization' header
    - Support Bearer token format
    - Return 401 if missing or invalid
    - Add user_id to request context on success
    """

    def __init__(self, handler: EndpointHandler, secret_key: str) -> None:
        # TODO: Implement
        pass

    def handle(self, request: Request) -> Response:
        # TODO: Implement
        raise NotImplementedError


class RateLimitMiddleware:
    """
    Rate limiting middleware.

    Requirements:
    - Track requests per client (by IP or API key)
    - Configurable limit (requests per minute)
    - Return 429 when limit exceeded
    - Include Retry-After header
    """

    def __init__(
        self,
        handler: EndpointHandler,
        requests_per_minute: int = 60,
    ) -> None:
        # TODO: Implement
        pass

    def handle(self, request: Request) -> Response:
        # TODO: Implement
        raise NotImplementedError


class CORSMiddleware:
    """
    CORS middleware.

    Requirements:
    - Add appropriate CORS headers to responses
    - Handle preflight OPTIONS requests
    - Configurable allowed origins
    """

    def __init__(
        self,
        handler: EndpointHandler,
        allowed_origins: list[str] | None = None,
    ) -> None:
        # TODO: Implement
        pass

    def handle(self, request: Request) -> Response:
        # TODO: Implement
        raise NotImplementedError


class MiddlewareChain:
    """
    Chain multiple middleware together.

    Usage:
        chain = MiddlewareChain(endpoint)
        chain.add(LoggingMiddleware)
        chain.add(AuthenticationMiddleware, secret_key="xxx")
        handler = chain.build()
    """

    def __init__(self, endpoint: EndpointHandler) -> None:
        # TODO: Implement
        pass

    def add(
        self,
        middleware_class: type,
        **kwargs,
    ) -> "MiddlewareChain":
        """Add middleware to the chain."""
        # TODO: Implement
        raise NotImplementedError

    def build(self) -> EndpointHandler:
        """Build the final handler with all middleware applied."""
        # TODO: Implement
        raise NotImplementedError
