from typing import List

from constants.contract_statuses import ContractStatus
from db.database import Contract, Project
from repositories.contracts_repository import ContractRepository


class ContractService:

    @staticmethod
    def create_contract(name: str):
        contract = Contract(name=name)
        if not name:
            print('The name cannot be empty')
        else:
            ContractRepository.save(contract)

    @staticmethod
    def update_contract(contract: Contract, status: ContractStatus):
        ContractRepository.update(contract.id, status)

    @staticmethod
    def get_all() -> List[Contract]:
        return ContractRepository.get_all()

    @staticmethod
    def get_by_status(status: ContractStatus) -> List[Contract]:
        return ContractRepository.get_by_status(status=status)

    @staticmethod
    def get_contracts_by_project(project: Project) -> List[Contract]:
        return ContractRepository.get_contracts_by_project(project)
