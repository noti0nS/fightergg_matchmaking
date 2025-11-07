import re


def is_email_valid(email: str) -> bool:
    rgx = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    return rgx.match(email) is not None


def get_password_status(password: str) -> str | None:
    if len(password) < 6:
        return "Senha muito curta. Deve ter pelo menos 6 caracteres."
    if not re.search(r"[A-Z]", password):
        return "Senha deve conter pelo menos uma letra maiúscula."
    if not re.search(r"[a-z]", password):
        return "Senha deve conter pelo menos uma letra minúscula."
    if not re.search(r"[0-9]", password):
        return "Senha deve conter pelo menos um número."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Senha deve conter pelo menos um caractere especial."
    return None
