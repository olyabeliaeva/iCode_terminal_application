from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from constants.contract_statuses import ContractStatus
from db.database import engine, Contract, Project


class ContractRepository():

    @staticmethod
    def save(contract: Contract):
        with Session(autoflush=False, bind=engine, expire_on_commit=False) as db:
            db.add(contract)
            db.commit()
            db.refresh(contract)

    @staticmethod
    def update(contract_id: Contract, status: ContractStatus):
        with Session(autoflush=False, bind=engine, expire_on_commit=False) as db:
            contract = db.query(Contract).filter(Contract.id == contract_id).first()
            contract.status = status.value
            if status.value == ContractStatus.ACTIVE.value:
                contract.signing_date = datetime.now()
            db.add(contract)
            db.commit()

    @staticmethod
    def get_all() -> List[Contract]:
        with Session(autoflush=False, bind=engine, expire_on_commit=False) as db:
            contracts = db.query(Contract).all()
            return contracts

    @staticmethod
    def get_by_status(status: ContractStatus) -> List[Contract]:
        with Session(autoflush=False, bind=engine) as db:
            contracts = db.query(Contract).filter(Contract.status == status).all()
            return contracts

    @staticmethod
    def get_contracts_by_project(project: Project) -> List[Contract]:
        with Session(autoflush=False, bind=engine) as db:
            contracts = db.query(Contract).filter(Contract.project_id == project.id).all()
            return contracts
