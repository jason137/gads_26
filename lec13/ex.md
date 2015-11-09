<!-- author: Jason Dolatshahi -->

# lec 13 exercises
## model evaluation

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) Define the following terms:
- recall
- AUC
- ROC space
- false positive rate
- precision
- confusion matrix
- true positive rate

2) Denote a positive record by `y = 1` and a positive prediction by `y' = 1`.
We can write the precision and recall at a threshold `t` as:

    p(t) = Pr(y = 1 | y' = 1)
    r(t) = Pr(y' = 1 | y = 1)

What mathematical relationship do you think these quantities share?

3) How can ROC analysis be incorporated into a cross-validated model selection
process? What remains to be done in order to make out-of-sample predictions?

4) Try to think of some examples of cases where false positives are more costly than
false negatives. Now try think of some examples of cases where the opposite is
true.
