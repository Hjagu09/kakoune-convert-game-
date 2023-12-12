kakoune-convert
===============

A small game around the
[kakoune text editor](https://kakoune.org/) and file
format convertions. Currently there are only four
levels, but i might add more some time. If you want to
feel free to submit a pull request with a new level :smile:

background
----------

I got the idea for this game while messing with the input
data for a challenge in [advent of code](https://adventofcode.com/).
Doing that i came to think of how amazig kakoune is for that
task and so i made an game.


installation
------------

1. clone this repo
2. (optional) add src/cli to your path so you can run the
   game as a regular command. If your
   using fish you can do it like so:
   ```sh
   # run this in fish from the root of the repo
   fish_add_path ./src/cli
   ```
3. you should now be abel to run the game.
   ```sh
   # if you did step two
   kak_converts

   # if you didn't do step two
   ./src/cli/kak_converts
   ```

command line usage
------------------
```
usage: kak_converts [-h] {play,list} ...

positional arguments:
  {play,list}
    play       play a level
    list       list all levels

options:
  -h, --help   show this help message and exit
```
