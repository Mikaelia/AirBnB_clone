#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


classes = ['BaseModel']

class HBNBCommand(cmd.Cmd):

    def do_create(self, args):
        if not args:
            print('** class name missing **')
        if args not in classes:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)


    def do_quit(self, args):
        """Quits the program."""
        raise SystemExit

    def emptyline(self):
            pass

    def help_quit(self):
        print('Quit command to exit the program\n')
if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
