#!/usr/bin/env python3
"""
record officer model
"""
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from models.staff import Staff


class RecordOfficer(Staff):
    """
    record officer model
    """
    __tablename__ = 'record_officers'

    staff_id: Mapped[int] = mapped_column(ForeignKey('staffs.staff_id'),
                                          primary_key=True)
    job_title: Mapped[str] = mapped_column(String(50),
                                           default='Record Officer')

    __mapper_args__ = {
        'polymorphic_identity': 'record_officer'
    }
