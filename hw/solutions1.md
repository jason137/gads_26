# HW # 1 
## Due: Oct 5th   
   
   
Finish answering the computer exericies from lecture 2   

Copy your ans + terminal output and align it 4 spaces from the left. See the first question as an example. Once complete send us a text file via email  to `zunayed@gmail.com` AND `arisha84@gmail.com`  with the subject `[gads-26][hw1] Fullname`
### Ex1

7) How many records are in datasets/citibike.csv? How many features? Write Unix commands to find these numbers

    $ wc -l citibike.csv
    332

    $ cat citibike.csv | awk -F, '{print NF}' | sort | uniq -c
    332 12


8) Create a sorted frequency distribution of the sizes of files & directories in your home directory using the du program. You will probably want to use a flag to keep the depth manageable.

    $ du -d1 ~ | sort -nrk1

9) Re-create the output from #8 in human-readable format. How might this affect the sorting?

    $ du -hd1 ~ | sort -nrk1
    --> outputs in column 1 are strings, which affects sorting

10) What technical difficulties might you face working with datasets/gdp.csv? Write a Unix command that demonstrates this.

    $ cat gdp.csv | awk -F, '{print NF}' | sort | uniq -c
    235 60
     15 61
    --> number of features varies across rows!

### Ex2

9) Create a frequency distribution of the areas of parks in Brooklyn using the datasets/nyc_parks.tsv file. How would you characterize the shape of this distribution? What steps could you take to improve its usefulness?

    $ cat nyc_parts.tsv | grep Brooklyn | cut -f4 | sort -nr | uniq -c
    --> skewed, heavy tails

10) Print the 5th line of datasets/snowfall.tsv. Now try to do it another way (don't use grep for either).

    $ head -n5 snowfall.tsv | tail -n1
    1921    39.8    4.0

    // decreasing levels of awk slickness 
    $ cat snowfall.tsv | awk '(NR==5)'
    1921    39.8    4.0

    $ cat snowfall.tsv | awk '(NR==5) {print}'
    1921    39.8    4.0

    $ cat snowfall.tsv | awk '(NR==5) {print $0}'
    1921    39.8    4.0

    $ cat snowfall.tsv | awk '{if (NR==5) print}' 
    1921    39.8    4.0

    etc

11) How many lines are in datasets/Capablanca.pgn? How many records?

    $ wc -l Capablanca.pgn
    10704

    $ grep "^1\." Capablanca.pgn | wc -l
    597

12) The pgn files in the datasets directory contain data in a format that's common for storing the results of chess games. Create (separate) frequency distributions for the first moves of each game in each of these these files. What can you conclude from your results?

    $ for file in *.pgn; do echo $file && cat $file | grep "^1\." | cut -d' ' -f1 | sort | uniq -c | sort -nrk1; done

    Capablanca.pgn
     333 1.d4
     202 1.e4
      39 1.Nf3
      18 1.c4
       3 1.e3
       2 1.f4
    Fischer.pgn
     527 1.e4
     172 1.d4
      55 1.Nf3
      53 1.c4
       7 1.g3
       5 1.f4
       4 1.b3
       2 1.b4
       2 1.Nc3
    Kasparov.pgn
     882 1.d4
     788 1.e4
     182 1.Nf3
     176 1.c4
       3 1.g3
       3 1.e3
       1 1.d3
       1 1.b3
       1 1.Nc3

Opening theory has stayed mostly consistent over time (or as you move down the
alphabet), with some variations.
