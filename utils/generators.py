import time
import random
import string

def gen_email(prefix="user"):
    ts = int(time.time() * 1000)
    return f"{prefix}{ts}@yopmail.com"

def gen_password(length=8):
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choice(alphabet) for _ in range(length))

