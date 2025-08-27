
from fastapi import FastAPI

app = FastAPI()

@app.post("/pay")
def process_payment(data: dict):
    # Simulate payment processing
    print(f"Processing payment with data: {data}")
    return {"status": "success", "message": "Payment processed successfully"}

@app.get("/")
def read_root():
    return {"message": "Payment service is running"}
