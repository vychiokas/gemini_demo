"""Model serialization utilities."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass
class Metric:
    """Internal metric representation."""

    id: str
    name: str
    value: float
    timestamp: datetime
    tags: dict[str, str] | None = None
    unit: str | None = None


@dataclass
class MetricSeries:
    """Time series of metrics."""

    metric_name: str
    data_points: list[tuple[datetime, float]]
    aggregation: str | None = None


@dataclass
class User:
    """Internal user representation."""

    id: str
    username: str
    email: str
    created_at: datetime
    api_key: str


class Serializer(Generic[T]):
    """
    Base serializer class.

    Convert model to dict (serialize).
    Convert dict to model (deserialize).
    Support field selection.
    Handle nested objects.
    """

    def serialize(self, obj: T, fields: list[str] | None = None) -> dict[str, Any]:
        """Convert model to dictionary."""
        raise NotImplementedError

    def deserialize(self, data: dict[str, Any]) -> T:
        """Convert dictionary to model."""
        raise NotImplementedError

    def serialize_many(
        self, objs: list[T], fields: list[str] | None = None
    ) -> list[dict[str, Any]]:
        """Serialize a list of objects."""
        raise NotImplementedError


class MetricSerializer(Serializer[Metric]):
    """
    Serializer for Metric model.

    Serialization format:
    {
        "id": "...",
        "name": "...",
        "value": 123.45,
        "timestamp": "2024-01-15T10:30:00Z",
        "tags": {"key": "value"},
        "unit": "ms"
    }
    """

    def serialize(self, obj: Metric, fields: list[str] | None = None) -> dict[str, Any]:
        raise NotImplementedError

    def deserialize(self, data: dict[str, Any]) -> Metric:
        raise NotImplementedError


class MetricSeriesSerializer(Serializer[MetricSeries]):
    """
    Serializer for MetricSeries model.

    Serialization format:
    {
        "metric_name": "response_time",
        "aggregation": "avg",
        "data_points": [
            {"timestamp": "2024-01-15T10:00:00Z", "value": 100.5},
            {"timestamp": "2024-01-15T10:01:00Z", "value": 102.3}
        ]
    }
    """

    def serialize(
        self, obj: MetricSeries, fields: list[str] | None = None
    ) -> dict[str, Any]:
        raise NotImplementedError

    def deserialize(self, data: dict[str, Any]) -> MetricSeries:
        raise NotImplementedError


class UserSerializer(Serializer[User]):
    """
    Serializer for User model.

    Serialization format:
    {
        "id": "...",
        "username": "...",
        "email": "...",
        "created_at": "2024-01-15T10:30:00Z"
    }
    """

    EXCLUDED_FIELDS = ["api_key"]

    def serialize(self, obj: User, fields: list[str] | None = None) -> dict[str, Any]:
        raise NotImplementedError

    def deserialize(self, data: dict[str, Any]) -> User:
        raise NotImplementedError


class PaginatedResponse(Generic[T]):
    """
    Wrapper for paginated API responses.

    Format:
    {
        "data": [...],
        "pagination": {
            "total": 100,
            "offset": 0,
            "limit": 20,
            "has_more": true
        }
    }
    """

    def __init__(
        self,
        data: list[T],
        total: int,
        offset: int,
        limit: int,
        serializer: Serializer[T],
    ) -> None:
        pass

    def to_dict(self) -> dict[str, Any]:
        """Convert to API response format."""
        raise NotImplementedError


def serialize_error(
    error_code: str,
    message: str,
    details: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Serialize an error response.

    Format:
    {
        "error": {
            "code": "VALIDATION_ERROR",
            "message": "Invalid input",
            "details": {...}
        }
    }
    """
    raise NotImplementedError
