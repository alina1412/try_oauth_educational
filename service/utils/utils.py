def verify_password(user, password) -> bool:
    password_in_db = user.get("password")
    if password_in_db == password:
        return True
    return False


def verify_user(user: dict, password: str) -> bool:
    if not user:
        return False
    if not verify_password(user, password):
        return False
    return True
