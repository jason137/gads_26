<!-- author: Jason Dolatshahi -->

# lec 5 exercises
## data transformations

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) Define the following terms:
- monotonic
- nonlinear

2) Imagine you're waiting on the subway platform. What do you think the
distribution of the heights of people on the subway platform looks like? What
about the distribution of subway waiting times looks like? Why?

3) T or F
- log(xy) = (log x) * (log y)
- the base of the logarithmic transformation affects the shape of the distribution
    of transformed values
- logs convert multiplication to addition
- the log function is "more" nonlinear than the sqrt function

### yes computers

4) Create a DataFrame in Python with a numeric feature containing the values
`[1, 2, 3, 4, 5]`. Now create another feature containing the logs of these
values. Verify that the median of the log values is the same as the log of
the median of the raw values.

5) Create a DataFrame in Python with a numeric feature containing the values
`[0, 1, 2, 3, 4]`. Now create another feature containing the logs of these
values (note that this requires you to think about how the log is calculated).
Verify that the median of the log values is the same as the log of the median
of the raw values. Do your results differ from question 1? Why or why not?

6) Create histograms of the features in `dinosaurs.tsv`. What can you say about
the shape of these distributions? Apply a useful transformation to one of the
features. What did you change?

7) Create a scatterplot of the raw values in `dinosaurs.tsv`. What can you say
about this relationship? Now create a scatterplot using the transformed values
you created in the last question. Does the relationship change?

8) Create a histogram of the values in `state_hts.tsv`. Now increase the number
of bins. Do you see any new behavior emerge?
