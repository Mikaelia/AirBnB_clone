#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print("Hello, {}".format(name))

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
