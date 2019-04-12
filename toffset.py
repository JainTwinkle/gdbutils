#!/usr/bin/python
"""GDB lfd command

List the proc fds of a given pid or the current inferior
process

To use this command, source it into your .gdbinit file:
   source /path/to/lfd.py
"""

import gdb

class Toffset(gdb.Command):
    """List the proc fds
    Usage: whereis [pid]
Prints the proc fd listing of the process with the given pid, or
prints the proc fd listing of the current inferior process if
no pid was specified.
    """

    def __init__(self):
        super(Toffset, self).__init__("toff", gdb.COMMAND_USER)

    def get_text_offset(self, path):
        """Returns the proc fd listing of the process with the given pid"""
        return gdb.execute("shell readelf -S "+ path +" | grep \.text",
                           False,
                           True)

    def invoke(self, arg, from_tty):
        """Invoked when the command is executed from GDB"""
        args = gdb.string_to_argv(arg)
        cur_proc = gdb.selected_inferior()
        if not cur_proc.is_valid() and len(args) == 0:
            return
        if len(args) > 0:
            path = args[0]
        out = self.get_text_offset(path)
        if from_tty:
            print(out, end="")
        return out
Toffset()
