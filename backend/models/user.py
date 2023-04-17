#!/usr/bin/env python3
"""
base user model
"""
from datetime import date
from enum import Enum

from sqlalchemy import String, Enum as Sa_Enum
from sqlalchemy.orm import Mapped, mapped_column

from models.model import Model


class Gender(Enum):
    """Gender enum"""
    male = 'Male'
    female = 'Female'


class MaritalStatus(Enum):
    """Marital status enum"""
    single = 'Single'
    married = 'Married'
    widowed = 'Widowed'
    divorced = 'Divorced'


class User(Model):
    """
    user model
    """

    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    other_names: Mapped[str | None] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(
        Sa_Enum(Gender, validate_strings=True))
    marital_status: Mapped[str] = mapped_column(
        Sa_Enum(MaritalStatus, validate_strings=True))
    dob: Mapped[date]
    address: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(20))
    next_of_kin: Mapped[str] = mapped_column(String(100))
    kin_phone: Mapped[str] = mapped_column(String(20))

    @property
    def full_name(self) -> str:
        name = f"{self.first_name} {self.last_name} {self.other_names}"
        return name.strip()

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.full_name}, email={self.email}"
