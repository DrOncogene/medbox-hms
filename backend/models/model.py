#!/usr/bin/env python3
"""
module for the base model
"""
from datetime import datetime
from uuid import uuid4, UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    DeclarativeBase,
    declarative_mixin,
    declared_attr,
    Mapped,
    MappedColumn,
    mapped_column
)
from sqlalchemy.sql import func
# db is imported within necessary methods


class Base(DeclarativeBase):
    pass


@declarative_mixin
class Model:
    """
    base model class
    """

    id: Mapped[UUID] = mapped_column(default=uuid4, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(),
                                                 server_onupdate=func.now())

    @declared_attr
    def created_by(cls) -> MappedColumn[int]:
        fk = ForeignKey('staffs.staff_id', ondelete='SET NULL')
        attr: Mapped[int] = mapped_column(fk, nullable=True)
        return attr

    @declared_attr
    def updated_by(cls) -> MappedColumn[int]:
        fk = ForeignKey('staffs.staff_id', ondelete='SET NULL')
        attr: Mapped[int] = mapped_column(fk, nullable=True)
        return attr

    def __init__(self, *args, **kwargs) -> None:
        try:
            del kwargs['__class__']
        except KeyError:
            pass

        self.__dict__.update(kwargs)

    def to_dict(self) -> dict:
        """
        convert object to dictionary
        """
        obj_dict = {k: v for k, v in self.__dict__.items()
                    if not k.startswith('_') and k != 'password'}
        if hasattr(self, 'staff_id'):
            obj_dict['staff_id'] = self.get_staff_id()

        return obj_dict
