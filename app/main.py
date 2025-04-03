from fastapi import FastAPI
from app.api.v1 import routes_user  # Suponiendo que tenés rutas en v1/routes_user.py



app = FastAPI(
    title="Mi API con FastAPI y PostgreSQL",
    version="1.0.0"
)

# Incluye las rutas (puede haber varias)
app.include_router(routes_user.router, prefix="/api/v1/users", tags=["Users"])
