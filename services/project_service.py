from typing import List

from db.database import Project, Contract
from repositories.projects_repository import ProjectRepository


class ProjectService:

    @staticmethod
    def create_project(name: str):
        project = Project(name=name)
        if not name:
            print('The name cannot be empty')
        else:
            ProjectRepository.save(project)

    @staticmethod
    def add_contract_to_project(contract: Contract, project: Project):
        ProjectRepository.add_contract_to_project(contract, project)

    @staticmethod
    def get_all() -> List[Project]:
        return ProjectRepository.get_all()
