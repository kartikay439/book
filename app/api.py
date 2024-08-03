import pydantic
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from mangum import Mangum


import model
from  database import engine, SessionLocal

from sqlalchemy.orm import Session
app = FastAPI()
# handler=Mangum(app)
model.Base.metadata.create_all(bind=engine)

#pydantic model
class BookCreate(BaseModel):
    id: str
    title: str
    author: str
    description: str
    rating: int

    class Config:
        orm_mode = True




def get_db():
    db=SessionLocal()
    try:
        yield db

    finally:
        db.close()


# @app.post("/books", status_code=status.HTTP_201_CREATED)
# async def create_book(book: BookCreate, db: Session = Depends(get_db)):
#     db_user=model.Book(**book.model_dump())
#     try:
#         db.add(db_user)
#         db.commit()
#     except Exception as e:
#         db.rollback()
#         raise HTTPException(status_code=400, detail=str(e))
@app.get("/books",status_code=status.HTTP_200_OK)
async def get_books(db: Session = Depends(get_db)):
    return db.query(model.Book).all()
# def get_hello():
#     return {"message":"Hello World"}

