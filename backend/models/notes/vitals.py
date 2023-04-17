#!/usr/bin/env python3
"""
vital signs model
"""
from uuid import UUID

from sqlalchemy import ForeignKey, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.notes.generic_note import Note


class Vitals(Note):
    """Vital signs model"""
    __tablename__ = 'vitals'

    id: Mapped[UUID] = mapped_column(ForeignKey('notes.id'), primary_key=True)
    temp: Mapped[float] = mapped_column(Float(precision=1))
    sbp: Mapped[int | None]
    dbp: Mapped[int | None]
    pr: Mapped[int]
    rr: Mapped[int]
    weight: Mapped[float | None] = mapped_column(Float(precision=1))
    height: Mapped[float | None] = mapped_column(Float(precision=1))
    bmi: Mapped[float | None] = mapped_column(Float(precision=1))
    spo2: Mapped[int | None]

    __mapper_args__ = {
        'polymorphic_identity': 'vitals',
    }

    def __repr__(self) -> str:
        return f"Vitals(id={self.id}, patient_id={self.pid})"
