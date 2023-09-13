from services.contract_user_service import ContractUserService
from services.project_user_service import ProjectUserService

IS_CONTINUE = 0


class MenuUtils:

    @staticmethod
    def show_options(selected_item_index, all_projects_index, all_contracts_index, exit_index):
        if selected_item_index == all_projects_index:
            for project in ProjectUserService.get_all_projects():
                print(project)
        elif selected_item_index == all_contracts_index:
            for contract in ContractUserService.get_all_contracts():
                print(contract)
        elif selected_item_index == exit_index:
            MenuUtils.quit_the_program()

    @staticmethod
    def quit_the_program():
        global IS_CONTINUE
        IS_CONTINUE = 1

    @staticmethod
    def is_continue():
        return IS_CONTINUE
