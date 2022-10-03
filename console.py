#!/usr/bin/python3
""" cmd line class """


import cmd
import readline
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage



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
