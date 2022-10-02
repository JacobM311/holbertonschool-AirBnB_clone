#!/usr/bin/python3
""" cmd line class """


import cmd
import readline


class HBNBCommand(cmd.Cmd):
    """ class for console """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ quit command """
        raise SystemExit

    def do_EOF(self, arg):
        """ exists on EOF """
        raise SystemExit

    def emptyline(self):
        """ do nothing if empty """
        pass

    def do_create(self, arg):


if __name__ == '__main__':
    HBNBCommand().cmdloop()
