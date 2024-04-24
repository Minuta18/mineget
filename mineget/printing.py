def get_overwriting_warning(path: str) -> str:
    return 'mineget is going to overwrite ' + path + '.'

def get_folder_error(path: str) -> str:
    return 'there is folder with path ' + path

def get_quitting_message() -> str:
    return 'Quitting...'

def input_y_or_n() -> bool:
    proceed = input('Proceed [Y/N]? ')
    while proceed.lower() != 'Y' or proceed.lower() != 'N':
        proceed = input('Please write Y (yes) or N (no): ')
    return proceed == 'Y'

def format_as_error(text: str) -> str:
    return '[bold red]' + text + '[/bold red]'

