from dotenv import load_dotenv
from utils import ui_utils
from services import auth


def main():
    load_dotenv()  # Carrega variáveis de ambiente do arquivo .env

    ui_utils.show_banner()

    while True:
        print("[1] - Realize o Login")
        print("[2] - Cadastre-se")
        print("[3] - Sair")

        option = ui_utils.get_menu_option("> ", 1, 3)
        if option == -1:
            continue

        user: tuple = None
        match option:
            case 1:
                ui_utils.clear_console()
                user = auth.login()
            case 2:
                ui_utils.clear_console()
                # TODO Gabriel: Implementar register
            case 3:
                break

        if not user:
            continue

        ui_utils.show_banner()

        print(f"Seja bem vindo, {user[1]}!\n")

        while user:
            print("[1] - Listar Eventos")
            print("[2] - Participar de Eventos")
            print("[3] - Gerenciar Eventos")
            print("[4] - Criar Evento")
            print("[5] - Excluir Evento")
            print("[6] - Logout")

            option = ui_utils.get_menu_option("> ", 1, 6)
            if option == -1:
                continue

            ui_utils.clear_console()

            match option:
                case 1:
                    # TODO Gabriel: Implementar Listagem de Eventos
                    pass
                case 2:
                    # TODO Gabriel: Implementar Participar de Eventos
                    pass
                case 3:
                    pass
                case 4:
                    # TODO Gabriel: Implementar criação de evento
                    pass
                case 5:
                    # TODO Gabriel: Implementar remoção de evento
                    # P.S: Só é possível remover eventos que ainda não foram iniciados
                    pass
                case 6:
                    user = None

        ui_utils.show_banner()

    print("Até breve! :-)")


if __name__ == "__main__":
    main()
