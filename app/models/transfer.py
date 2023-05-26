import uuid

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Transfer(Base):
    """Transfer model."""

    __tablename__ = "transfer"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user_bank_account_id = Column(Integer, ForeignKey("user_bank_account.id", ondelete="CASCADE"), nullable=False)
    transfer_contact_id = Column(Integer, ForeignKey("transfer_contact.id", ondelete="CASCADE"), nullable=False)
    loan_id = Column(Integer, ForeignKey("loan.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    amount = Column(Integer)
    currency = Column(String(255))
    date = Column(DateTime)
    transfer_type = Column(String(255))
    is_recurring = Column(Boolean)
    transfer_title = Column(String(255))
    description = Column(Text)

    user = relationship(
        "User", backref=backref("transfers", uselist=False, passive_deletes=True), foreign_keys=[user_id]
    )
    user_bank_account = relationship(
        "UserBankAccount",
        backref=backref("transfer_accounts", uselist=False, passive_deletes=True),
        foreign_keys=[user_bank_account_id],
    )
    transfer_contact = relationship(
        "TransferContact",
        backref=backref("transfer_contacts", uselist=False, passive_deletes=True),
        foreign_keys=[transfer_contact_id],
    )
    loan = relationship("User", backref=backref("Loan", uselist=False, passive_deletes=True), foreign_keys=[loan_id])
