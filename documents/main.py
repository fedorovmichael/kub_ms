
from fastapi import FastAPI

app = FastAPI()

@app.post("/documents")
def process_documents(data: dict):
    # Simulate document processing
    print(f"Processing document with data: {data}")
    return {"status": "success", "message": "Document processed successfully"}

@app.get("/")
def read_root():
    return {"message": "Documents service is running"}
