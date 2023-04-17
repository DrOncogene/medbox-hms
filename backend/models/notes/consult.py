#!/usr/bin/env python3
"""
consultation note model
"""
from uuid import UUID

from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from models.notes.generic_note import Note


class Consultation(Note):
    """Consultation note model"""
    __tablename__ = 'consultations'

    id: Mapped[UUID] = mapped_column(ForeignKey('notes.id'), primary_key=True)
    pc: Mapped[str | None] = mapped_column(Text)
    hpc: Mapped[str | None] = mapped_column(Text)
    pmhx: Mapped[str | None] = mapped_column(Text)
    poghx: Mapped[str | None] = mapped_column(Text)
    fshx: Mapped[str | None] = mapped_column(Text)
    prov_diag: Mapped[str] = mapped_column(Text)
    plan: Mapped[str | None] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"Consultation(id={self.id}, patient_id={self.pid})"
