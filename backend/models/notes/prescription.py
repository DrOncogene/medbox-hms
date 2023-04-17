#!/usr/bin/env python3
"""
prescription model
"""
from uuid import UUID
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from models.notes.generic_note import Note


# class Prescription(Note):
#     """Prescription model"""
#     __tablename__ = 'prescriptions'

#     id: Mapped[UUID] = mapped_column(ForeignKey('notes.id'),
#                                      primary_key=True)
#     drug_id: Mapped[UUID] = mapped_column(ForeignKey('drugs.id'))
#     dosage: Mapped[str] = mapped_column(String(100))
#     frequency: Mapped[str] = mapped_column(String(100))
#     duration: Mapped[str] = mapped_column(String(100))
#     instructions: Mapped[str | None] = mapped_column(String(100))

#     __mapper_args__ = {
#         'polymorphic_identity': 'prescription',
#     }
