import os
from datetime import datetime
from typing import List

from sqlalchemy import Column, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column

from constants.contract_statuses import ContractStatus

DB_NAME = os.getenv('DB_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
engine = create_engine(f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@127.0.0.1:5432/{DB_NAME}")


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String(100), nullable=False)
    creation_date = Column(DateTime(), default=datetime.now)
    contracts: Mapped[List["Contract"]] = relationship(back_populates="project", lazy='subquery')

    def __repr__(self):
        return "{name: %s, creation_date: %s, contracts: %s}" % \
               (self.name, self.creation_date, self.contracts)


class Contract(Base):
    __tablename__ = 'contracts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name = Column(String(100), nullable=False)
    creation_date = Column(DateTime(), default=datetime.now)
    signing_date = Column(DateTime())
    status = Column(String(50), default=ContractStatus.DRAFT.value)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), nullable=True)
    project: Mapped["Project"] = relationship(back_populates="contracts", lazy='subquery')

    def __repr__(self):
        return "{name: %s, creation_date: %s, signing_date: %s, status: %s}" % \
               (self.name, self.creation_date, self.signing_date, self.status)


Base.metadata.create_all(engine)
