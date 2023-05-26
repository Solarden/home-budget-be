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


class Expense(Base):
    """Expense model."""

    __tablename__ = "expense"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    amount = Column(Integer)
    date = Column(DateTime)
    category = Column(String(255))
    description = Column(Text)

    user = relationship(
        "User", backref=backref("expenses", uselist=False, passive_deletes=True), foreign_keys=[user_id]
    )
