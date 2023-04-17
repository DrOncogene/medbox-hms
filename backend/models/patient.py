#!/usr/bin/env python3
"""
patient model
"""
from sqlalchemy.orm import Mapped, mapped_column

from models.model import Base
from models.user import User


class Patient(User, Base):
    """
    patient model
    """
    __tablename__ = 'patients'

    pid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
