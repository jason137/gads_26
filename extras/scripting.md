<!-- author: Jason Dolatshahi -->

# scripting

Most of the time we write code that we'd like to share or re-use at some point.
This can be done simply using **scripts**. For our purposes, scripts are just files
that contain code (this is true for shell scripts and for a scripting language like
Python. It's not true for lower-level languages like C or Java).

Scripts are text files. We usually append a **file extension** to the script to
indicate the type of code that lives in the script (such as `.sh` or `.py`).
This file extension is mostly for our benefit.

## scripting in bash

Let's create a simple shell script. Open your favorite text editor and type the
following lines:

    YOU=`whoami`
    echo "hello $YOU"

Save these lines in a file called `hello.sh`. Now navigate to the same
directory in the Unix terminal and type `bash hello.sh`. You should see a
greeting that refers to you by your username, for example:

    $ bash hello.sh
    hello jason

Note that **variables** are accessed using the `$` character, just like
environment variables (or any variables) in the Unix shell. Also note the use
of the backticks `` which evaluate the statement they contain.

We can streamline the way this script is run by specifying the **interpreter**
`bash` inside the of file, instead of in the run command. This specification
goes in a special statement called the **shebang**.

The shebang goes at the first line of the script, and begins with the
characters `#!`. These characters are followed by the path to the interpreter
that will run the script. For example, `#!/bin/bash` will run the script using
the `bash` program in the `bin` directory.

Our code will be more portable (good practice) if we make this specification
more abstract. We can instruct the user's shell to rely on its defaults to
determine the interpreter by replacing the absolute path in the shebang with a reference 
to the user's environment variables, which live in `/usr/bin/env`.

For example, the shebang `#!/usr/bin/env bash` runs the script with
the same version of bash that the user would run if they typed `bash` at the
command line.

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

For example, once the shebang is in place and the execution bit is set, you
should see the following:

    $ ./hello.sh
    hello jason

## python scripting

imports  
globals  
funcs  
`main` func  
`if __name__ == ‘__main__’:`
`ipdb3`  
