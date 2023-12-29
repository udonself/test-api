from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import users_router, tasks_router


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


for router in (users_router, tasks_router):
    app.include_router(router)