# 🌦️ Weather Microservice

## 📌 Overview
This **FastAPI-based microservice** fetches real-time weather data for a given city using an external weather API.  
It is designed to be **efficient, lightweight, and easy to deploy**.

## 🚀 Features
✔ Fetch current weather information for any city  
✔ Uses **FastAPI** for high-performance API development  
✔ Stores API keys securely in a `.env` file (not exposed in the code)  
✔ Includes an interactive API documentation interface  
✔ Can be deployed on **Render, Heroku, AWS Lambda, or Google Cloud Run**  

## 🛠️ Setup Instructions

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/ndsang001/Weather_Microservice.git
cd Weather_Microservice
```
### **2️⃣ Create and Activate a Virtual Environment (Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```
### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```
### **4️⃣ Add Your API Key**
Sign up at WeatherAPI (https://www.weatherapi.com) (or any other weather API provider).
Get an API key from your account.
Create a .env file in the project root and add:
```sh
WEATHER_API_KEY=your_api_key_here
```
### **5️⃣ Run the Microservice**
```sh
uvicorn main:app --reload
```
The service will be available at:
🔗 http://127.0.0.1:8000

### **6️⃣ Access API Documentation**
FastAPI automatically generates an interactive Swagger UI for testing endpoints.
🔗 http://127.0.0.1:8000/docs


### **📡 Example API Request**

To fetch weather data for Helsinki, send a GET request:

GET /weather/Helsinki
Example Response:
{
  "city": "Helsinki",
  "temperature": -2,
  "condition": "Partly cloudy"
}

### **🌍 Deployment Guide**

You can deploy this microservice on various cloud platforms, here is the guide for using Render:

Deploy on Render
1. Push your project to GitHub.
2. Create an account at Render.
3. Connect your GitHub repository.
4. Select FastAPI and set the START COMMAND to:
```sh
uvicorn main:app --host 0.0.0.0 --port $PORT
```
6. Add an environment variable for WEATHER_API_KEY.


### **📄 License**

This project is licensed under the MIT License.
Feel free to modify and use it as needed.

### **📬 Contact**

For any issues, open a GitHub issue or email me at:
📧 sangdinh2001@gmail.com
