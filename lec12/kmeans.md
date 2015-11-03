<!-- author: Jason Dolatshahi -->

# clustering

The models we've discussed up to this point are models for **supervised**
learning, meaning they rely on labelled training data to create rules for
generalization. If we don't have labelled data, we can't apply supervised
techniques to make predictions, but we can still apply **unsupervised**
techniques to help enhance our understanding of the data. 

The goal of unsupervised learning is to extract patterns or structure from a
dataset.

## unsupervised learning

- sup goal: make predictions
- unsup goal: extract patterns/structure from data

- want to extract (not impose) structure
- enhances our understanding of data
- model-driven form of data exploration

- model evaluation is less rigorous than in supervised learning

## clustering

- goal: divide data into groups

what is a cluster?
- group of **similar** data points
- think of it as a “potential class”

k-means clustering
- popular, scalable, simple theoretical properties
- requires manual input for value of k

algo logic:
specify k initial **centroids** (means)
- randomly, explicitly, or “smart” (kmeans++)
for each point, assign to nearest centroid
re-calculate centroids
repeat until stopping criterion (tol)
- centroids change by no more than eps

k-means clustering
- nearest neighbor/prototype method
- greedy algo: each record assigned to cluster based on local structure
- recall greedy is related to local optimization; depends on initial conditions
- frequently run a number of times

notes:
- this algo is **k-means**
- use of mean requires **numerical features**
- centroid does not need to be member of dataset
- need to define similarity!

## similarity measures

distance <—> similarity
easiest for numerical data: euclidean distance

## etc

have to specify number of clusters
tends to create clusters of equal size
result = voronoi diagram
clusters (distances) are not scale invariant!

variation (eg for ctg features): **k-medoids**
- centroids need not belong to dataset

choice of similarity depends on data

strings:
- jaccard = IP addresses (4-ples)
- lev = strings

numbers: euclidean

## cluster validation
how do you know how well you’ve done?
difficult to answer, but can make some basic empirical measurements of algo effectiveness
 
- **cohesion/inertia** measures effectiveness within a cluster (want this to be low)
- **separation** measures effectiveness between clusters (want this to be high)

- **sc** combines these (defined per point)
—> takes values between -1 and +1
—> high sep, low coh = sc of 1
—> sc can be < 0 if clusters overlap (bad)
—> can be averaged within cluster or across clusters for higher-level metrics

these numbers can be used to suggest clusters that should be merged, split, etc

can also be used to select value of k (eg model selection)

## fin
lots of differetn clustering techniques, diff strenghts & weaknesses
