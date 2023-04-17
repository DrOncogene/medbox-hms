#!/usr/bin/env python3
"""
staff model
"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.model import Base
from models.user import User


class Staff(User, Base):
    """
    staff model
    """
    __tablename__ = 'staffs'

    staff_id: Mapped[int] = mapped_column(unique=True, primary_key=True,
                                          autoincrement=True)
    staff_type: Mapped[str] = mapped_column(String(20))
    department: Mapped[str | None] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    username: Mapped[str] = mapped_column(String(20), unique=True)
    password: Mapped[str] = mapped_column(String(50))
    job_title: Mapped[str | None] = mapped_column(String(50))
    title: Mapped[str | None] = mapped_column(String(10))
    speciality: Mapped[str | None] = mapped_column(String(50))

    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)

    __mapper_args__ = {
        'polymorphic_identity': 'staff',
        'polymorphic_on': 'staff_type'
    }

    def get_staff_id(self) -> str:
        """
        format staff id
        """
        return f"{self.staff_id:05d}"
