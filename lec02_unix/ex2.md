<!-- author: Jason Dolatshahi -->

# lec 2 exercises
## data exploration II

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) Define the following terms:
- frequency distribution
- pattern matching
- `man` page

2) Identify the function of each of these Unix programs. What are some
important flags for these programs?
- `cut`
- `tr`
- `grep`
- `less`
- `sed`

3) What does the pattern in a regular expression represent?

4) How can you use Unix to create a frequency distribution of a particular
feature?

5) T or F: it's important to know whether your numbers are sorted numerically
or lexicographically (not numerically).

6) What's a quick way to count the number of blank values for a particular
field?

7) What makes `less` a safe way to open a large text file?

8) T or F: `sed` replaces each occurrence of the target string by default.

### yes computers

9) Create a frequency distribution of the areas of parks in Brooklyn using the
`datasets/nyc_parks.tsv` file. How would you characterize the shape of this
distribution? What steps could you take to improve its usefulness?

10) Print the 5th line of `datasets/snowfall.tsv`. Now try to do it another
way (don't use `grep` for either).

11) How many lines are in `datasets/Capablanca.pgn`? How many records?

12) The `pgn` files in the `datasets` directory contain data in a format that's
common for storing the results of chess games. Create (separate) frequency distributions
for the first moves of each game in each of these these files. What can you
conclude from your results?
