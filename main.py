from fastapi import FastAPI, Query
from services.scraper import get_google_reviews
from typing import Annotated
import json
with open("./mock_data/mock_reviews.json", "r", encoding="utf-8") as f:
  mock_reviews = json.load(f)

app = FastAPI()

@app.get("/")
def read_root():
  return {"Places": mock_reviews}

@app.get("/reviews")
def get_reviews(place_name: Annotated[str,Query(...,max_length=50, description="Place Name")] = ""):
  reviews = get_google_reviews(place_name, mock_reviews)
  return reviews
