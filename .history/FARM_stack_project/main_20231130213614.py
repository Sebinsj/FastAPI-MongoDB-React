from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=['https://localhost:3000']

app.add_middleware(CORSMiddleware,allow_)

