import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class TransferContact(Base):
    """Transfer Contact model."""

    __tablename__ = "transfer_contacts"

    id = Column(UUID(as_uuid=True), unique=True, nullable=False, blank=False, default=uuid.uuid4)
    first_name = Column(String, nullable=False, blank=False)
    last_name = Column(String, nullable=False, blank=False)
    email = Column(String)
    phone_number = Column(String)
    street_address = Column(String)
    zip_code = Column(String)
    city = Column(String)
    account_number = Column(String, nullable=False, blank=False)

    user = relationship("User", back_populates="transfer_contacts")
