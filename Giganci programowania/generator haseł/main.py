import random
import string

def generate_strong_password(length=16):
    """Generuje jedno bardzo silne hasło."""
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)):
            return password

def generate_passwords(count=5, length=16):
    """Generuje wiele silnych haseł."""
    return [generate_strong_password(length) for _ in range(count)]

# Przykładowe użycie:
if __name__ == "__main__":
    ile = int(input("[❓] Ile haseł wygenerować? "))
    dlugosc = int(input("[❓] Długość każdego hasła? (np. 16): "))
    hasla = generate_passwords(ile, dlugosc)
    for i, h in enumerate(hasla, 1):
        print(f"[✅] Hasło {i}: {h}")

    input("\nNaciśnij Enter, aby zakończyć...")
