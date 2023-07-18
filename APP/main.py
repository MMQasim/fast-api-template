from fastapi import FastAPI
import uvicorn
from server_config import settings
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",  # Replace with your frontend URL
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)



def main():
    uvicorn.run("APP.main:app",host=settings.system_ip_fast, port=settings.system_port_fast, log_level="info",reload=True)

if __name__ == "__main__":
    main()