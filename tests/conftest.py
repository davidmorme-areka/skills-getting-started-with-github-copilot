"""Shared pytest fixtures for backend API tests.

Tests in this suite follow the AAA pattern:
- Arrange: prepare input and preconditions
- Act: execute one API call
- Assert: verify response and state
"""

from copy import deepcopy

import pytest
from fastapi.testclient import TestClient
from typing import Iterator

from src.app import activities, app

@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(app) as client:
        yield client


@pytest.fixture(autouse=True)
def reset_activities() -> None:
    original = deepcopy(activities)

    yield

    activities.clear()
    activities.update(original)
