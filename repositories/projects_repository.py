from typing import List

from sqlalchemy.orm import Session

from db.database import engine, Project, Contract


class ProjectRepository:

    @staticmethod
    def save(project: Project):
        with Session(autoflush=False, bind=engine) as db:
            db.add(project)
            db.commit()
            db.refresh(project)

    @staticmethod
    def get_by_id(id: int) -> Project:
        with Session(autoflush=False, bind=engine) as db:
            project = db.query(Project).filter(Project.id == id).first()
            return project

    @staticmethod
    def add_contract_to_project(contract: Contract, project: Project):
        with Session(autoflush=False, bind=engine) as db:
            project = ProjectRepository.get_by_id(project.id)
            project.contracts.append(contract)
            db.add(project)
            db.commit()

    @staticmethod
    def get_all() -> List[Project]:
        with Session(autoflush=False, bind=engine) as db:
            projects = db.query(Project).all()
            return projects
