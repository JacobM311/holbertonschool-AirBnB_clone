#!/usr/bin/python3
""" cmd line class """


import cmd
import readline
import json
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
classes = {"BaseModel": BaseModel,
           "User": User,
           "State": State,
           "Ctiy": City,
           "Amenity": Amenity,
           "Place": Place,
           "Review": Review
           }


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
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) 
        and prints the id. Ex: $ create BaseModel
        """
        alist = arg.split(" ")
        if len(alist[0]) == 0:
            print("** class name missing **")
        elif alist[0] not in classes.keys():
            print("** class doesn't exist **")
        else:
            creation = classes[alist[0]]()
            creation.save()
            print(creation.id)

    def do_show(self, arg):
        """ 
        Prints the string representation of an instance based 
        on the class name and id 
        """
        slist = arg.split(" ")
        if len(arg) == 0:
            print("** class name missing **")
        elif slist[0] not in classes.keys():
            print("** class doesn't exist **")
        elif len(slist) < 2:
            print("** instance id missing **")
        else:
            FindObj = slist[0] + "." + slist[1]
            AllObj = storage.all()
            item = AllObj.get(FindObj)
            if item is None:
                print("** no instance found **")
            else:
                print(item)

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or 
        not on the class name.
        """
        myDict = storage.all()
        ObjList = []
        if len(arg) == 0:
            for obj in myDict:
                item = myDict.get(obj)
                ObjList.append(str(item))
        else:
            StrList = arg.split(" ")
            if StrList[0] not in classes.keys():
                print ("** class doesn't exist **")
                return
            else:
                for obj in myDict:
                    if StrList[0] in obj:
                        item = myDict.get(obj)
                        ObjList.append(str(item))
        print(ObjList)





if __name__ == '__main__':
    HBNBCommand().cmdloop()
