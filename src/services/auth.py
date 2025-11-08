from utils import validators_utils, password_utils
from data import user


def login(email: str, password: str) -> bool:
    try:
        if not validators_utils.is_email_valid(email):
            print("O E-mail fornecido é inválido.")
            return False

        password_status = validators_utils.get_password_status(password)
        if password_status:
            print(f"A senha fornecida é inválida: {password_status}")
            return False

        user_password = user.fetch_user_password(email)
        return password_utils.verify_password(password, user_password)
    except Exception as e:
        print(e)
        return False
    

def register() -> bool:
    # TODO Gabriel: Implementar função.
    pass
