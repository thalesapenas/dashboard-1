from unittest.mock import MagicMock
import pytest
from src.server import app
from src.infra.sqlalchemy.config.database import get_db


mock_session = MagicMock()

def override_get_db():
    try:
        yield mock_session
    finally:
        pass
    
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def mock_db_session():
    return mock_session