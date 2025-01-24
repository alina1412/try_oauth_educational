from typing import Generator

import pytest
from fastapi.testclient import TestClient

from service.__main__ import app


@pytest.fixture(name="client", scope="session")
def fixture_client() -> Generator:
    with TestClient(app) as client:
        yield client
