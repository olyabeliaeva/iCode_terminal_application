from typing import List

from constants.contract_statuses import ContractStatus
from db.database import Contract, Project
from services.contract_service import ContractService


class ContractUserService:

    @staticmethod
    def create_contract(name: str):
        ContractService.create_contract(name=name)

    @staticmethod
    def confirm_contract(contract: Contract):
        ContractService.update_contract(contract=contract, status=ContractStatus.ACTIVE)

    @staticmethod
    def complete_contract(contract: Contract):
        ContractService.update_contract(contract=contract, status=ContractStatus.COMPLETED)

    @staticmethod
    def get_all_contracts() -> List[Contract]:
        return ContractService.get_all()

    @staticmethod
    def get_contracts_by_project(project: Project) -> List[Contract]:
        return ContractService.get_contracts_by_project(project)
