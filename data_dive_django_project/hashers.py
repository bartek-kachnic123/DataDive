from django.contrib.auth.hashers import PBKDF2PasswordHasher


class PBKDF2PasswordHasherDouble(PBKDF2PasswordHasher):
    iterations = PBKDF2PasswordHasher.iterations * 2
