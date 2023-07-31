from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    '''User model'''
    
    id: Optional[int] = None
    username: str
    password: Optional[str] = None
    email: Optional[str] = None
    created_at: Optional[str] = None
    is_active: bool = True
    is_admin: bool = False
    is_verified: bool = True # TODO: change to appropriate default value
    is_authenticated: bool = True # TODO: change to appropriate default value
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'created_at': self.created_at,
            'is_active': self.is_active,
            'is_admin': self.is_admin,
            'is_verified': self.is_verified,
            'is_authenticated': self.is_authenticated
        }