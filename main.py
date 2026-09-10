from fastapi import Depends, FastAPI


from routers import news
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Team Portal!"}


app.include_router(news.router)

