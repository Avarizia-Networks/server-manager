import hashlib

from database.database import Database

db = Database("database")


def check_password(password: str):
    """function to check the given password against the password hash"""
    generated_hash = create_password(password)
    
def hash_password(password: str):
    """function to create a password hash from the given password"""
    encoded_password = password.encode("utf-8")
    password_hash = hashlib.sha3_512(encoded_password)
    second_hash = hashlib.sha3_512(password_hash.hexdigest().encode("utf-8"))
    return second_hash.hexdigest()

if __name__ == "__main__":
    print(create_password("test"))