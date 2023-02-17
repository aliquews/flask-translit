from sqlalchemy.orm import Session

from .tables import Translation
from .database import get_session

def create(text: str, text_translit: str, session: Session = next(get_session())):
    translation = Translation(
        text=text,
        text_translit=text_translit,
    )
    session.add(translation)
    try:
        session.commit()
    except:
        session.rollback()
        raise
    