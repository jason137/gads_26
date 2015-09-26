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

Recall that `uniq` prints counts and values, so the output
shows us that the most frequently occuring value of ABV for IPA's is 8, and
this value occurs in 11 records.

Again we're familiar with most of these programs, but the exception is `grep`.
The `grep` program is a search tool. Its unusual [name](https://kb.iu.edu/d/abnd) contains an allusion to
the technology that it's based on, namely **regular expressions**. The use of regular
expressions, or [regexes](http://www.diveintopython.net/regular_expressions/),
is a notoriously thorny subject, but one whose basic application is easily
manageable and frequently invaluable in data processing.

Searching using regular expressions is performed by **pattern matching**. As
the name implies, this requires both a pattern and some input to match it
against. The regular expression (pattern) is a string of characters that is
meant to represent a broader set of strings. Input strings are compared to the
pattern, and those that belong to this broader set (matches) are produced as output.

In the present case, we've passed the string `IPA` to `grep` as the pattern, so 
`grep` compares each input line to `IPA` and produce lines that match (in
this case, exactly) as output. The final result of the above command is the
top 10 most frequently occuring values of ABV for IPAs, or more precisely, the
first 10 lines of the sorted frequency distribution of ABV for records matching
the pattern IPA. 

Now suppose alternatively we want to see ABV's for beers that aren't IPA's.

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

less (pattern matching)
tr/sed
- BASH
executable scripts

PANDAS
loading data into pandas
data exploration
summaries
group by

