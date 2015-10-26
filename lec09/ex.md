<!-- author: Jason Dolatshahi -->

# lec 9 exercises
## decision tree classifiers

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) Define the following terms:
- directed edge
- tree depth
- purity
- local optimum
- leaf node

2) What can you say about the bias & variance properties of a decision tree?
How would you compare these to a linear classifier like logistic regression?

3) Name some important sources of variance in learning a decision tree. What
can we do to counteract these?

4) Are we guaranteed to get the optimal decision tree when we fit the model?
Why or why not?

### yes computers

5) Use the dataset in `abalone.csv` to build a decision tree that predicts the
number of rings (a proxy for age) for each organism. Note that you'll have to
encode the categorical feature (`gender`) to fit the model. How well does your model
perform? What do you think you could do to improve its performance?

Try to build a model that achieves >80% prediction accuracy. What steps does this
require, and how do you measure your results? Is this model still useful?
