import uuid

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import backref
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class TransferContact(Base):
    """Transfer Contact model."""

    __tablename__ = "transfer_contact"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255))
    phone_number = Column(String(255))
    street_address = Column(String(255))
    zip_code = Column(String(255))
    city = Column(String(255))
    account_number = Column(String(255), nullable=False)

    user = relationship(
        "User", backref=backref("transfer_contacts", uselist=False, passive_deletes=True), foreign_keys=[user_id]
    )
