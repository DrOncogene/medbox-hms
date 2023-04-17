#!/usr/bin/env python3
"""
pharmacist model
"""
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from models.staff import Staff


class Pharmacist(Staff):
    """
    pharmacist model
    """
    __tablename__ = 'pharmacists'

    staff_id: Mapped[int] = mapped_column(ForeignKey('staffs.staff_id'),
                                          primary_key=True)
    job_title: Mapped[str] = mapped_column(String(50), default='Pharmacist')
    title: Mapped[str] = mapped_column(String(10), default='Pharm')

    __mapper_args__ = {
        'polymorphic_identity': 'pharmacist'
    }
