#!/usr/bin/python3
'''creation of BaseModel class'''
import uuid
import datetime

class BaseModel():
    '''BaseModel class'''
    def __init__(self, id=None, created_at=None, updated_at=None):
        '''Instantiation of BaseModel class

            Args:
                id (str): Assigned a UUID when an instance is created
                created_at (datetime): assigned when an instance is created
                updated_at (datetime): assigned/updated each time an instance is created/changed
            Returns:
                Instance of BaseModel class
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    def __str__(self):
        '''overloads __str__ method'''
        return("[{}] ({}) {}".format(self.__class__, self.id, self.__dict__))
    def save(self):
        '''updates `updated_at` with the current datetime'''
        self.updated_at = datetime.datetime.now()
    def to_dict(self):
        '''returns dictionary of the instance'''
        self.__dict__['__class__'] = self.__class__.__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__

