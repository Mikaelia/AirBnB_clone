#!/usr/bin/python3
'''creation of BaseModel class'''
import uuid
import models
from datetime import datetime


class BaseModel():
    '''BaseModel class'''

    def __init__(self, *args, **kwargs):
        '''Instantiation of BaseModel class

            Args:
                id (str): Assigned a UUID when an instance is created
                created_at (datetime): assigned when an instance is created
                updated_at (datetime): updated each time an instance is changed
            Returns:
                Instance of BaseModel class
        '''
        if (kwargs):
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(
                self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(
                self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''overloads __str__ method'''
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def __repr__(self):
        '''return string representation of object'''
        return self.__str__()

    def save(self):
        '''updates `updated_at` with the current datetime'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''returns dictionary of the instance'''
        mydict = dict(vars(self))
        mydict['__class__'] = self.__class__.__name__
        mydict['created_at'] = self.created_at.isoformat()
        mydict['updated_at'] = self.updated_at.isoformat()
        return mydict
