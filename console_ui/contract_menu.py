from simple_term_menu import TerminalMenu

from constants.constants import CHOOSE_CONTRACT, CONTRACT_NAME
from constants.menu_options import ContractMenuOptions
from db.database import Contract
from services.contract_user_service import ContractUserService
from utils.menu_utils import MenuUtils


class ContractMenu:

    @staticmethod
    def _choose_contract() -> Contract:
        contracts = ContractUserService.get_all_contracts()
        contract_index = TerminalMenu(list(map(repr, contracts)), title=CHOOSE_CONTRACT).show()
        return contracts[contract_index]

    @staticmethod
    def show_menu():
        contract_option_names = ContractMenuOptions.get_option_names()
        menu = TerminalMenu(contract_option_names)
        selected_item_contract = menu.show()
        if selected_item_contract == ContractMenuOptions.CREATE_CONTRACT.value.index:
            name = input(CONTRACT_NAME)
            ContractUserService.create_contract(name)
        elif selected_item_contract == ContractMenuOptions.CONFIRM_CONTRACT.value.index:
            contract = ContractMenu._choose_contract()
            ContractUserService.confirm_contract(contract)
        elif selected_item_contract == ContractMenuOptions.COMPLETE_CONTRACT.value.index:
            contract = ContractMenu._choose_contract()
            ContractUserService.complete_contract(contract)
        MenuUtils.show_options(
            selected_item_index=selected_item_contract,
            all_projects_index=ContractMenuOptions.ALL_PROJECTS.value.index,
            all_contracts_index=ContractMenuOptions.ALL_CONTRACTS.value.index,
            exit_index=ContractMenuOptions.EXIT.value.index
        )
