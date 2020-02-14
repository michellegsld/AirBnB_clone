#!/usr/bin/python3
""" Entry point for command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program """
        if arg == 'quit':
            self.close()
        return True

    def do_EOF(self, arg):
        """ End of file command to exit the program """
        if arg == 'EOF':
            self.close()
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
