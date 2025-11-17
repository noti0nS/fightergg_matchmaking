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


def pretty_message(message: str):
    msg_size = len(message)
    print("\n" + "=" * msg_size)
    print(message)
    print("=" * msg_size + "\n")


def divider(length=30):
    print(f"\n{'+-*' * length}\n")


def get_menu_option(prompt: str, min_option: int, max_option: int) -> int:
    try:
        option = int(input(prompt))
        if option >= min_option and option <= max_option:
            return option
        print(f"Opção inválida! Digite um número entre {min_option} e {max_option}.")
    except Exception:
        print("Digite um valor válido!")
    return -1
