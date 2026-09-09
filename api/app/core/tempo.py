from datetime import datetime, timezone

# utilitário de data e hora. guardamos no banco de dados em UTC, sem timezone.
def agora() -> datetime:
    return datetime.now(timezone.utc).replace(tzinfo=None)