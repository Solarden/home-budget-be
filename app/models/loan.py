import uuid

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Loan(Base):
    """Loan model."""

    __tablename__ = "loans"

    id = Column(UUID(as_uuid=True), unique=True, nullable=False, blank=False, default=uuid.uuid4)
    name = Column(String, nullable=False, blank=False)
    loan_type = Column(String)
    instalments = Column(String)
    total_amount = Column(Integer)
    paid_amount = Column(Integer)
    instalment_amount = Column(Integer)
    paid_instalments = Column(Integer)
    agreement_number = Column(String)
    signed_date = Column(DateTime)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    description = Column(Text)

    user = relationship("User", back_populates="loans")
