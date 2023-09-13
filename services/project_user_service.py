from typing import List

from constants.contract_statuses import ContractStatus
from db.database import Contract, Project
from services.contract_service import ContractService
from services.project_service import ProjectService
from utils.validate_project import ValidateUtils


class ProjectUserService:

    @staticmethod
    def create_project(name: str):
        if len(ContractService.get_by_status(status=ContractStatus.ACTIVE.value)) >= 1:
            ProjectService.create_project(name=name)
        else:
            print('you cannot create a project without the existence of at least one active contract.')

    @staticmethod
    def add_contract(contract: Contract, project: Project):
        if ValidateUtils.validate(contract, project):
            ProjectService.add_contract_to_project(contract, project)
        else:
            print('validation failed.')

    @staticmethod
    def complete_contract(contract: Contract):
        ContractService.update_contract(contract=contract, status=ContractStatus.COMPLETED)

    @staticmethod
    def get_all_projects() -> List[Project]:
        return ProjectService.get_all()
