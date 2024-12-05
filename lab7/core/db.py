from sqlalchemy import create_engine
from core.config import settings
from sqlalchemy.orm import declarative_base

engine = create_engine(settings.POSTGRES_DSN)

Base = declarative_base()
