from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from passlib.context import CryptContext
from uuid import UUID


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    if get_user_by_email(db, user.email):
        raise ValueError("El email ya está registrado")

    hashed_password = get_password_hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        verified=False,
        access_token=None,
        refresh_token=None,
        role="user"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(User).filter(User.is_active == True).all()

def get_user_by_id(db: Session, user_id: UUID):
    return db.query(User).filter(User.id == user_id, User.is_active == True).first()


def update_user(db: Session, user_id: UUID, user_data: UserUpdate):
    user = get_user_by_id(db, user_id)
    if not user:
        return None

    # Validar duplicado de email si están actualizando el email
    if user_data.email and user_data.email != user.email:
        existing_user = get_user_by_email(db, user_data.email)
        if existing_user:
            raise ValueError("El email ya está en uso por otro usuario")

    # Solo encriptar si envían una nueva password
    if user_data.password:
        user_data.password = get_password_hash(user_data.password)

    for field, value in user_data.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: UUID):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    user.is_active = False
    db.commit()
    db.refresh(user)
    return user