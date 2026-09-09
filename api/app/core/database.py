from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from api.app.core.config import settings


# engine: pool de conexao
engine = create_engine(settings.database_url, pool_pre_ping=True)

# SessionLocal é a fábrica de sessões (uma por requisicao)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)


# Base é a calsse mãe de todos os models SQLAlchemy
class Base(DeclarativeBase):
    pass
