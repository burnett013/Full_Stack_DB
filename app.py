from fastapi import FastAPI
from api import user_routes

app = FastAPI()
app.include_router(user_routes.router)