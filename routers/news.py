from database import get_db
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.models import News
from app.schemas import NewsCreate, NewsUpdate, NewsPatch, NewsResponse

router = APIRouter(prefix="/news")


@router.get("", response_model=list[NewsResponse])
def get_news(db: Session = Depends(get_db)):
    news = db.query(News).all()

    return news

@router.get("/{news_id}", response_model=NewsResponse)
def get_single_news(news_id: int, db: Session = Depends(get_db)):
    news = db.query(News).filter(News.news_id == news_id).first()
    if news is None:
        raise HTTPException(
            status_code=404,
            detail="News not found"
        )
    return news

@router.post("", response_model=NewsResponse)
def create_news(news_data: NewsCreate, db: Session = Depends(get_db)):

    news = News(
        title=news_data.title,
        description=news_data.description,
        is_announcement=news_data.is_announcement
    )

    db.add(news)
    db.commit()
    db.refresh(news)

    return news

@router.put("/{news_id}", response_model=NewsResponse)
def update_news(news_id: int, news_data: NewsUpdate, db: Session = Depends(get_db)):

    news = db.query(News).filter(News.news_id == news_id).first()

    if news is None:
        raise HTTPException(
            status_code=404,
            detail="News not found"
        )
    
    news.title = news_data.title
    news.description = news_data.description
    news.is_announcement = news_data.is_announcement

    db.commit()
    db.refresh(news)

    return news        

@router.patch("/{news_id}", response_model=NewsResponse)
def partial_update_news(news_id: int, news_data: NewsPatch, db: Session = Depends(get_db)):

    news = db.query(News).filter(News.news_id == news_id).first()

    if news is None:
        raise HTTPException(
            status_code=404,
            detail="News not found"
        )
    news_data = news_data.model_dump(exclude_unset=True)

    for field, value in news_data.items():
        setattr(news, field, value)

    db.commit()
    db.refresh(news)

    return news   


@router.delete("/{news_id}", response_model=NewsResponse)
def delete_news(news_id: int, db: Session = Depends(get_db)):

    news = db.query(News).filter(News.news_id == news_id).first()

    if news is None:
        raise HTTPException(
            status_code=404,
            detail="News not found"
        )
    
    db.delete(news)
    db.commit()

    return news    
