from enum import Enum
from typing import List


class MenuOption:
    def __init__(self, index: int, option_name: str):
        self.index = index
        self.option_name = option_name


class MainMenuOptions(Enum):
    PROJECT = MenuOption(0, '1.Project')
    CONTRACT = MenuOption(1, '2.Contract')
    AlL_PROJECTS = MenuOption(2, '3.All projects')
    ALL_CONTRACTS = MenuOption(3, '4.All contracts')
    EXIT = MenuOption(4, '5.Quit the program')

    @staticmethod
    def get_option_names() -> List[str]:
        return [
            MainMenuOptions.PROJECT.value.option_name,
            MainMenuOptions.CONTRACT.value.option_name,
            MainMenuOptions.AlL_PROJECTS.value.option_name,
            MainMenuOptions.ALL_CONTRACTS.value.option_name,
            MainMenuOptions.EXIT.value.option_name
        ]


class ProjectMenuOptions(Enum):
    CREATE_PROJECT = MenuOption(0, '1.Create project')
    ADD_CONTRACT = MenuOption(1, '2.Add contract')
    COMPLETE_CONTRACT = MenuOption(2, '3.Complete contract')
    ALL_PROJECTS = MenuOption(3, '4.All projects')
    ALL_CONTRACTS = MenuOption(4, '5.All contracts')
    EXIT = MenuOption(5, '6.Quit the program')

    @staticmethod
    def get_option_names() -> List[str]:
        return [
            ProjectMenuOptions.CREATE_PROJECT.value.option_name,
            ProjectMenuOptions.ADD_CONTRACT.value.option_name,
            ProjectMenuOptions.COMPLETE_CONTRACT.value.option_name,
            ProjectMenuOptions.ALL_PROJECTS.value.option_name,
            ProjectMenuOptions.ALL_CONTRACTS.value.option_name,
            ProjectMenuOptions.EXIT.value.option_name
        ]


class ContractMenuOptions(Enum):
    CREATE_CONTRACT = MenuOption(0, '1.Create contract')
    CONFIRM_CONTRACT = MenuOption(1, '2.Confirm contract')
    COMPLETE_CONTRACT = MenuOption(2, '3.Complete contract')
    ALL_PROJECTS = MenuOption(3, '4.All projects')
    ALL_CONTRACTS = MenuOption(4, '5.All contracts')
    EXIT = MenuOption(5, '6.Quit the program')

    @staticmethod
    def get_option_names() -> List[str]:
        return [
            ContractMenuOptions.CREATE_CONTRACT.value.option_name,
            ContractMenuOptions.CONFIRM_CONTRACT.value.option_name,
            ContractMenuOptions.COMPLETE_CONTRACT.value.option_name,
            ContractMenuOptions.ALL_PROJECTS.value.option_name,
            ContractMenuOptions.ALL_CONTRACTS.value.option_name,
            ContractMenuOptions.EXIT.value.option_name
        ]
