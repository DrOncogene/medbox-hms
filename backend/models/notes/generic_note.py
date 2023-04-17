#!/usr/bin/env python3
"""
generic note
"""
from sqlalchemy import ForeignKey, Text, String
from sqlalchemy.orm import Mapped, mapped_column

from models.model import Model, Base


class Note(Model, Base):
    """Generic note model"""
    __tablename__ = 'notes'

    pid: Mapped[int] = mapped_column(
        ForeignKey('patients.pid', ondelete='CASCADE'))
    note: Mapped[str | None] = mapped_column(Text)
    note_type: Mapped[str] = mapped_column(String(20))
    creator: Mapped[str] = mapped_column(String(100))

    __mapper_args__ = {
        'polymorphic_identity': 'note',
        'polymorphic_on': 'note_type'
    }

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        if self.created_by is not None:
            from storage import db
            from models.staff import Staff
            staff = db.get_by_staff_id(Staff, self.created_by)
            self.creator = staff.full_name

    def __repr__(self) -> str:
        name = self.__class__.__name__
        return f"{name}(id={self.id}, patient_id={self.pid})"
