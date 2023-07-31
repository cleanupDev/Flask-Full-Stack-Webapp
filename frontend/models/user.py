from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    '''User model'''
    is_active: bool = True
    is_admin: bool = False
    is_verified: bool = True # TODO: change to appropriate default value
    is_authenticated: bool = True # TODO: change to appropriate default value

    username: Optional[str] = None
    id: Optional[int] = None
    password: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    created_at: Optional[str] = None
    
    def get_id(self):
        return self.id
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at,
            'is_active': self.is_active,
            'is_admin': self.is_admin,
            'is_verified': self.is_verified,
            'is_authenticated': self.is_authenticated
        }