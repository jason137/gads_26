<!-- author: Jason Dolatshahi -->

# lec 7 exercises
## logistic regression

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) What are the main differences between logistic regression and linear
regression?

2) How can you use a regression model for classification?

3) What is the purpose of regularization? How does it work?

### yes computers
4) Look at the image of a logistic regression model being used for
classification in the README for this lecture. How could you draw in the
decision boundary for this model?

5) Have a look at the sklearn
[documentation](http://scikit-learn.org/stable/modules/linear_model.html)
for linear models. Which parts look familiar? Which parts are confusing?

6) Have a look at the sklearn
[api
reference](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression)
for logistic regression. What do each of the input parameters do? Why are their
defaults selected as they are?

7) Use sklearn and the data in `beer.txt` to build a logistic regression model that
predicts the type of beer. How does your model perform? Try to improve it by
coarsening your target variable: instead of trying to predict type, try to
predict whether the beer is a stout or not.
