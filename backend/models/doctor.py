#!/usr/bin/env python3
"""
doctor model
"""
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from models.staff import Staff


class Doctor(Staff):
    """
    doctor model
    """
    __tablename__ = 'doctors'

    staff_id: Mapped[int] = mapped_column(ForeignKey('staffs.staff_id'),
                                          primary_key=True)
    job_title: Mapped[str] = mapped_column(String(50), default='Doctor')
    title: Mapped[str] = mapped_column(String(10), default='Dr.')
    speciality: Mapped[str] = mapped_column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'doctor'
    }
