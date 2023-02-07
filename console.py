#!/usr/bin/python3
"""console mdule"""
import cmd


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
