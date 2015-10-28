<!-- author: Jason Dolatshahi -->

# ensemble classifiers

Ensemble classifiers are typically the best choice for practical machine
learning applications due to their ability to combine models together using
powerful **variance reduction** techniques.

They are formed by collections of **base classifiers** which are combined
together either by averaging predictions or by majority vote. (Note that
averaging takes place before threshholding probabilistic predictions to a class
label, while majority vote takes place after.)

Combining base classifiers together in one of these ways leverages the power of
the LLN to reduce variance across the base classifiers. This is similar to its
use in cross-validation, where we use it to reduce variance across training
folds. The more base classifiers we use, the lower we can push the variance,
but with diminishing marginal returns.

Good base classifiers explore as many candidate decision boundaries (or
**decision surfaces**, in higher dimensions) as possible while keeping aggregate
predictions as close to the true decision surface as possible. Another way of
saying this is that the variance reduction properties of the LLN permit ensemble
classifiers to get the benefits of low bias base classifiers without incurring 
the otherwise high variance that they are associated with. Decision trees (low
bias, high variance) make good base classifiers, and many ensemble techniques are
collections of trees.

## problems in classification

statistical problems
- consider local opt (eg dec trees)
- ensembles can use different initial conditions in opt problem
- LLN

mathematical problems
- consider diagonal dec surface
- approx by several DTs better than single DT
- ensembles expand hypothesis space of dec boundaries
- LLN


## creating multiple bc’s
- introduce randomness into model training
- resampling: randomness in data
- local optimization: randomness in algo

bagging: resampling (boostrapping) training set w/ unif distr
- variance reduction
- each model trained on random subset of training data
- work best w/ high variance base clf’s (deep trees)

boosting: resampling training set w/ adaptive distr
- adjust focus to most difficult records
- prediction task is more difficult at each iteration
- adaptive distr tries hard to fit true dec surface
- bias reduction + variance reduction!
- work best w/ high bias (low var) base clf’s (shallow trees)

random forest
- randomness in algo
- randomly choose one of top k splits at each node
- more bias than base clf, less variance

extremely random forest (extr randomized trees)
- randomized feature + (best of several) randomized threshhold
- somewhat more bias, somewhat less variance

## hyper-parameters

n_estimators: num trees in forest
- larger is better, but more comps
- dim mgl returns

max_features: size of random subsets to consider for splits
- smaller = lower variance, higher bias

tips
- max_features=N —> regression
- max_features=sqrt(N) —> clf
- use fully developed trees (max_depth=None, min_samples_split=1) —> high V

## Q’s
- why might LR not make a good base clf for an ensemble? (low variance)
- how do bagging/boosting/rf address the stat & math problems?

- why does low bias correspond to high variance?
—> high V: explore more of sample space, possible overfitting
—> high B: more systemic error, but more control, possible underfitting

- which of these do you think could be parallelized? which do you think could
  not?
