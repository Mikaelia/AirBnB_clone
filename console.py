#!/usr/bin/python3
'''Console module'''
import cmd
from models.base_model import BaseModel
from models import storage

classes = ['BaseModel', 'User', 'State',
           'City', 'Amenity', 'Place', 'Review']


def checkme(args, name=''):
    '''Checks for correct arguments, returns object dict'''
    arglist = args.split(' ')
    argcount = len(arglist)

    if argcount:
        class_name = arglist[0]
    if not class_name:
        print('** class name missing **')
    elif class_name not in classes:
        print("** class doesn't exist **")
    elif name == 'create':
        return
    elif argcount < 2:
        print('** instance id missing **')
    elif name == 'update' and argcount < 4:
        if argcount < 3:
            print('** attribute name missing **')
        else:
            print('** value missing **')
    else:
        objdict = storage.all()
        key = '{}.{}'.format(class_name, arglist[1])
        if key in objdict.keys():
            return (objdict, key)
        else:
            print('** no instance found **')
            return


class HBNBCommand(cmd.Cmd):
    '''Console class'''
    def do_create(self, args):
        '''creates model instance'''
        checkme(args, 'create')
        if args == 'BaseModel':
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
        arglist = args.split(' ')

        if not arglist[0] or arglist[0] in classes:
            objdict = storage.all()
            for k, v in objdict.items():
                objlist.append(v)
            print(objlist)
        else:
            print("** class doesn't exist **")

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
        key = arglist[2]
        newval = arglist[3]

        objtuple = checkme(args, 'update')
        if objtuple:
            myobjdict = vars(objtuple[0][objtuple[1]])
            if key in myobjdict:
                val = myobjdict[key]
                cast_val = type(val)(newval)
                myobjdict[key] = cast_val
            else:
                myobjdict[key] = newval
            storage.save()

    def emptyline(self):
        '''Reasserts prompt on empy input'''
        pass

    def help_quit(self):
        '''Outlines quit usage'''
        print('Quit command to exit the program\n')


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
