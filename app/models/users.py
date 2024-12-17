
from typing import List
from typing import Optional
from sqlalchemy import Boolean,Column,ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    mobile: Mapped[str] = mapped_column(String(30))
    first_name: Mapped[str]
    last_name: Mapped[Optional[str]]
    hashtags: Mapped[Optional[List["HashTag"]]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, first name={self.first_name!r}, last name={self.last_name!r})"

class HashTag(Base):
    __tablename__ = "hashtag"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="hashtags")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, name={self.name!r})"