#!/usr/bin/env python3
"""
nurse model
"""
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from models.staff import Staff


class Nurse(Staff):
    """
    nurse model
    """
    __tablename__ = 'nurses'

    staff_id: Mapped[int] = mapped_column(ForeignKey('staffs.staff_id'),
                                          primary_key=True)
    job_title: Mapped[str] = mapped_column(String(50), default='Nurse')
    title: Mapped[str] = mapped_column(String(10), default='Nrs')

    __mapper_args__ = {
        'polymorphic_identity': 'nurse'
    }
