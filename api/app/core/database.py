from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings


# engine: pool de conexao
engine = create_engine(settings.database_url, pool_pre_ping=True)

# SessionLocal é a fábrica de sessões (uma por requisicao)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)


# Base é a classe mãe de todos os models SQLAlchemy
class Base(DeclarativeBase):
    pass

# py -c "import app.models as m; print(sorted(m.Base.metadata.tables))"

# criar migrations
# alembic revision --autogenerate -m "<mensagem>"
# aplicar as migrations (criar tabela, modificr tabela, apagar tabelas)
# alembic upgrade head