from dotenv import load_dotenv
from ui import menu
from services import auth


def main():
    load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

    menu.show_banner()

    while True:
        print("[1] - Realize o Login")
        print("[2] - Cadastre-se")
        print("[3] - Sair")
        option = menu.get_menu_option("> ", 1, 3)
        if option == -1:
            continue

        user: tuple = None
        match option:
            case 1:
                menu.clear_console()
                email = input("Digite o seu e-mail: ")
                password = input("Digite a sua senha: ")
                user = auth.login(email, password)
            case 2:
                menu.clear_console()
                # TODO Gabriel: Implementar register
            case 3:
                break

        if not user:
            continue

        menu.show_banner()

        print(f"Seja bem vindo, {user[1]}!\n")

        while user:
            print("[1] - Listar Eventos")
            print("[2] - Participar de Eventos")
            print("[3] - Gerenciar Eventos")
            print("[4] - Criar Evento")
            print("[5] - Logout")

            option = menu.get_menu_option("> ", 1, 5)
            if option == -1:
                continue

            match option:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    user = None

        menu.show_banner()

    print("Até breve! :-)")


if __name__ == "__main__":
    main()
