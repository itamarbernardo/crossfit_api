from fastapi import FastAPI
from crossfit_api.routers import api_router

app = FastAPI(title='CrossfitApi')
app.include_router(api_router)