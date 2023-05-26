import uuid

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class UserBankAccount(Base):
    """User Bank Account model."""

    __tablename__ = "user_bank_account"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    number = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    bank = Column(String(255), nullable=False)
    branch = Column(String(255))
    account_type = Column(String(255))
    currency = Column(String(255), nullable=False)
    iban = Column(String(255))
    swift = Column(String(255))

    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = relationship(
        "User", backref=backref("user_bank_accounts", uselist=False, passive_deletes=True), foreign_keys=[user_id]
    )
