from fastapi import FastAPI
from app.api.v1 import routes_user, routes_auth
from app.db.init_db import init_db

init_db()


app = FastAPI(
    title="Mi API con FastAPI y PostgreSQL",
    version="1.0.0"
)

app.include_router(routes_user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(routes_auth.router, prefix="/api/v1/auth", tags=["Auth"])