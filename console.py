#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

classes = ['BaseModel', 'User', 'State',
           'City', 'Amenity', 'Place', 'Review']

def checkme(args):
    arglist = args.split(' ')
    argcount = len(arglist)
    objdict = {}

    if args is '':
        print('** class name missing **')
    elif argcount < 2:
        print('** instance id missing **')
    elif arglist[0] not in classes:
        print("** class doesn't exist **")

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
            return
        elif args not in classes:
            print("** class doesn't exist **")
            return
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args=''):
        '''Prints the string representation of an instance'''
        objtuple = checkme(args)
        if objtuple:
            print(objtuple[0][objtuple[1]])

    def do_quit(self, args):
        '''Quits the program.'''
        raise SystemExit

    def emptyline(self):
            pass

    def help_quit(self):
        print('Quit command to exit the program\n')

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
