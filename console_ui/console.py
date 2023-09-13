from console_ui.main_menu import MainMenu

from utils.menu_utils import MenuUtils, IS_CONTINUE

while MenuUtils.is_continue() == IS_CONTINUE:
    MainMenu.show_menu()
