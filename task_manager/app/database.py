from sqlalchemy.ext.declarative import declarative_base
from databases import Database
from app.config import DATABASE_URL
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
import uuid
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "SessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# For ORM model declarations
Base = declarative_base()

# For async database operations
database = Database(DATABASE_URL)

class BaseModel(Base):
    """Abstract base model with common fields"""
    __abstract__ = True

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())
    
# Dependency to get DB session in route
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()