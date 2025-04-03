# app/db/session.py

from app.db.database import SessionLocal

# Dependency para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
