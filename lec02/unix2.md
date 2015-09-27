# data exploration at the command line

## 2. looking more closely

Now we know something about our dataset, namely its size & shape and what kind
of data it contains. Next let's dig deeper to see what the data is actually
telling us.

Take another look at the first few records:

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

There's a field called "Type", and we can see that the data contains
information like Stout, IPA, etc. How can we see the number of records per
type?

    $ cat beer.tsv | cut -f4 | sort | uniq -c | sort -nrk1 | head
    46 Imperial Stout
    40 Imperial IPA
    25 American IPA
    14
    13 Russian Imperial Stout
    10 American Strong Ale
     8 Fruit
     8 American Wild Ale
     6 Old Ale
     6 Gueuze

We've already seen most of these programs. Note that the
result of the first n-1 programs in this command is a sorted **frequency
distribution** of the data. The final call to `head` simply truncates the
distribution to show the 10 most frequently occuring values of "Type"
alongside their counts. We can see from this output that field 4 is blank in 14
rows.

One program we haven't seen yet is `cut`, which outputs only the selected column
from its input. The column to output is denoted by the `-f` flag. Since "Type" is
the fourth field, we retrieve it using the number 4 (note that Unix arrays begin
at 1, not 0 as in Python).

This command also uses a little more power from the `sort` program through its
arguments. The `-n` flag specifies
[numeric sorting]
(http://stackoverflow.com/questions/4856030/linux-command-sort-according-to-fields-numerical-value),
the `-r` flag says to sort in reverse (descending) order, and `-k1` says to use
column 1 as the sort key.

Suppose we wanted to get an idea of the typical ABV (alcohol content) for IPA's.

    $ cat beer.tsv | grep IPA | cut -f5 | sort | uniq -c | sort -nrk1 | head
      11 8
       7 7
       5 9
       5 10
       4 7.5
       3 9.4
       3 6.5
       3 11
       2 9.5
       2 6.8

Again we're familiar with most of these programs, but the exception is `grep`.
The `grep` program is a search tool. Its unusual [name](https://kb.iu.edu/d/abnd) contains an allusion to
the technology that it's based on, namely **regular expressions**. The use of regular
expressions, or [regexes](http://www.diveintopython.net/regular_expressions/),
is a notoriously thorny subject, but one whose basic application is easily
managed and frequently invaluable in data processing.

Searching using regular expressions is performed by **pattern matching**. As
the name implies, this requires both a pattern and some input to match it
against. The regular expression (pattern) is a string of characters that is
meant to represent a broader set of strings. Input strings are compared to the
pattern, and those that belong to this broader set (matches) are produced as output.

In the present case, we've passed the string `IPA` to `grep` as the pattern, so 
`grep` compares each input line to `IPA` and produces lines that match (in
this case, exactly) as output. The final result of the above command is the
top 10 most frequently occuring values of ABV for IPA's, or more precisely, the
first 10 lines of the (reverse) sorted frequency distribution of ABV for records matching
the pattern `IPA`. 

Recall that `uniq` prints counts and values, so we see in particular that 8 is
the most frequently occuring value of ABV for IPA's, and it occurs in 11 records.

We can also use `grep` to look at ABV's for beers that are not IPA's:

    $ cat beer.tsv | grep -v IPA | cut -f5 | sort | uniq -c | sort -nrk1 | head
      13 10
      12 5
       9 9.5
       9 11
       7 9
       7 7.5
       7 6
       7 11.5
       6 10.5
       5 8.5

Passing the `-v` flag to `grep` tells it to invert matches, or to print the
complement of its typical output.

Let's take a look at the data now in a more interactive way, using `less`:

    $ less beer.tsv

The `less` program opens its input file for reading, and it does so in a way
that [minimizes the demands](https://en.wikipedia.org/wiki/Less_(Unix))
placed on your computer's memory. As a result it's
safe to use `less` with large files that you wouldn't be able to open using a
text editor.

Notice that the same arrow up/down and `fn` commands you used to navigate the
`man` pages can be used here too (those `man` pages are really
just text files opened in `less`). Also `gg` goes to the top of the file, and
`G` goes to the end of the file.

One of the useful things about `less` is that it supports pattern matching,
similar to `grep`. For example, to search for occurences of the string `Trappist`,
type `/Trappist` and then `return` at the `less` prompt. Now occurrences of the string
will be highlighted, and you can navigate between them using `n` to move
forward and `N` to move backward.

You can also use `less` to catch input from
[stdin](http://stackoverflow.com/questions/3385201/confused-about-stdin-stdout-and-stderr).
For example, suppose you wanted to look at the (unsorted) frequencies of ABV
across all records:

    $ cat beer.tsv | cut -f5 | sort -n | uniq -c | less
       2 
       1 ABV
       3 4
      12 5
       2 5.2
       1 5.25
       1 5.3
       2 5.4
       3 5.5
       1 5.6
    (...)

Recall that `uniq` displays counts and values, so we see that there are 2
blanks, 1 occurrence of `ABV` (in the header row), 3 occurrences of the
minimum value, and 12 occurrences of the next lowest value. Piping the output
to less allows us to scroll up & down to identify frequently occurring values
and possible clusters, and to get a rough idea of the shape of the
distribution. We can clearly see the tendency for ABV to come in increments of
0.5, for example, as well as the fact that the maximum value is in 

You may have noticed in your explorations that one of the fields is slightly
wonky:

    $ cat beer.tsv | grep Knuckle


    $ cat beer.tsv | grep CuvÌ©e | tr CuvÌ©e Cuvee
    $ cat beer.tsv | grep CuvÌ©e | sed s/CuvÌ©e/Cuvee/g
