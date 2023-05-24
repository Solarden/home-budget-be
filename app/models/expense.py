import uuid

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Expense(Base):
    """Expenses model."""

    __tablename__ = "expenses"

    id = Column(UUID(as_uuid=True), unique=True, nullable=False, blank=False, default=uuid.uuid4)
    name = Column(String, nullable=False, blank=False)
    amount = Column(Integer)
    date = Column(DateTime)
    category = Column(String)
    description = Column(Text)

    user = relationship("User", back_populates="expenses")
