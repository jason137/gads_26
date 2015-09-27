## anaconda installation 
Anaconda is a (free) wrapped Python distribution, meaning it comes with a
number of libraries pre-installed. The installation process is pretty
straightforward (instructions below for Mac OS X):

- click here for installer (python3.4): http://continuum.io/downloads#py34 
- download installer, double-click .pkg file
- follow installation wizard

**Heads up!** This installation edits your system
[search path](https://www.decf.berkeley.edu/help/unix/searchpath.html). You can
see this using any of these steps:
- `echo $PATH`
- `which python`
- look at your `~/.profile` file

If you don't like this, you can revert the change & create a separate shortcut
to Anaconda:
- edit `~/.profile`
- create a symbolic link with `ln -s` (see `man ln` for help) 
