<!-- author: Jason Dolatshahi -->

# lec 12 exercises
## k-means clustering

Complete these exercises in groups of 2 or 3. Try to make your responses as
simple as possible.

### no computers

1) Define the following terms:
- separation
- cohesion/inertia
- cluster
- unsupervised learning
- centroid
- silhouette coefficient

2) What's the difference between supervised and unsupervised learning?

3) What role does the distance (or equivalently, similarity) function play
in clustering?

4) How can you determine the right value to use for *k*?

### yes computers

5) Use sklearn to perform k-means clustering on the data in `iris.csv`. Perform
model selection (eg, cross-validate the value of k) using the average
silhouette coefficient across points (you can use
`sklearn.metrics.silhouette_score` to do this easily). What conclusions can you
draw? What preprocessing steps might affect your results?
