<!-- author: Jason Dolatshahi -->

# lec 5 exercises
## data transformations

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) Define the following terms:
- monotonic
- nonlinear
- boxplot

### yes computers

1) Create this DataFrame in Python:

       a     log_a
    0  1  0.000000
    1  2  0.693147
    2  3  1.098612
    3  4  1.386294
    4  5  1.609438

Verify that the median of the log values is the same as the log of the median
of the raw values.

2) Now create this DataFrame in Python:

       b      log_b
    0  0 -11.512925     # your value may differ here
    1  1   0.000000
    2  2   0.693147
    3  3   1.098612
    4  4   1.386294
    5  5   1.609438

Write a function that can convert column `b` to logarithms, and verify that the
median of the log values is the same as the log of the median of the raw
values. How do your results differ from question 1?
