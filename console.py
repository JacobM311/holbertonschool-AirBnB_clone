#!/usr/bin/python3
""" cmd line class """
import cmd
import readline

class HBNBCommand(cmd.Cmd):
    """ class for console """
    prompt = "(hbnb) "

    def quit(self, arg):
        """ quit command """
        raise SystemExit

    def EOF(self, arg):
        """ exists on EOF """
        raise SystemExit

    def emptyline(self):
        """ do nothing if empty """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
