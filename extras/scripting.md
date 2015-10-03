<!-- author: Jason Dolatshahi -->

# scripting

Most of the time we write code that we'd like to share or re-use at some point.
This can be done simply using **scripts**. For our purposes, scripts are just files
that contain code (this is true for shell scripts and for a scripting language like
Python. It's not true for lower-level languages like C or Java).

Scripts are text files. We usually append a **file extension** to the script to
indicate the type of code that lives in the script (such as `.sh` or `.py`).
This file extension is mostly for our benefit.

## 1. scripting with bash

Let's create a simple **shell script**. Use your favorite text editor to create
a file that contains the following lines, and save them into a file called
`hello.sh`:

    YOU=`whoami`
    echo "hello $YOU"

Note that **variables** in bash are accessed using the `$` character, just like
environment variables (or any variables) in the Unix shell. Also note the use
of the backticks `` which evaluate the statement they contain.

Now navigate to the same
directory in the Unix terminal and type `bash hello.sh`. You should see a
greeting that refers to you by your username, for example:

    $ bash hello.sh
    hello jason

### shebang

We can streamline the way this script is run by specifying the **interpreter**
`bash` inside the of file, instead of in the run command. This specification
goes in a special statement called the **shebang**.

The shebang goes at the first line of the script, and begins with the
characters `#!`. These characters are followed by the path to the interpreter
that will run the script. For example, `#!/bin/bash` will run the script using
the `bash` program in the `bin` directory.

Our code will be more portable (which is good practice) if we make this specification
more abstract. We can instruct the user's shell to rely on its defaults to
determine the interpreter by replacing the absolute path in the shebang with a reference 
to the user's environment, which can be accessed through `/usr/bin/env`.

For example, the shebang `#!/usr/bin/env bash` runs the script with
the same version of bash that the user would run if they typed `bash` at the
command line.

### executable

Specifying the interpreter with a shebang makes the script self-contained, and
we have to let the file system know that we plan to use it this way. We do this
by changing the
[file
permissions](http://grassbook.org/wp-content/uploads/2015/04/unix_dir.png) with
the `chmod` command:

    $ chmod +x hello.sh

The `+x` syntax tells `chmod` to change the mode (permissions) of this file by
adding the execution bit. This turns our file into a full-fledged
**executable** file, self contained and runnable. Note that the `ls -l`
command will display different file permissions depending on whether this bit is
set or unset; if you've turned it on, you can turn it off again by removing the
execution bit with `chmod -x`.

We run an executable by simply using its name if it's in our search path (for
example, `ls`). We can run it even if it's not in our search path, but then we
have to specify the path directly. The present working directory is specified
with the syntax `./`.

For example, once the shebang is in place and the execution bit is set, you can
run the script like this:

    $ ./hello.sh
    hello jason

## 2. scripting with python

Like shell scripts, Python scripts are text files. Everything we've said about
shebangs and `chmod` holds true here as well; these details relate to how the
operating system treats the file, and don't depend on the code inside the
file.

However there are a couple of additional points to make about the structure and
features of a typical Python script. We'll cover these points as they usually
appear in a script beginning at the top and moving to the bottom.
 
### imports

The shebang goes on the first line as before, and is typically followed by
`import` statements. Remember that we need to import Python library code (like
pandas) in order to make it accessible. There are three ways to import code in
Python:

    import pandas as pd
    from sklearn.linear_model import LogisticRegression as LR
    from ggplot import *

The first method is the most general and the most common. It imports the library
code into its own namespace, specified in this case by the optional shorthand
`pd.` As we've already seen, this allows us to refer to code in this library
with the `pd` prefix.

The second method is common if you only want a subset of the
functionality of the library. In this case the `LogisticRegression` object is
imported into the local namespace under the (again, optional) shorthand name
`LR`. Since `LR` is in our local namespace, no prefix is necessary to access it.

The third (and least common) method is to import code directly into the
local namespace wholesale using the `*` syntax. This method is
frowned upon since it defeats the purpose of namespaces (keeping
logically separate things functionally separate). Its use with the `ggplot`
library is meant to make the syntax resemble `ggplot`'s ancestral R syntax.

### globals  

After the import statements come the global definitions. These are variables
whose values tend not to change, and that we want to be accessible at every
point in the script:

    INPUT_FILE = '~/gits/gads_26/datasets/dinosaurs.tsv'
    FEET_TO_METERS = 0.3048
    DATE_FORMAT = '%Y-%m-%d'

Note that unlike in other languages, Python doesn't give us a way to enforce
the fact that these variables are constant; it's up to us to keep things
straight.

### functions  

Like in many programming languages, our code is typically divided into
functions. Functions are defined with the `def` keyword, take arguments as
input, and (sometimes) return a value:

    def square_plus_one(k):
        return k ** k + 1

An important question that anyone writing code has to deal with is how to
properly divide code into functions. There are many different ways to
do this, and to a certain extent it's a matter of style. However a good rule of
thumb is to make the division of code mirror the division of your task into
logical pieces. An easy way to do this is to start by writing down what
you want to do, for example:

    # load & preprocess data
    # do some manipulations
    # fit model
    # produce output

You'll find that these statements tend to align closely with logical divisions
in your task, and similarly that they give a good indication of how functions
(or sometimes blocks of functions) should be arranged.

### `main`

Again like many programming languages, it's customary in Python to have a
`main` function that contains the main logic that drives your program. The
`main` function can call other functions and maybe do some high-level error
checking, but in general you want it to control the strategic operation of your
code, and ideally you want this to be clearly reflected in its syntactic
structure.

### `if __name__ == ‘__main__’:`

This
[special line](https://docs.python.org/3/library/__main__.html)
occurs in every Python script, and tells Python what to do when the script is
run. It's extremely common to see this pattern at the bottom of a Python
script:

    if __name__ == '__main__':
        main()

This just says that when the script is run, invoke the main function.

Note that the functions and objects you define in one script can be accessed in
another script using `import`. Using this pattern ensures that our
code is
[only](http://ibiblio.org/g2swap/byteofpython/read/module-name.html)
run when we explicitly run it, not when other code calls it with import
statements.

### `pdb`  

A final point to make is about the Python 
[debugger](https://docs.python.org/3.5/library/pdb.html).
This is a built-in interactive debugging tool that can be invaluable for
figuring out what's going on inside your program, how objects are being
changed, how control flow is being handled, etc (though one of the goals of
good programming is to make all of these things as unambiguous as possible,
Python does not enforce good hygiene on us).

It's highly recommended that you take a look at the debugger and at its interactive 
[commands](https://docs.python.org/3.5/library/pdb.html#debugger-commands),
especially as you begin to write more and more complicated scripts. There's
also a version called `ipdb`, which is analogous to `pdb` the same way that
[IPython](http://ipython.org/) is to Python.

### example

The file `hello.py` in this directory mimics the functionality of `hello.sh`
and can be invoked the same way (once the executable bit has been set):

    $ ./hello.py
    hello jason
