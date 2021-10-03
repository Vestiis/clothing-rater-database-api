from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.config import Config

ssl_args = {
    "sslrootcert": "server-ca.pem",
    "sslcert": "client-cert.pem",
    "sslkey": "client-key.pem",
}
engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    # connect_args={"sslmode": "require"},
    connect_args=ssl_args,
    pool_pre_ping=True,
    pool_size=15,
    max_overflow=5,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
        # return db
    finally:
        db.close()
