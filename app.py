from fastapi import FastAPI,Request
import os
import datetime
from sqlalchemy.sql.sqltypes import DATETIME
from werkzeug.utils import secure_filename
from fastapi.staticfiles import StaticFiles
from fastapi.datastructures import UploadFile
from fastapi.param_functions import Depends, File, Form
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from sqlalchemy.orm import relationship
import time as t
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()
SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()
app.mount('/static',StaticFiles(directory="static"),name="static")


class upload_file(Base):
    __tablename__="upload_file"
    id = Column(Integer,primary_key=True)
    create_date = Column(DATETIME,default=datetime.datetime.now())
    old_name = Column(String)
    new_name = Column(String)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/')
def add_post(db:Session=Depends(get_db),file:UploadFile=File(...)):
    text = secure_filename(file.filename)
    old_name = file.filename
    contents = file.file.read()
    new = upload_file(old_name=old_name,new_name=text)
    db.add(new)
    db.commit()
    with open(f"./static/"+text,'wb') as f:
        f.write(contents)
    return {"filename":file.filename}


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0',port=5000)