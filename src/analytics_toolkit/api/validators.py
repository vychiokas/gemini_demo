"""
SCENARIO 4: Parallel development - Validators stub.

This module needs implementation. Develop in parallel with other API modules.

Requirements:
- Validate request data against schemas
- Return detailed error messages
- Support common validation rules
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class ValidationError:
    """Represents a validation error."""

    field: str
    message: str
    code: str


@dataclass
class ValidationResult:
    """Result of validation."""

    is_valid: bool
    errors: list[ValidationError] = field(default_factory=list)

    @classmethod
    def success(cls) -> "ValidationResult":
        return cls(is_valid=True)

    @classmethod
    def failure(cls, errors: list[ValidationError]) -> "ValidationResult":
        return cls(is_valid=False, errors=errors)


# === TODO: Implement the following validators ===

class Validator:
    """
    Base validator class.

    Requirements:
    - Chain validation rules
    - Collect all errors (don't stop at first)
    - Support custom error messages
    """

    def __init__(self) -> None:
        # TODO: Implement
        pass

    def required(self, field: str) -> "Validator":
        """Field must be present and not None."""
        # TODO: Implement
        raise NotImplementedError

    def string(self, field: str, min_length: int = 0, max_length: int | None = None) -> "Validator":
        """Field must be a string with optional length constraints."""
        # TODO: Implement
        raise NotImplementedError

    def integer(self, field: str, min_val: int | None = None, max_val: int | None = None) -> "Validator":
        """Field must be an integer with optional range constraints."""
        # TODO: Implement
        raise NotImplementedError

    def number(self, field: str, min_val: float | None = None, max_val: float | None = None) -> "Validator":
        """Field must be a number with optional range constraints."""
        # TODO: Implement
        raise NotImplementedError

    def email(self, field: str) -> "Validator":
        """Field must be a valid email address."""
        # TODO: Implement
        raise NotImplementedError

    def datetime_iso(self, field: str) -> "Validator":
        """Field must be a valid ISO 8601 datetime string."""
        # TODO: Implement
        raise NotImplementedError

    def one_of(self, field: str, choices: list[Any]) -> "Validator":
        """Field must be one of the allowed values."""
        # TODO: Implement
        raise NotImplementedError

    def list_of(self, field: str, item_validator: "Validator") -> "Validator":
        """Field must be a list where each item passes validation."""
        # TODO: Implement
        raise NotImplementedError

    def validate(self, data: dict[str, Any]) -> ValidationResult:
        """Run all validation rules against data."""
        # TODO: Implement
        raise NotImplementedError


class MetricsValidator(Validator):
    """
    Specialized validator for metrics data.

    Required fields:
    - name: non-empty string
    - value: number
    - timestamp: ISO 8601 datetime

    Optional fields:
    - tags: dict of string key-value pairs
    - unit: string
    """

    def __init__(self) -> None:
        # TODO: Implement with predefined rules
        pass


class QueryParamsValidator(Validator):
    """
    Validator for query endpoint parameters.

    Required fields:
    - start_date: ISO 8601 datetime
    - end_date: ISO 8601 datetime

    Optional fields:
    - metric_name: string
    - aggregation: one of ['sum', 'avg', 'min', 'max', 'count']
    - offset: non-negative integer
    - limit: integer between 1 and 1000
    """

    def __init__(self) -> None:
        # TODO: Implement with predefined rules
        pass


def validate_request_body(data: dict[str, Any], validator: Validator) -> ValidationResult:
    """Convenience function to validate request body."""
    # TODO: Implement
    raise NotImplementedError
