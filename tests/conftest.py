import os
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from main import app
from database import Base, get_db
from app.models import News

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

TEST_DATABASE_URL = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}"
    "@127.0.0.1:5432/team_portal_test"
)
test_engine = create_engine(TEST_DATABASE_URL)

Base.metadata.create_all(bind=test_engine)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine
)


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
