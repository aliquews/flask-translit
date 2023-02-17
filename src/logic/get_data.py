from sqlalchemy import select
from sqlalchemy.orm import Session

from src.db.tables import Translation
from src.db.database import get_session


def get_latest(session: Session = next(get_session())):
    query = select(Translation)
    result = list(session.execute(query))
    if len(result) < 10:
        return result
    return result[len(result) - 10:]