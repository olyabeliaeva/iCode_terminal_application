from typing import List

from simple_term_menu import TerminalMenu

from constants.constants import CHOOSE_CONTRACT, CHOOSE_PROJECT, PROJECT_NAME
from constants.menu_options import ProjectMenuOptions
from db.database import Contract, Project
from services.contract_user_service import ContractUserService
from services.project_user_service import ProjectUserService
from utils.menu_utils import MenuUtils


class ProjectMenu:

    @staticmethod
    def _choose_project() -> Project:
        projects = ProjectUserService.get_all_projects()
        project_index = TerminalMenu(list(map(repr, projects)), title=CHOOSE_PROJECT).show()
        return projects[project_index]

    @staticmethod
    def _choose_contract(contracts: List[Contract]) -> Contract:
        contract_index = TerminalMenu(list(map(repr, contracts)), title=CHOOSE_CONTRACT).show()
        return contracts[contract_index]

    @staticmethod
    def show_menu():
        project_option_names = ProjectMenuOptions.get_option_names()
        menu = TerminalMenu(project_option_names)
        selected_item_project = menu.show()
        if selected_item_project == ProjectMenuOptions.CREATE_PROJECT.value.index:
            name = input(PROJECT_NAME)
            ProjectUserService.create_project(name)
        elif selected_item_project == ProjectMenuOptions.ADD_CONTRACT.value.index:
            project = ProjectMenu._choose_project()
            contracts = ContractUserService.get_all_contracts()
            contract = ProjectMenu._choose_contract(contracts)
            ProjectUserService.add_contract(contract, project)
        elif selected_item_project == ProjectMenuOptions.COMPLETE_CONTRACT.value.index:
            project = ProjectMenu._choose_project()
            contracts = ContractUserService.get_contracts_by_project(project)
            contract = ProjectMenu._choose_contract(contracts)
            ProjectUserService.complete_contract(contract=contract)
        MenuUtils.show_options(
            selected_item_index=selected_item_project,
            all_projects_index=ProjectMenuOptions.ALL_PROJECTS.value.index,
            all_contracts_index=ProjectMenuOptions.ALL_CONTRACTS.value.index,
            exit_index=ProjectMenuOptions.EXIT.value.index
        )
