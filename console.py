#!/usr/bin/python3
"""console mdule"""
import cmd
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
    prompt = '(hbnb) '

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
