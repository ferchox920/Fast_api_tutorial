from fastapi import FastAPI
from app.api.v1 import routes_user, routes_auth
from app.db.init_db import init_db
import os
from app.db.database import Base, engine

if os.getenv("RESET_DB", "false").lower() == "true":
    print("Reiniciando la base de datos...")
    Base.metadata.drop_all(bind=engine)  # Borra TODAS las tablas que estén registradas en Base
    print("Tablas borradas, ahora se vuelven a crear...")
    Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Mi API con FastAPI y PostgreSQL",
    version="1.0.0"
)

app.include_router(routes_user.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(routes_auth.router, prefix="/api/v1/auth", tags=["Auth"])
