# data exploration at the command line

This introduction is meant to cover some basic exploratory steps to carry out when you
see a dataset for the first time.

## 0. preamble
Make sure you're careful when you're working at the command line. **There is no undo!**

Remember that you can access the operating system's built-in **documentation**
for any Unix program via the `man` page. For example, `man less` will show you
the `less` docs. Use the up & down arrows to navigate (`fn` up/down to page up/down),
and close the docs with `q`. 

Datasets usually live in files, and sometimes we think of them like
[relational tables](http://www.w3schools.com/sql/sql_intro.asp)
(or spreadsheets), but each of these nouns comes with its own jargon
attached. You may find this **vocabulary** chart helpful as you go through the exercise:

<table>
    <tr>
        <th>file
        <th>relational table
        <th>dataset
    <tr>
        <td>line
        <td>row
        <td>record
    <tr>
        <td>field
        <td>column
        <td>feature
</table>

Also note that the `$` character below denotes the Unix **command prompt**.

Now that you're ready to go, start by
[cloning](https://guides.github.com/activities/hello-world/) this
[repo](https://github.com/jason137/gads_26)
and navigating to the `datasets` directory. Let's make sure we're in the right place.

    $ pwd
    /Users/jason/gits/gads_26/datasets

The `pwd` command shows you the present working directory, which means the
directory you're in. You probably won't see the "jason/gits" part, but the rest should
be reasonably close, especially if you're using a Mac.

## 1. first steps
Let's have a look around.

    $ ls
    Fischer.pgn             citibike.csv            gdp.csv                 shakespeare.tsv
    anscombe.tsv            citibike.json           meteorite.csv           snowfall.tsv
    beer.tsv                coffee.tsv              nyc_parks.tsv           state_hts.tsv
    central_park_temps.txt  epl.csv                 presidents.tsv          student_profiles.tsv

The `ls` command lists the directory contents, and passing the `-l` flag to
`ls` gives you more detailed information (including permissions, owner &
group, size, date modified, and filename).

    $ ls -l
    total 11784
    -rwxr-xr-x@ 1 jason  staff   550330 Jan  6  2008 Fischer.pgn
    -rw-r--r--@ 1 jason  staff      424 Sep 24 13:03 anscombe.tsv
    -rw-r--r--  1 jason  staff    19771 Sep 18 18:24 beer.tsv
    -rw-r--r--  1 jason  staff    11198 Sep 23 11:59 central_park_temps.txt
    -rw-r--r--  1 jason  staff    32591 Sep 24 12:38 citibike.csv
    -rw-r--r--  1 jason  staff   119312 Sep 24 12:38 citibike.json
    -rw-r--r--@ 1 jason  staff     2059 Sep 18 10:41 coffee.tsv
    -rw-r--r--  1 jason  staff    14656 Sep 23 21:24 epl.csv
    -rwxr-xr-x@ 1 jason  staff   192523 Sep 18 11:31 gdp.csv
    -rw-r-----@ 1 jason  staff  4976164 Sep 20 19:04 meteorite.csv
    -rw-r--r--@ 1 jason  staff    72519 Sep 20 18:30 nyc_parks.tsv
    -rw-r--r--  1 jason  staff     3536 Sep 19 15:32 presidents.tsv
    -rw-r--r--@ 1 jason  staff      816 Sep  4  2014 shakespeare.tsv
    -rw-r--r--  1 jason  staff      314 Sep 23 20:14 snowfall.tsv
    -rw-r--r--  1 jason  staff     1454 Sep 17 21:48 state_hts.tsv
    -rw-r--r--@ 1 jason  staff      224 Sep 23 19:06 student_profiles.tsv

We'll take a look at the data in `beer.tsv`. First let's verify the file size:

    $ du -h beer.tsv
     20K    beer.tsv

The `du` program shows the disk usage of its inputs, and the `-h` flag means to
display the output in human-readable format. This file is small, but it's good
practice to check this out early. Trying to analyze a file that is larger than
expected could cause unpredictable errors (if the file size exceeds the amount
of available RAM on your computer, you wouldn't want to open it in a text editor).

The `head` command shows you the first few lines of the input file:

    $ head beer.tsv
    Rank    Name    Brewery Type    ABV     WR      Reviews
    1       Heady Topper    The Alchemist   Imperial IPA    8       4.69    3146
    2       Pliny The Younger       Russian River Brewing Company   Imperial IPA    11      4.65    1572
    3       Pliny The Elder Russian River Brewing Company   Imperial IPA    8   4.64    6129
    4       Founders CBS Imperial Stout     Founders Brewing Company    Imperial Stout  10.6    4.63    2026
    5       Founders KBS (Kentucky Breakfast Stout) Founders Brewing Company    Imperial Stout  11.2    4.61    4714
    6       Zombie Dust     Three Floyds Brewing Co. & Brewpub      American Pale Ale       6.4     4.61    2978
    7       Trappist Westvleteren 12 (XII)  Brouwerij Westvleteren (Sint-Sixtusabdij van Westvleteren)              10.2    4.61    2891
    8       Bourbon County Brand Coffee Stout       Goose Island Beer Co.   Imperial Stout  14      4.61    2014
    9       Parabola        Firestone Walker Brewing Co.    Imperial Stout  12.5    4.55    2178 

We can see from this output that our dataset has seven **features**. Four of the
features are **numeric** (real values), and the rest are **categorical** (strings).

The lines that contain data are called **records**. We usually have one record
per line, and an extra line on top for the **header row**. This header row contains
metadata that gives the names of the features in the dataset:

    $ head -n1 beer.tsv
    Rank    Name    Brewery Type    ABV     WR      Reviews

The `head` program gives us the first 10 lines of the file by default, but
the `-n` flag allows us to specify the number of output lines.

We can count the **number of records** in the dataset using the `wc` command:

    $ wc -l beer.tsv
    251 beer.tsv

The `wc` program is for counting words, but passing the `-l` flag tells it to
count lines instead. Using the correspondence between lines and records,
this tells us that the dataset has 250 records (remember, the first row is the
header row).

Our next task is to verify that the **number of features** is consistent throughout the
dataset. This dataset lives in a `.tsv` file, which reminds us that it contains
tab-separated values. Frequently we'll refer to this as a tab-delimited
dataset. The **delimiter** is the character that separates fields from each
other in the file (this is what allows us to draw the correspondence between fields and
features). Tabs (`.tsv`) and commas (`.csv`) are the most common delimiters.

If the number of fields per record varies then our dataset is malformed,
and we'll have trouble trying to load it into [pandas](http://pandas.pydata.org/)
(or into a relational database, etc). This could happen if our data contained
**embedded delimiters** (delimiters used as text).

We have to flex our Unix muscles a little to check the number of fields per
record:

    $ cat beer.tsv | awk -F\t '{print NF}' | sort | uniq -c
    251 7

Notice that we used a number of Unix programs in the line above, and we
concatenated them together using the `|` character. This is called the Unix
**pipe**. The pipe uses the output from one program as the input to another program.

For example, the command above pipes output from `cat` into `awk`, then
pipes the output of `awk` into `sort`, then pipes the output of `sort`
into `uniq`. The pipe is a fundamental tool for working at the command line.
It's intuitive, practical, and very Unix-y.

So the pipe is the glue between Unix programs in this command, but what do the
programs themselves do?

The `cat` program prints the contents of a file to
[stdout](http://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr).
For this reason, `cat` is frequently used to initiate a chain of
Unix commands that uses a file as its input (this is not the only way to do it,
but it's the most flexible & intuitive way).

Next we have `awk`. The ins & outs of `awk` could (and do) fill many books.
Strictly speaking, `awk` is its own programming language, and our
command contains both an invocation and a short `awk` program (set off by
single quotes). This program prints the number of fields per input line, denoted
by `NF`. The `-F` flag tells `awk` which delimiter to use, in this case `\t` for
the tab character.

The `sort` program does what it sounds like: sorts its input. It's necessary
because the next program relies on sorted input.

Next is `uniq`. This program de-duplicates its (sorted) input and produces unique 
output lines. Regarding sorting, note the warning cry that echoes through the
streets of the Unix documentation:

> Repeated lines in the input will not be detected if they are not adjacent, so it
> may be necessary to sort the files first.  
>\- *man uniq*

Passing the `-c` flag couples this output with a count, which
gives us a quick look at the number of occurrences per record in the input
(we'll see later that this is an easy way of generating **frequency distributions** at the
command line).

In the present case, the output from our command tells us we have 250
records (plus a header row) with 7 fields each, so we are in good shape.

