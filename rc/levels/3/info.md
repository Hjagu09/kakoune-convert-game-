Level three
===========

background
----------

NOTE: for this level you will need the tool hexdump
or something that does the same thing.

Computers work in binary. Binary is a very scary
format so if humans have to interact with it we
generally encode it as **hexadecimal** (aka "hex").
This format is a lot easier to read, and we will be
working with it here. For the purpose of this level
we dump files as hex on the command line using:

```sh
hexdump -v file
```

challange
---------

given some input, you should convert it to hexadecimal
and **remove all digits** 0 - 9. This will give you a
string of letters A - F. Make sure all letters are
**uppercase** and then you have your solution.

example
-------

### input
```python
2*-1
```

### hexadecimal
```hex
2a31 312d 000a
```

### solution
```
ADA
```
