<!-- author: Jason Dolatshahi -->

# regularization

We've already discussed the pitfalls of overfitting, and the use of a
train/test split to mitigate most of its effects. But some overfitting can
still occur even if we train our model the right way, and there is more we can
do to prevent it.

Note that sklearn returns regularized fits for many models by
default, so if you've ever used it for regression or classification you may
have seen or used this technique already.

## complexity

Overfitting occurs when we begin to fit the noise in our dataset instead of just
the signal, which is the part we want to fit because it will generalize well to
give us good out-of-sample predictions. Another way to say this is that
overfitting occurs when we have too much **complexity** in our model.

We can control for overfitting by applying regularization, which **explicitly
penalizes** the model for adding complexity. The way it does this depends on our
definition of complexity.

Suppose for simplicity we're using a linear regression model (though the
discussion holds for other models as well). In this case we have *Y = β0 + β1
x1 + ... + βn xn + ε*, where in a minor change of notation *β0* plays the role
that *α* played before.

## norms

One way to define complexity is as the overall size of the model coefficients. Then
controlling complexity amounts to minimizing some global measure of their
magnitudes (note that we can't just minimize their sum, because they may have
different signs).

One useful measure of overall magnitude is given by the sum of the absolute
values of the coefficients, *Σ |β|*. Another useful measure is given by the sum of
the squares of the coefficients, *Σ β^2*. These measures are called the **L1-norm**
and the **L2-norm**, respectively.

With these definitions we can add a new complexity constraint to our linear regression
model:

    1) y = Σ βX such that Σ |β| < λ 
    2) y = Σ βX such that Σ β^2 < λ 

The first version of the constrained model is called **L1 regularization** and
the second version is called **L2 regularization** (these are sometimes
confusingly called **lasso regression** and **ridge regression**,
respectively). Another technique called **elasticnet regression** uses a
combination of both the L1 and L2 norms.

## Lagrangian formulation

The equations above can be re-expressed in using another (Lagrangian)
formulation as follows:

    1) y = min (|| y - Σ βX ||^2 + λ ||x||)
    2) y = min (|| y - Σ βX ||^2 + λ ||x||^2)

The Lagrangian formulation incorporates the constraint into the optimization
problem itself; this explicitly associates complexity with a **cost** to the
optimization program that learns the model.

## bias-variance tradeoff
Regularization is a technique for reducing overfitting, which is a symptom of a
model with too much complexity. A too-complex model produces an erratic
**decision boundary** which does not generalize well, and therefore yields
**high-variance** predictions.

You probably noticed that regularization affects the predictions we make, and
therefore pulls our model slightly off target while reducing overfitting. We
only regularize the model up to the point that the drift (bias) we incur is
mode than made up for by the reduction in overfitting (variance). This is a
tangible example of the **bias-variance tradeoff**.
