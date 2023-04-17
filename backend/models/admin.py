#!/usr/bin/env python3
"""
admin model
"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from models.staff import Staff


class Admin(Staff):
    """
    admin model
    """
    __tablename__ = 'admins'

    staff_id: Mapped[int] = mapped_column(ForeignKey('staffs.staff_id'),
                                          primary_key=True)

    is_superuser: Mapped[bool] = mapped_column(default=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }
