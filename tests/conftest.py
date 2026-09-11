import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from main import app
from database import Base, get_db, TestingSessionLocal


@pytest.fixture
def db_session():
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    app.dependency_overrides.clear()

@pytest.fixture
def create_news(client):
    post_data = {
        "title" : "This news is a test",
        "description" : "a pay rise will happen on June 2027 to all employees",
        "is_announcement" : True
    }
    response = client.post("/news", json = post_data)
    news_id = response.json()["news_id"]

    return news_id
