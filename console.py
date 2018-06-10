#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

classes = ['BaseModel', 'User', 'State',
           'City', 'Amenity', 'Place', 'Review']

def checkme(args, name=''):
    arglist = args.split(' ')
    argcount = len(arglist)
    objdict = {}

    if args is '':
        print('** class name missing **')
    elif argcount < 2:
        print('** instance id missing **')
    elif arglist[0] not in classes:
        print("** class doesn't exist **")
    elif name == 'update' and argcount < 4:
        if argcount < 3:
            print('** attribute name missing **')
        else:
            print('** value missing **')
    else:
        objdict = storage.all()
        key = '{}.{}'.format(arglist[0], arglist[1])
        if key in objdict.keys():
            return (objdict, key)
        else:
            print('** no instance found **')


class HBNBCommand(cmd.Cmd):

    def do_create(self, args):
        if not args:
            print('** class name missing **')
        elif args not in classes:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args=''):
        '''Prints the string representation of an instance'''
        objtuple = checkme(args)
        if objtuple:
            print(objtuple[0][objtuple[1]])

    def do_all(self, args=''):
        '''Prints all stored object instances'''
        objlist = []
        if args and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            objdict = storage.all()
            for k, v in objdict.items():
                objlist.append(v)
            print(objlist)

    def do_quit(self, args=''):
        '''Quits the program.'''
        raise SystemExit

    def do_destroy(self, args=''):
        '''Destroys an instance and updates JSON file'''
        objtuple = checkme(args)
        if objtuple:
            del objtuple[0][objtuple[1]]
            storage.save()
    def do_update(self, args):
        '''Updates an instance/JSON file by adding or updating attribute'''
        arglist = args.split(' ')
        objtuple = checkme(args, 'update')
        key = arglist[2]
        newval = arglist[3]
        if objtuple:
            myobjdict = vars(objtuple[0][objtuple[1]])
            if key in myobjdict:
                val = myobjdict[key]
                cast_val = type(val)(newval)
                myobjdict[key] = cast_val
            else:
                myobjdict[key] = newval
            storage.save()
            print(myobjdict)

    def emptyline(self):
            pass

    def help_quit(self):
        print('Quit command to exit the program\n')

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
