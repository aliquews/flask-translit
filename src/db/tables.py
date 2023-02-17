from sqlalchemy import Column, Integer, String

from .database import Base


class Translation(Base):
    __tablename__ = "translations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String)
    text_translit = Column(String)

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}(text={self.text}, translate={self.text_translit})>'


