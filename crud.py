from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models, schemas

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_all_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = pwd_ctx.hash(user.password)
    db_user = models.User(
        name=user.name, phone=user.phone,
        email=user.email, password=hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    data = user.model_dump(exclude_unset=True)
    if "password" in data:
        data["password"] = pwd_ctx.hash(data["password"])
    for k, v in data.items():
        setattr(db_user, k, v)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if not db_user:
        return False
    db.delete(db_user)
    db.commit()
    return True