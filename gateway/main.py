
from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# In a real application, you would use a more secure way to store and handle credentials
# and service locations. For this example, we'll keep it simple.
users = {
    "user1": os.getenv("USER1_PASSWORD")
}

# Service locations (using Kubernetes service names)
PAYMENT_SERVICE_URL = os.getenv("PAYMENT_SERVICE_URL")
DOCUMENTS_SERVICE_URL = os.getenv("DOCUMENTS_SERVICE_URL")

@app.post("/gateway/{service}")
def gateway(service: str, data: dict, user: str, token: str):
    # Simulate credential check
    if user not in users or users[user] != token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if service == "payment":
        try:
            response = requests.post(PAYMENT_SERVICE_URL, json=data)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=503, detail=f"Payment service is unavailable: {e}")
    elif service == "documents":
        try:
            response = requests.post(DOCUMENTS_SERVICE_URL, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=503, detail=f"Documents service is unavailable: {e}")
    else:
        raise HTTPException(status_code=404, detail="Service not found")

@app.get("/")
def read_root():
    return {"message": "Gateway service is running"}
