from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Initialize FastAPI app
app = FastAPI()

@app.get("/weather/{city}")
def get_weather(city: str):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="City not found")
    
    data = response.json()
    return {
        "city": data["location"]["name"],
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"]
    }

