import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class UserBankAccount(Base):
    """User Bank Accounts model."""

    __tablename__ = "user_bank_accounts"

    id = Column(UUID(as_uuid=True), unique=True, nullable=False, blank=False, default=uuid.uuid4)
    number = Column(String, nullable=False, blank=False)
    name = Column(String, nullable=False, blank=False)
    bank = Column(String, nullable=False, blank=False)
    branch = Column(String)
    account_type = Column(String)
    currency = Column(String, nullable=False, blank=False)
    iban = Column(String)
    swift = Column(String)

    user = relationship("User", back_populates="user_bank_accounts")
