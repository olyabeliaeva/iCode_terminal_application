from simple_term_menu import TerminalMenu

from console_ui.contract_menu import ContractMenu
from console_ui.project_menu import ProjectMenu
from constants.menu_options import MainMenuOptions
from utils.menu_utils import MenuUtils


class MainMenu:

    @staticmethod
    def show_menu():
        main_menu_option_names = MainMenuOptions.get_option_names()
        main_menu = TerminalMenu(main_menu_option_names)
        selected_item_index = main_menu.show()
        if selected_item_index == MainMenuOptions.PROJECT.value.index:
            ProjectMenu.show_menu()
        elif selected_item_index == MainMenuOptions.CONTRACT.value.index:
            ContractMenu.show_menu()
        MenuUtils.show_options(
            selected_item_index=selected_item_index,
            all_projects_index=MainMenuOptions.AlL_PROJECTS.value.index,
            all_contracts_index=MainMenuOptions.ALL_CONTRACTS.value.index,
            exit_index=MainMenuOptions.EXIT.value.index
        )
