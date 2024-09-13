from fastapi.testclient import TestClient
from src.server import app

client = TestClient(app)


def test_signup(mock_db_session):
    response = client.post("/auth/signup", 
                           json={ "email": "teste1@gmail.com","password": "123"})
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "teste1@gmail.com"
    assert data["id"] == 1
    
    mock_db_session.add.assert_called()
    mock_db_session.commit.assert_called()

