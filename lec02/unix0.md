<!-- author: Jason Dolatshahi -->

## basic Unix warmup

These are the Unix bunny slopes. It doesn't hurt to start here.

## 0. preamble

Make sure you're careful when you're working at the command line. **There is no undo!**

Remember that you can access the operating system's built-in **documentation**
for any Unix program via the `man` page. For example, `man less` will show you
the `less` docs. Use the up & down arrows to navigate (`fn` up/down to page up/down),
and close the docs with `q`. 

You can type `ctrl-L` to clear your screen in the terminal, and `ctrl-C` to
cancel the current line of input and move to a new line. Also, `cmd` plus
the left/right arrow keys allow you to jump to the beginning/end of an active prompt.

Also note that the `$` symbol below refers to the Unix command prompt.

## 1. looking at things

The application you use to issue Unix commands is called a **terminal**. Mac OS
X has a default application, called Terminal, or you can download a more
customizable alternative [here](https://www.iterm2.com/) if you're interested.

The terminal exposes the **command prompt**, which is a text-based interface you
use to communicate with the system **shell**. The
shell is the "outer part" of the operating system, and the part you typically
interact with. The shell communicates with the "inner part" of the operating
system, called the **kernel**, which is the the part that handles low-level tasks and
interacts with the hardware components of your computer. Your interaction with
the kernel is typically always indirect, through the shell.

Let's start with something reassuring:

    $ whoami
    jason

The commands you issue in the terminal are run in the context of a login
**session**, and the `whoami` command shows the username that corresponds to
the active session.
Sometimes it can be necessary to
[switch users](https://linuxacademy.com/blog/linux/linux-commands-for-beginners-sudo/)
in order to perform certain tasks. We don't need to talk much about this here.

Like a GUI window, the command line gives you an interface to the 
[file system](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
of your computer. Your present location in the file system is called your
**working directory**. To see where in the file system you are (eg to see your
present working directory), use `pwd`:

    $ pwd
    /Users/jason

Usually a new terminal session begins in your **home directory**. Frequently
the home directory is referred to by the 1-character nickname `~`. If you're in
another directory, you can change to the home directory using the `cd` command:

    $ cd

Entering `cd` with no input always brings you to your home directory.

The `ls` command lists the contents of a directory:

    $ ls
    Applications    Downloads       Movies          Public          gits
    Desktop         Dropbox         Music           anaconda        Documents
    Documents       Library         Pictures        genomics

You can get more information about these files by changing the way you invoke the
`ls` program. Many Unix programs take arguments called **flags** that can alter
their behavior. For example, passing the `-l` flag to `ls` shows us the
contents of our directory in long form.

    $ ls -l
    drwx------   3 jason  staff   102 Jun 28  2014 Applications
    drwx------+  9 jason  staff   306 Sep 27 16:19 Desktop
    drwx------+ 28 jason  staff   952 Sep 25 22:35 Documents
    drwx------+ 29 jason  staff   986 Sep 26 16:59 Downloads
    drwx------@ 76 jason  staff  2584 Sep 25 22:35 Dropbox
    drwx------@ 54 jason  staff  1836 Sep 18 10:57 Library
    drwx------+  3 jason  staff   102 Aug 22  2013 Movies
    drwx------+  8 jason  staff   272 Sep 18 10:55 Music
    drwx------+ 21 jason  staff   714 Sep 22 15:55 Pictures
    drwxr-xr-x+  5 jason  staff   170 Mar 22  2014 Public
    drwxr-xr-x   3 jason  staff   102 Sep 23 15:25 anaconda
    drwxr-xr-x   5 jason  staff   170 May  1  2014 genomics
    drwxr-xr-x   9 jason  staff   306 Sep 23 15:53 gits


## 2. making things

We can make a new directory using the `mkdir` command. Make a new directory in
your home directory called `tmp`, and then navigate to that directory with the
`cd` command.

    $ mkdir tmp
    $ cd tmp

If you issue the `ls` command from inside `tmp` you should see no output,
because this directory is empty. We can make a new file using `echo`:

    $ echo 'ciao mondo' > file1

The `echo` command simply prints its output to your screen. The `>` in the
command above **redirects** the output into `file1`. If you try this again with
a different input string, you'll see that it overwrites the original contents
of `file1`. The `>>` redirect operator solves this problem by appending its
output to the target file instead of overwriting.

Now that you've created `file1`, listing the directory contents will produce this new
file's name as output.

    $ ls
    file1

Copy the file using the `cp` command:

    $ cp file1 file2

This copies the contents of `file1` into a new file called `file2`. We can
print the contents of a file to the screen using the `cat` command:

    $ cat file1
    ciao mondo

    $ cat file*
    ciao mondo
    ciao mondo

Notice the use of the `*` character in the input to `cat` above. This character
is a **wildcard** that tells `cat` to print all files in the current directory
whose filenames begin with "file" (eg both `file1` and `file2`).

You can remove a file with the `rm` command. This is one program that you 
have to be careful with, because in general when you delete data at the command
line it is not retrievable. **Beware**!

    $ ls
    file1   file2

    $ rm file2
    $ ls
    file1

We can rename our file by moving it into a new file with `mv`:

    $ mv file1 file0
    $ ls
    file0

## 3. navigating the file system

You can think of navigating through the directories in your file system like
moving between nodes in a tree. This would be difficult in practice if you had to
explicitly specify your target node every time you wanted to move, but fortunately there
are some shortcuts that allow us to issue navigation commands relative to our
current node (eg, relative to the directory you're currently in).

Starting from the `~/tmp` directory, you can navigate up one directory using `..`:

    $ pwd
    /Users/jason/tmp

    $ cd ..
    $ pwd
    /Users/jason

The `-` input to `cd` navigates to the previous working directory, regardless
of its position in the file system hierarchy:

    $ pwd
    /Users/jason/tmp

    $ cd ..
    $ pwd
    /Users/jason

    $ cd -
    /Users/jason/tmp

We can delete the `tmp` directory and all its contents using the `rm` command,
but again this is one command that is worth being **careful** with:

    $ rm -r tmp

The `-r` flag instructs `rm` to remove the directory and its contents
recursively. This doesn't work for empty directories though; to remove an empty
directory use the `rmdir` command:

    $ mkdir tmp2
    $ rmdir tmp2

## 4. the search path

An important attribute of your Unix session is the system **search path** it
corresponds to. The search path is a string that represents the directories
that your system checks (in order) when you issue a command at the prompt.

For example, typing `ls` at the prompt does something rather than nothing
because the `ls` program exists somewhere in your search path. To see where
exactly, use the `which` program:

    $ which ls
    /bin/ls

This output shows you that when you issue `ls` at the prompt, the shell accesses
the file that `/bin/ls` refers to.

Alternatively, if you enter a command that doesn't exist on the search path,
you will see an error:

    $ nogood
    -bash: nogood: command not found

    $ which nogood

As you can see, there is no program called `nogood`, and the `which` command
generates no output. Notice the reference to `bash` above. This refers to the
particular shell
[software](http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x143.html)
that's running my session.

You can see the full system search path by accessing the **environment
variable** that stores it. Environment variables are just variables that the
Unix environment (eg, the operating system) can access. You can see all of them
with the `env` command, or access specific variables using `$`.

The system search path lives in an environment variable called `PATH`:

    $ echo $PATH
    /usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/TeX/texbin:/usr/local/sbin

As you can see, this is just a `:`-delimited string of directories.

Programs that belong to your operating system typically live in places like `/usr/bin/`,
`/bin`, etc. It's good practice to avoid interfering with the contents of these
directories. Third-party software is customarily installed into `/usr/local/`.
Putting `/usr/local/bin` ahead of `/usr/bin` in your system path gives preference to
user-specified software in cases where multiple versions of a program exist.

This has been a pretty quick overview, but hopefully you agree at this point that
basic use of the Unix command line is not impossible. But there is more to
it than this, and you should take a look at the other Unix tutorials in this repo
to go further with data exploration at the command line.

## postscript

Some Unix programs take longer than others to master, but you'll find that the
investments of time you make will bring incredible gains in productivity. Be patient, 
search the internet for answers, discuss with your classmates, and ask lots of
questions.

One example of a steep learning curve is a text editor called `vim`, which you 
may find counterintuitive at first, but which pays dividends as you gain
[experience](http://vim-adventures.com/).
