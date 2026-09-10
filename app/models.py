from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class News(Base):
    __tablename__ = "news"

    news_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_announcement = Column(Boolean, nullable=False)