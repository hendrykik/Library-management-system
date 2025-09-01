from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/library")

def create_db_engine():
    for i in range(30):  # Próbuj przez 30 sekund
        try:
            engine = create_engine(DATABASE_URL)
            # Test połączenia
            engine.connect()
            logger.info("Successfully connected to database")
            return engine
        except Exception as e:
            logger.info(f"Database connection attempt {i+1} failed: {e}")
            time.sleep(1)
    
    raise Exception("Could not connect to database after 30 attempts")

engine = create_db_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()