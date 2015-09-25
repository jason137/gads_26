# data exploration at the command line
## 2. looking more closely

Now we know something about our dataset, namely its size & shape and what kind
of data it contains. Now let's dig deeper to see what the data is actually
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

We've already seen most of the programs used in this command. Note that the
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
[numeric sorting](http://stackoverflow.com/questions/4856030/linux-command-sort-according-to-fields-numerical-value),
the `-r` flag says to sort in reverse (descending) order, and 
















