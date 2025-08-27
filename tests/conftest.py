# tests/conftest.py
import os
import pytest
from app.settings import Settings

os.environ["ENV_FILE"] = "tests/test.env"


@pytest.fixture(scope="session")
def settings():
    return Settings(_env_file=os.environ["ENV_FILE"])
