import os


def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    clear_console()
    print(
        r"""

███████╗██╗ ██████╗ ██╗  ██╗████████╗███████╗██████╗  ██████╗  ██████╗ 
██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝ ██╔════╝ 
█████╗  ██║██║  ███╗███████║   ██║   █████╗  ██████╔╝██║  ███╗██║  ███╗
██╔══╝  ██║██║   ██║██╔══██║   ██║   ██╔══╝  ██╔══██╗██║   ██║██║   ██║
██║     ██║╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║╚██████╔╝╚██████╔╝
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ 
                                        
"""
    )


def get_menu_option(prompt: str, min_option: int, max_option: int) -> int:
    try:
        option = int(input(prompt))
        if option >= min_option and option <= max_option:
            return option
        print(f"Opção inválida! Digite um número entre {min_option} e {max_option}.")
    except Exception:
        print("Digite um valor válido!")
    return -1
