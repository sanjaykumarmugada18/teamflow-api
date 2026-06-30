from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# 1. Create the database engine
engine = create_engine(settings.DATABASE_URL)

# 2. Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Create a base class for our ORM models
Base = declarative_base()

# 4. Dependency to get a database session per reuest
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
