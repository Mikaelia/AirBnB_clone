# AirBnb Clone Command Interpreter
The goal for this project was to build a command line interpreter that can :
- Put in place a parent class to take care of the initialization, serialization and deserialization of future instances
- Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON strin <-> file
- Create all classes used for AirBnb (User, State, City, Place..) 
- Create the first abstracted storage engine of the project: File Storage
- Create all unittests to validate all our classes and storage engine

### Command Interpreter
The command interpreter should be capable of:
- Creating a new object
- Retrieving an object from a file, a database, etc...
- Doing operations on objects
- Updating attributes of an object
- Destroying an object

### Project Goals
- Create a Python package
- Create a command interpreter in Python using the cmd module
- Implement unit testing at a large scale
- Serialize and deserialize a Class
- Write and read a JSON file
- Manage datetime
- Define a UUID
- Know how to use \*args and \*\*kwargs
- Know how to handle named arguments in a function

### Directory Descriptions
| Directory | Description |
| ------------- |:-------------:|
| models | contains all models |
| engine | contains file_storage module to interact with data |
| tests | contains all unit tests |

### File Descriptions
| File | Description |
| ------------- |:-------------:|
| console.py | entry point of the command interpreter |
| base_model.py | contains class BaseModel that defines all common attributes/methods for other classes |
| file_storage.py | contains class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances|
| init.py | within models, links BaseModel to FileStorage through the variable storage |

### Command Line Commands
| Command | Description |
| ------------- |:-------------:|
| help | lists all documented commands |
| exit | exits the console |
| EOF | exits the console |
| all | Prints all string representations of all instances based or not on the class name |
| create | Creates a new instance of BaseModel and saves it to the JSON file |
| destroy | Deletes an instance based on the class name and id |
| show | Prints the string represenation of an instance based on the class name and id |
| update | Updates an instance based on the class name and id by adding or updating attribute |

### Installation
``` ./hsh
git clone git@github.com:Mikaelia/AirBnB_clone.git
```

### Command Line Usage
``` ./hsh
**create** - create <class name>
**show** - show <class name> <id>
**destroy** - destroy <class name> <id>
**all** - all or all <class name>
**update** - update <class name> <id> <attribute name> "<attribute value">
**quit** - quit
```

### Examples
``` ./hsh
$ ./console.py
(hbnb) 
(hbnb) help

Documented commands (type help <topic>):
========================================
all  create  destroy  help  quit  show  update

(hbnb) create BaseModel
1cf88285-079b-4f35-81c6-5535e231aaeb

(hbnb) show BaseModel 1cf88285-079b-4f35-81c6-5535e231aaeb
[BaseModel] (1cf88285-079b-4f35-81c6-5535e231aaeb) {'updated_at': datetime.datetime(2018, 6, 12, 22, 26, 12, 803233), 'id': '1cf88285-079b-4f35-81c6-5535e231aaeb', 'created_at': datetime.datetime(2018, 6, 12, 22, 26, 12, 803196)}

(hbnb) update BaseModel 1cf88285-079b-4f35-81c6-5535e231aaeb email "thisisanexample@gmail.com

(hbnb) show BaseModel 1cf88285-079b-4f35-81c6-5535e231aaeb
[BaseModel] (1cf88285-079b-4f35-81c6-5535e231aaeb) {'id': '1cf88285-079b-4f35-81c6-5535e231aaeb', 'updated_at': datetime.datetime(2018, 6, 12, 22, 26, 12, 803233), 'email': '"thisisanexample@gmail.com', 'created_at': datetime.datetime(2018, 6, 12, 22, 26, 12, 803196)}

(hbnb) all
[[BaseModel] (d29e08db-73a0-47c3-90b8-8e8986dc4a5d) {'updated_at': datetime.datetime(2018, 6, 12, 22, 26, 42, 978598), 'id': 'd29e08db-73a0-47c3-90b8-8e8986dc4a5d', 'created_at': datetime.datetime(2018, 6, 12, 22, 26, 42, 978575)}, [BaseModel] (1cf88285-079b-4f35-81c6-5535e231aaeb) {'id': '1cf88285-079b-4f35-81c6-5535e231aaeb', 'updated_at': datetime.datetime(2018, 6, 12, 22, 26, 12, 803233), 'email': '"thisisanexample@gmail.com', 'created_at': datetime.datetime(2018, 6, 12, 22, 26, 12, 803196)}]
[[BaseModel] (d29e08db-73a0-47c3-90b8-8e8986dc4a5d) {'updated_at': datetime.datetime(2018, 6, 12, 22, 26, 42, 978598), 'id': 'd29e08db-73a0-47c3-90b8-8e8986dc4a5d', 'created_at': datetime.datetime(2018, 6, 12, 22, 26, 42, 978575)}, [BaseModel] (1cf88285-079b-4f35-81c6-5535e231aaeb) {'updated_at': datetime.datetime(2018, 6, 12, 22, 26, 12, 803233), 'id': '1cf88285-079b-4f35-81c6-5535e231aaeb', 'created_at': datetime.datetime(2018, 6, 12, 22, 26, 12, 803196)}]
```

#### Authors
Mikaela Gurney, Lisa Olson
