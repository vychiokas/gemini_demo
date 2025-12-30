"""HTTP middleware components."""

from __future__ import annotations

from .endpoints import EndpointHandler, Request, Response


class LoggingMiddleware:
    """
    Logging middleware.

    Log incoming request method, path, and timestamp.
    Log outgoing response status code and duration.
    """

    def __init__(self, handler: EndpointHandler) -> None:
        pass

    def handle(self, request: Request) -> Response:
        raise NotImplementedError


class AuthenticationMiddleware:
    """
    Authentication middleware.

    Check for 'Authorization' header.
    Support Bearer token format.
    Return 401 if missing or invalid.
    Add user_id to request context on success.
    """

    def __init__(self, handler: EndpointHandler, secret_key: str) -> None:
        pass

    def handle(self, request: Request) -> Response:
        raise NotImplementedError


class RateLimitMiddleware:
    """
    Rate limiting middleware.

    Track requests per client (by IP or API key).
    Configurable limit (requests per minute).
    Return 429 when limit exceeded.
    Include Retry-After header.
    """

    def __init__(
        self,
        handler: EndpointHandler,
        requests_per_minute: int = 60,
    ) -> None:
        pass

    def handle(self, request: Request) -> Response:
        raise NotImplementedError


class CORSMiddleware:
    """
    CORS middleware.

    Add appropriate CORS headers to responses.
    Handle preflight OPTIONS requests.
    Configurable allowed origins.
    """

    def __init__(
        self,
        handler: EndpointHandler,
        allowed_origins: list[str] | None = None,
    ) -> None:
        pass

    def handle(self, request: Request) -> Response:
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
        pass

    def add(
        self,
        middleware_class: type,
        **kwargs: str,
    ) -> "MiddlewareChain":
        """Add middleware to the chain."""
        raise NotImplementedError

    def build(self) -> EndpointHandler:
        """Build the final handler with all middleware applied."""
        raise NotImplementedError
