import uuid

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


class Loan(Base):
    """Loan model."""

    __tablename__ = "loan"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    loan_type = Column(String(255))
    instalments = Column(String(255))
    total_amount = Column(Integer)
    paid_amount = Column(Integer)
    instalment_amount = Column(Integer)
    paid_instalments = Column(Integer)
    agreement_number = Column(String(255))
    signed_date = Column(DateTime)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    description = Column(Text)

    user = relationship("User", backref=backref("loans", uselist=False, passive_deletes=True), foreign_keys=[user_id])
