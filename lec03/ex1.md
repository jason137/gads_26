<!-- author: Jason Dolatshahi -->

# lec 3 exercises
## pandas

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) Define the following terms:
- namespace
- inner join
- group by
- outer join
- DataFrame
- slice object

2) Write a command that reads `data.tsv` into a pandas DataFrame called `df`.

3) The file `nyc_parks.tsv` contains areas of NYC parks by borough. Do you
think the distribution of these areas is skewed? Why or why not?

4) How could you verify the shape of the distribution of areas in question 3 
at the command line? How could you verify it using pandas?

5) Usually skewness can be detected by the relationship between the mean and
the median, but this relationship does not always hold. What relationships
between mean and meadian would hold in the typical case? What could lead to
these relationships breaking down?

### yes computers

6) Use the file `shakespeare_words.tsv` to display the total words Shakespeare
wrote by genre.

7) Use the file `state_hts.tsv` to print the highest peak for only those states
beginning with the letter 'A'.

8) Use the file `admissions.tsv` to look at a) total admissions rates by gender
and b) departmental admissions rates by gender. What do you think is going on
here?

9) Use the files `presidents.tsv` and `pres_parties.tsv` to find total time in
office by party (hint: you may find the builtin Python `datetime` library useful).

10) The file `epl.tsv` contains half-time and full-time scores for all soccer
(football) matches in the English Premier League for the 2013-14 season. What
is the probability of a team winning if they're ahead at half time? Does this
probability change if the team is the home team (eg Team 1)?
