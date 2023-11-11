import hashlib

from database.database import Database

users = Database("users")

def generate_password_hash(password: str):
    """function to create a password hash from the given password"""
    encoded_password = password.encode("utf-8")
    password_hash = hashlib.sha3_512(encoded_password)
    second_hash = hashlib.sha3_512(password_hash.hexdigest().encode("utf-8"))
    return second_hash.hexdigest()

def load_user(id: int) -> dict:
    """load the user from the database
    
    Format:
    id = {
        username: str,
        groups: list,
        password: str, (hashed)
        mail: str,
        main_group: str
    }
    """
    return users.get_value(id)

class User:
    def __init__(self, id: int):
        userdata = load_user(id)
        
        self.username = userdata["username"]
        self.groups = userdata["groups"]
        self.password = userdata["password"]
        self.mail = userdata["mail"]
        self.main_group = userdata["main_group"]
        
    def add_group(self, group: str):
        """add a group to the user"""
        self.groups.append(group)
        
    def remove_group(self, group: str):
        """remove a group from the user"""
        self.groups.remove(group)
        
    def get_groups(self):
        """return the groups of the user"""
        return self.groups
    
    
    def set_username(self, username: str):
        """set the username of the user"""
        self.username = username
    
    def get_username(self):
        """return the username of the user"""
        return self.username
    
    
    def set_password(self, password: str):
        """set the password of the user"""
        self.password = generate_password_hash(password)
        
    def get_password(self):
        """return the password hash of the user"""
        return self.password
    
    
    def set_mail(self, mail: str):
        """set the mail of the user"""
        self.mail = mail
        
    def get_mail(self):
        """return the mail of the user"""
        return self.mail
        
        
    def set_main_group(self, group: str):
        """set the main group of the user"""
        self.main_group = group
        
    def get_main_group(self):
        """return the main group of the user"""
        return self.main_group
    
    
    def check_password(self, password: str):
        """check the given password against the password hash"""
        password_hash = generate_password_hash(password)
        return password_hash == self.password
    
    def save(self):
        """save the user to the database"""
        users.set_value(self.username, self)
    
        
        

