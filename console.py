#!/usr/bin/python3
"""console module"""
import cmd
import models
from models.base_model import *
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB Class"""
    prompt = "(hbnb) "
    cls_lst = ["Review", "Place", "State",
               "User", "BaseModel", "City", "Amenity"]
    res_att = ["created_at", "updated_at", "id"]

    def do_quit(self, line):
        """escape hatch"""
        return True

    def do_EOF(self, line):
        """end of file message"""
        print("Goodbye")
        return True

    def emptyline(self):
        """empty and pass"""
        pass

    def do_create(self, line):
        """to create"""
        arg_str = line.split()
        if len(arg_str) == 0:
            print("** class name missing **")
            return
        if line not in HBNBCommand.cls_lst:
            print("** class doesn't exist **")
            return
        try:
            cls = eval(line)()
            cls.save()
            print(cls.id)
            return
        except (NameError, AttributeError):
            pass

    def do_show(self, line):
        """to show"""
        if line == "":
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, iid = args[0], args[1]
        if class_name not in HBNBCommand.cls_lst:
            print("** class doesn't exist **")
            return
        objects = models.storage.all()
        key = "{}.{}".format(class_name, iid)
        if key not in objects:
            print("** no instance found **")
            return
        obj = objects[key]
        print(obj)

    def do_destroy(self, line):
        """placeholder"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        cname, uwuid = args[0], args[1]
        if cname not in HBNBCommand.cls_lst:
            print("** class doesn't exist **")
            return
        target = "{}.{}".format(cname, uwuid)
        if target not in storage.all().keys():
            print("** no instance found **")
            return
        stor_rich = storage.all()
        del stor_rich["{}.{}".format(cname, uwuid)]
        storage.save()
        return

    def do_all(self, line):
        """placeholder"""
        if line == "":
            print([str(ii) for ii in storage.all().values()])
            return
        if line in HBNBCommand.cls_lst:
            print([str(ii) for ik, ii in storage.all().items() if line in ik])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """placeholder"""
        args = line.split(maxsplit=3)
        num_args = len(args)
        if num_args < 4:
            if num_args == 0:
                print("** class name missing **")
                return
            elif num_args == 1:
                print("** instance id missing **")
                return
            elif num_args == 2:
                print("** attribute name missing **")
                return
            elif num_args == 3:
                print("** value missing **")
                return
        if args[0] not in HBNBCommand.cls_lst:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        target = storage.all().get(key)
        if target is None:
            print("** no instance found **")
            return
        if args[2] in HBNBCommand.res_att:
            return
        try:
            setattr(target, args[2], eval(args[3]))
        except Exception as er:
            print(er)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
