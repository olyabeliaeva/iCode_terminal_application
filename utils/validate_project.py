from constants.contract_statuses import ContractStatus
from db.database import Contract, Project


class ValidateUtils:

    @staticmethod
    def validate(contract: Contract, project: Project) -> bool:
        return ValidateUtils._is_active_contract(contract) \
               and ValidateUtils._is_not_active_contracts(project) \
               and ValidateUtils._is_not_duplicate_contract(contract, project) \
               and ValidateUtils._is_not_used_contract(contract)

    @staticmethod
    def _is_not_duplicate_contract(contract: Contract, project: Project) -> bool:
        return contract not in project.contracts

    @staticmethod
    def _is_not_active_contracts(project: Project) -> bool:
        return len(list(filter(
            lambda contract: contract.status == ContractStatus.ACTIVE.value, project.contracts))) == 0

    @staticmethod
    def _is_active_contract(contract: Contract) -> bool:
        return contract.status == ContractStatus.ACTIVE.value

    @staticmethod
    def _is_not_used_contract(contract: Contract) -> bool:
        return contract.project_id is None
