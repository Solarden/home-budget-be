import uuid

from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Transfer(Base):
    """Transfer model."""

    __tablename__ = "transfers"

    id = Column(UUID(as_uuid=True), unique=True, nullable=False, blank=False, default=uuid.uuid4)
    name = Column(String, nullable=False, blank=False)
    amount = Column(Integer)
    currency = Column(String)
    date = Column(DateTime)
    transfer_type = Column(String)
    is_recurring = Column(Boolean)
    transfer_title = Column(String)
    description = Column(Text)

    user = relationship("User", back_populates="transfers")
    user_bank_account = relationship("UserBankAccount", back_populates="transfer_account")
    transfer_contact = relationship("TransferContact", back_populates="transfer_contact")
    loan = relationship("Loan", back_populates="loan")
