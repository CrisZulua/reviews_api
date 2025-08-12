from fastapi import HTTPException

# Funciones para obtener las reviews
def get_place_id(place_name:str, mock_reviews):
  """Gets the place_id from google using the place name"""
  for p in mock_reviews:
    if place_name == p["place"]:
      return p["place_id"]
  raise HTTPException(status_code=404,detail="Place not found!")

#No hace falta esta función ahora mismo, pero más adelante servirá
def get_reviews_by_place_id(place_id:str, mock_reviews):
  """Get the reviews from a place from its place_id"""
  for p in mock_reviews:
    if place_id == p["place_id"]:
      return p["reviews"]


def get_google_reviews(place_name:str, mock_reviews):
  """Gets place info and returns the last 5 reviews and metadata"""
  place_id = get_place_id(place_name, mock_reviews)
  reviews = get_reviews_by_place_id(place_id, mock_reviews)
  return reviews

