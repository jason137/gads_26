<!-- author: Jason Dolatshahi -->

# evaluating model performance

Consider a binary classification task (eg, a supervised learning task with two
possible outcomes). We can encode the binary target variable as an integer, so
1 corresponds to the positive outcome, and 0 to the negative outcome. If our
problem was fraud detection, then a transaction labelled 1 would correspond a
transaction we suspect is fradulent.

Suppose that the proportion of transactions that are fradulent is quite low;
many common applications of machine learning deal with **class imbalance**
situations where the ratio of negative to positive records is on the order of
1000 or more. If we were to build a model and judge its effectiveness solely
using accuracy, it would be easy to be misled. A trivial classifier that
labels each record as negative regardless of its features would be 99.9%
accurate in this case, but this assessment does not contain the information we
need to evaluate and compare models.

There are two ways for a model to make an inaccurate prediction in binary
classification: either it assigns a positive label to a record
that should be labelled negative (**false positive**), or it assigns a negative
label to a record that should be labelled positive (**false negative**). These
are sometimes referred to as **type I** and **type II** errors.

Note that there are also two ways to make accurate predictions; **true
positives** and **true negatives** are defined analogously.

Just as class imbalance is a common phenomenon in practical machine learning,
so is the presence of inequal costs associated with either type of inaccuracy.
In fraud detection a false positive could lead to a lost sale or a lost
customer, whereas in digital advertising a false positive may be relatively
cost-free.

Clearly evaluating model performance using a naive measure of accuracy like
**0/1 loss** is not sufficient to address these issues. But we can arrange the
prediction outcomes into a more useful format called a **confusion matrix**
that allows us to be more specific in our evaluation, and that forms the basis
for the other evaluation metrics we'll discuss.

## confusion matrix

The confusion matrix for a binary classification task is simply a 2x2 matrix
with true values of the outcome variable on one axis and predicted values of
the outcome variable on the other axis:

<p align="center">
<img src="../images/conf_mtx.png">

Correct predictions occur on the diagonal of the matrix, while the off-diagonal
entries correspond to incorrect predictions.

A number of useful metrics can be simply derived from the confusion matrix. The
**true positive rate** (TPR) is given by the ratio of true positives to all
positive records, or *TP / (TP + FN)*. Keep in mind that a false negative is a
record that we identify as negative, but is actually positive.

Similarly the **false positive rate** (FPR) is given by the ratio of negatives
incorrectly classified to all negative records, or *FP / (FP + TN)*. Keep in
mind that a false positive is a record that we identify as positive, but is
actually negative.

Note that both of these calculations take place in a single column of the
confusion matrix.

## points in ROC space

We can evaluate and compare classifiers by plotting their TP and FP rates in a
two dimensional plot. The two-dimensional space that this plot depicts is
called **ROC space**:

<p align="center">
<img src="../images/roc_space.png">

Each classifier produces a single confusion matrix, a single tradeoff 
between true positives and false positives, and therefore a single point in ROC
space. ROC stands for "receiver operating characteristic", a vestige of its
origins in signal detection theory.

Note that the point *(0, 0)* corresponds to a classifier that makes no
positive predictions; its false positive rate is zero, but so is its true
positive rate. Similarly, the point *(1, 1)* corresponds to a classifier that
makes no negative predictions; its true positive rate is 100%, but so is its
false positive rate. The diagonal line that connects these points corresponds
to the region of ROC space where *TPR = FPR*; this is the case of random
classification, where the model performs no better (or worse) than a coin toss.

The point (0, 1) corresponds to perfect prediction. This is where we'd like our
model to be, but perfection is rarely attainable. Typical classifiers will land
in the region above the diagonal; these points correspond to models that use
the information in the data to make predictions that are better than random.
Only a pathological classifier will land in the region below the diagonal;
points in this region represent classifiers that use the information
they find in the data incorrectly (eg, to make backwards predictions).

Points near the lower-left of the plot can be regarded as "strict" classifiers;
they keep their false positive rates down by requiring strong evidence to make
a positive prediction, and so true positive rates are also low.

Points near the upper-right of the plot can be regarded as "lenient"
classifiers; they require little evidence to make a positive prediction, so
their true positive rates and false positive rates are both high.

## curves in ROC space

The picture of classification we've been using so far, where a classifier
corresponds to a single point in ROC space, is accurate if the only thing our
classifier can do is predict a label. More generally, a classification model
predicts a probability or a score for a record that can be combined with a
choice of **threshold** to make a binary classifier (recall that this is how
logistic regression works). In this case each threshold value produces a point
in ROC space, and so by varying the threshold we trace out an **ROC curve**:

<p align="center">
<img src="../images/roc_curve.png">

High thresholds correspond to classifiers that require strong evidence for
positive prediction; these occur in the lower-left corner of ROC space as
described above. Similarly, low thresholds correspond to classifiers that
require little evidence for positive prediction, and these occur in the
upper-right corner of ROC space.

The main strength of ROC curves is their ability to graphically depict the tradeoff
between true positives and false positives. In addition to this, ROC curves
also have the property that they are invariant to changes in the class
distribution. As a result, class imbalance does not affect ROC analysis. This
can be seen from the fact that the class distribution is encoded in the ratio
of the columns in the confusion matrix (actual positives / actual negatives),
and ROC analysis uses only within-column ratios, so any changes in class
distribution cancel each other.

## area under the ROC curve

ROC curves are useful as graphical representations of TPR/FPR tradeoff, but in
order to evaluate models in practice we frequently want to represent expected
performance as a scalar value, eg one that can be produced and compared as the
output of a cross-validation routine.

We can use the area under the ROC curve (frequently called the **AUC**) to
achieve this. Since the AUC measures a fraction of the unit square, it will
always be between 0 and 1. And since we expect valid ROC curves to occur in
only half of this region, we similarly expect valid AUC values to range from
0.5 to 1.

The AUC is an average of an ROC curve that's meant to give a 1-dimensional view
of expected performance by averaging over all possible thresholds. It can be
interpreted as the probability that the classifier ranks a randomly chosen
positive record higher than a randomly chosen negative record. Note that AUC
gives a useful way to compare models using [cross-validation]
(http://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html),
but implementing a model for prediction (while targeting a specific point on
the ROC curve) still requires an explicit choice of threshold.

## precision & recall

The concepts of **precision** and **recall** are closely related to (and frequently
confused with) the concepts of ROC analysis, and like their relatives they too can be
derived from the confusion matrix.

It helps to think about these concepts using the language of information
retrieval, the field where they were first used:

<p align="center">
<img src="../images/prec_recall.png">

Our classifier creates a mapping from records to labels, and these labels are
either correct or incorrect. Using the notation in the confusion matrix, the
set of all predictions (the **selected** set) is given by *TP + FP*.

The data our classifier evaluates contains a proportion of positive records,
some of which we identify and some of which we miss. Again, in the notation in
the confusion matrix, this **target** set (sometimes called the relevant set) is
given by *TP + FN*.

The **precision** of a classifier is the ratio of true positives to the
selected set. This ratio measures the relationship between correct positive 
predictions and all predictions; more specifically, it gives the conditional
probability of a positive record given positive prediction. If we denote actual
positive by `y = 1` and a predicted positive by `y' = 1`, then the precision at
a threshold `t` can be written as

    p(t) = P(y = 1 | y' = 1)

The **recall** of a classifier is the ratio of true positives to the target
set. This ratio measures the relationship between correct positive predictions
and all positive records; more specifically, it gives the conditional
probability of positive prediction given a positive record. Using the same
notation as above, we can write the recall at a threshold `t` as

    r(t) = P(y' = 1 | y = 1)

As in ROC analysis, precision and recall can be combined into a scalar value
called **average precision** for use in cross-validation. Average precision is
sensitive to class imbalance, and (as the name implies) penalizes lack of
precision more heavily than ROC AUC does.
