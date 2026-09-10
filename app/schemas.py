from pydantic import BaseModel, ConfigDict, Field

class NewsCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1, max_length=1000)
    is_announcement: bool

class NewsUpdate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: str = Field(min_length=1, max_length=1000)
    is_announcement: bool    

class NewsPatch(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=255)
    description: str | None = Field(default=None, min_length=1, max_length=1000)
    is_announcement: bool | None = None 

class NewsResponse(BaseModel):
    news_id: int
    title: str
    description: str
    is_announcement: bool

    model_config = ConfigDict(from_attributes=True)
