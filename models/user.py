from dataclasses import dataclass

@dataclass
class Userino:
    id: int
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
    is_authenticated: bool
    
    def get_id(self):
        return self.id
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
            "is_authenticated": self.is_authenticated
        }