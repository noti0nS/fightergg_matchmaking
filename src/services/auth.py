from utils import validators_utils, password_utils
from data import user


def login(email: str, password: str) -> tuple | None:
    try:
        if not validators_utils.is_email_valid(email):
            print(
                "As credencias estão inválidas! Verifique se o e-mail e a senha foram digitados corretamente."
            )
            return None

        password_strength_result = validators_utils.validate_password_strength(password)
        if password_strength_result:
            print(password_strength_result)
            return None

        user_data = user.get_user_by_email(email)
        if not password_utils.verify_password(password, user_data[2]):
            print(
                "As credencias estão inválidas! Verifique se o e-mail e a senha foram digitados corretamente."
            )
            return None

        return (user_data[0], user_data[1]) # Retorna apenas o id e nickname.
    except Exception as e:
        print(e)


def register() -> bool:
    # TODO Gabriel: Implementar função.
    pass
