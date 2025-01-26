from fastapi import FastAPI, Depends, HTTPException
import models
from database import engine, SessionLocal


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
