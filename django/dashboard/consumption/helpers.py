import secrets
import string

# ランダムなトークンを生成する
def generate_random_token(length=32):
    characters = string.ascii_letters + string.digits
    return ''.join(secrets.choice(characters) for _ in range(length))
