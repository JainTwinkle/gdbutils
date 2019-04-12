# Various GDB utils and tricks

## whereis

Find where a given set of addresses are in the proc-maps
of the current inferior process

usage: whereis <addr>

## lfd

List the proc fds of a given pid or the current inferior
process

usage: lfd

## toff

grep the text offset of the given absolute path of executable or shared library

usage: toff <absolute-path-of-executable>
