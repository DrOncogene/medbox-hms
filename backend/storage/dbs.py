#!/usr/bin/env python3
"""
database engine
"""
from os import getenv
from typing import Type

from sqlalchemy import create_engine
from sqlalchemy.sql import select, column as col
from sqlalchemy.orm import scoped_session, sessionmaker

from models.model import Base
from models.staff import Staff
from models.doctor import Doctor
from models.nurse import Nurse
from models.pharmacist import Pharmacist
from models.record import RecordOfficer
from models.admin import Admin
from models.patient import Patient
from models.notes.consult import Consultation
from models.notes.vitals import Vitals

Staffs = Doctor | Nurse | Pharmacist | Admin | RecordOfficer | Staff
User = Patient | Staffs
Notes = Consultation | Vitals
T = User | Notes


DB_URL = getenv('DATABASE_URI')
USER = getenv('DB_USER') or 'medbox_dev'
PASSWD = getenv('DB_PWD') or 'medbox_pwd'
HOST = getenv('DB_HOST') or 'localhost'
DB_NAME = getenv('DB_NAME') or 'medbox_dev_db'
PORT = getenv('DB_PORT') or 3306


class DBS:
    """
    database storage engine
    """
    __engine = None
    __session = None
    __sessionmaker = None

    if DB_URL:
        url = DB_URL
    else:
        url = f"mysql+mysqldb://{USER}:{PASSWD}@{HOST}:{PORT}/{DB_NAME}"

    def __init__(self) -> None:
        self.__engine = create_engine(self.url, echo=True, pool_pre_ping=True)

    def load(self) -> None:
        """
        create a new session
        """
        Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, autoflush=False)
        self.__sessionmaker = scoped_session(factory)
        self.__session = self.__sessionmaker()

    def close_session(self) -> None:
        """
        close the current session
        """
        if self.__session:
            self.__session.close()
        self.__session = self.__sessionmaker()

    def save(self) -> None:
        """
        commit all changes of the current database session
        """
        try:
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            raise e

    def refresh(self, obj: T) -> None:
        """
        refresh the object with the current state in the database
        """
        self.__session.refresh(obj)

    def all(self, cls: Type[T]) -> list[T]:
        """
        query on the current database session all objects of the class
        """
        return self.__session.execute(select(cls)).scalars().all()

    def count(self, cls: Type[T]) -> int:
        """
        counts all objects of the class
        """
        return len(self.all(cls))

    def get_by_id(self, cls: Type[T], id: str) -> T:
        """
        query on the current database session the object of the class
        with the id
        """
        return self.__session.get(cls, id)

    def get_by_pid(self, pid: int) -> Patient:
        """
        query the patients table with the pid
        """
        return self.__session.get(Patient, pid)

    def get_by_staff_id(self, cls: Type[Staffs], staff_id: int) -> T:
        """
        query on the current database session the object of the class
        with the staff id
        """
        statement = select(cls).where(col(cls.staff_id) == staff_id)
        return self.__session.execute(statement).scalars().first()

    def get_by_email(self, cls: Type[T], email: str) -> T:
        """
        query on the current database session the object of the class
        with the email
        """
        statement = select(cls).where(col(cls.email) == email)
        return self.__session.execute(statement).scalars().first()

    def get_by_username(self, cls: Type[T], username: str) -> T:
        """
        query on the current database session the object of the class
        with the username
        """
        statement = select(cls).where(col(cls.username) == username)
        return self.__session.execute(statement).scalars().first()

    def new(self, new_obj: T) -> None:
        """
        add the object to the current database session
        """
        self.__session.add(new_obj)

    def delete(self, obj: T) -> bool:
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)
            return True
        return False
