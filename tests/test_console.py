#!/usr/bin/python3

"""
test for console to make it start working
"""

import unittest
from io import StringIO
import sys
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test suite for the HBNBCommand class"""

    def setUp(self):
        self.orig_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.orig_stdout

    def test_command_docstrings_exist(self):
        """Check if command method docstrings exist"""
        commands = [
            HBNBCommand.do_quit,
            HBNBCommand.do_create,
            HBNBCommand.do_show,
            HBNBCommand.do_destroy,
            HBNBCommand.do_all,
            HBNBCommand.do_update
        ]

        for command in commands:
            self.assertIsNotNone(command.__doc__,
                                 f"Docstring missing for {command.__name__}")

    def test_create_error_messages(self):
        """Test error messages for the 'create' command"""
        cmd = HBNBCommand()

        cmd.do_create('mymodel')
        self.assertEqual(sys.stdout.getvalue(),
                         "** class doesn't exist **\n")

        sys.stdout = StringIO()
        cmd.do_create("base")
        self.assertEqual(sys.stdout.getvalue(),
                         '** class doesn\'t exist **\n',
                         "Non-existent class message")


if __name__ == "__main__":
    unittest.main()
